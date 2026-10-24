"""
ui/main_window.py
Interface Gráfica construída com Tkinter/TTK moderno e Grid estruturado.
"""

from __future__ import annotations
import tkinter as tk
from tkinter import messagebox, ttk

from core.key_engine import KeyEngine


class MainWindow(tk.Tk):
    """Janela principal do Gerador de Chaves."""

    def __init__(self) -> None:
        super().__init__()

        self.title("CIGS Key Generator - CIGS")
        self.geometry("460x360")
        self.minsize(440, 340)
        self.resizable(False, False)

        self._chave_gerada: str = ""

        self._configurar_tema()
        self._construir_interface()

    def _configurar_tema(self) -> None:
        """Aplica a paleta de cores escura e estiliza componentes TTK."""
        self.bg_color = "#1e1e2e"       # Fundo base
        self.fg_color = "#cdd6f4"       # Texto claro
        self.card_bg = "#313244"        # Containers e campos
        self.accent_color = "#89b4fa"   # Azul de destaque
        self.terminal_bg = "#11111b"   # Fundo preto profundo do visor
        self.success_color = "#a6e3a1"  # Verde terminal

        self.configure(bg=self.bg_color)
        estilo = ttk.Style(self)
        estilo.theme_use("clam")

        estilo.configure(".", background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 10))
        estilo.configure("TLabel", background=self.bg_color, foreground=self.fg_color)

        # Botão Primário
        estilo.configure(
            "Primary.TButton",
            background=self.accent_color,
            foreground="#11111b",
            font=("Segoe UI", 10, "bold"),
            borderwidth=0
        )
        estilo.map("Primary.TButton", background=[("active", "#b4befe")])

        # Botão Secundário (Copiar)
        estilo.configure(
            "Secondary.TButton",
            background="#45475a",
            foreground=self.fg_color,
            font=("Segoe UI", 9),
            borderwidth=0
        )
        estilo.map("Secondary.TButton", background=[("active", "#585b70")])

    def _construir_interface(self) -> None:
        """
        Desenha a malha do Grid:
        - Linha 0: Cabeçalho com Título e Subtítulo
        - Linha 1: Bloco de Entrada (Label + Entry)
        - Linha 2: Botão de Execução
        - Linha 3: Visor de Exibição da Chave
        - Linha 4: Botão de Copiar
        """
        self.grid_columnconfigure(0, weight=1)

        # ==================== LINHA 0: CABEÇALHO ====================
        frame_header = tk.Frame(self, bg=self.bg_color)
        frame_header.grid(row=0, column=0, pady=(20, 15), padx=20, sticky="ew")
        frame_header.grid_columnconfigure(0, weight=1)

        lbl_titulo = tk.Label(
            frame_header,
            text="ACESSO RESTRITO - CIGS",
            font=("Segoe UI", 13, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        lbl_titulo.grid(row=0, column=0)

        lbl_sub = tk.Label(
            frame_header,
            text="Digite o código de solicitação exibido no sistema",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg="#a6adc8"
        )
        lbl_sub.grid(row=1, column=0, pady=(4, 0))

        # ==================== LINHA 1: ENTRADA ====================
        frame_input = tk.Frame(self, bg=self.bg_color)
        frame_input.grid(row=1, column=0, pady=(0, 15))

        lbl_desafio = tk.Label(frame_input, text="Código:", font=("Segoe UI", 10, "bold"))
        lbl_desafio.grid(row=0, column=0, padx=(0, 10))

        self.ent_desafio = tk.Entry(
            frame_input,
            bg=self.card_bg,
            fg=self.fg_color,
            insertbackground="white",
            font=("Consolas", 12, "bold"),
            width=18,
            relief="flat",
            justify="center"
        )
        self.ent_desafio.grid(row=0, column=1, ipady=3)
        self.ent_desafio.focus_set()

        # Vincula o Enter do teclado à função de calcular
        self.ent_desafio.bind("<Return>", lambda event: self._executar_calculo())

        # ==================== LINHA 2: BOTÃO CALCULAR ====================
        btn_calcular = ttk.Button(
            self,
            text="Gerar Chave de Liberação",
            style="Primary.TButton",
            command=self._executar_calculo
        )
        btn_calcular.grid(row=2, column=0, pady=(0, 15), ipadx=12, ipady=4)

        # ==================== LINHA 3: VISOR DA CHAVE ====================
        frame_visor = tk.Frame(self, bg=self.terminal_bg, padx=15, pady=12, highlightthickness=1)
        frame_visor.config(highlightbackground="#45475a")
        frame_visor.grid(row=3, column=0, sticky="ew", padx=40, pady=(0, 10))
        frame_visor.grid_columnconfigure(0, weight=1)

        self.lbl_resultado = tk.Label(
            frame_visor,
            text="[ AGUARDANDO DESAFIO ]",
            font=("Consolas", 13, "bold"),
            bg=self.terminal_bg,
            fg="#585b70"
        )
        self.lbl_resultado.grid(row=0, column=0)

        # ==================== LINHA 4: BOTÃO COPIAR ====================
        self.btn_copiar = ttk.Button(
            self,
            text="Copiar Chave para Área de Transferência",
            style="Secondary.TButton",
            state="disabled",
            command=self._copiar_para_clipboard
        )
        self.btn_copiar.grid(row=4, column=0, ipadx=8, ipady=2)

    def _executar_calculo(self) -> None:
        """Captura o valor, valida no Service e atualiza a interface."""
        entrada = self.ent_desafio.get()

        try:
            chave_calculada = KeyEngine.gerar_chave(entrada)
            self._chave_gerada = str(chave_calculada)

            # Atualiza o visor com sucesso
            self.lbl_resultado.config(text=f"CHAVE: {self._chave_gerada}", fg=self.success_color)
            self.btn_copiar.config(state="normal")

        except ValueError as erro:
            messagebox.showwarning("Atenção", str(erro))
            self.ent_desafio.delete(0, tk.END)
            self.ent_desafio.focus_set()

    def _copiar_para_clipboard(self) -> None:
        """Copia a chave calculada diretamente para o clipboard do Windows."""
        if self._chave_gerada:
            self.clipboard_clear()
            self.clipboard_append(self._chave_gerada)
            messagebox.showinfo("Sucesso", f"Chave {self._chave_gerada} copiada com sucesso!")