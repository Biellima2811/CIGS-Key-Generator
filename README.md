# 🔑 CIGS Key Generator

Aplicação desktop desenvolvida em **Python** com **Tkinter/TTK** para gerar chaves de liberação CIGS a partir de um código de desafio.

O projeto foi organizado para separar a **interface gráfica** da **regra de cálculo**, facilitando a leitura, a manutenção e o aprendizado de Python.

## ✨ Funcionalidades

- Interface gráfica com tema escuro.
- Campo para informar o código de desafio.
- Validação de entradas vazias ou inválidas.
- Geração da chave de liberação a partir do desafio informado.
- Exibição do resultado na própria janela.
- Botão para copiar a chave para a área de transferência.
- Atalho com a tecla **Enter** para executar o cálculo.

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal.
- **Tkinter** — construção da interface gráfica.
- **TTK** — estilização de componentes.
- **Programação orientada a objetos** — organização da janela e da lógica de cálculo.

> O Tkinter faz parte da biblioteca padrão do Python na maioria das instalações para desktop. Não há dependências de terceiros no código apresentado.

## 📁 Estrutura do projeto

```text
CIGS-Key-Generator/
├── core/
│   └── key_engine.py      # Validação e cálculo da chave
├── ui/
│   └── main_window.py     # Interface gráfica Tkinter
└── main.py                # Ponto de entrada da aplicação
```

### Responsabilidade de cada arquivo

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Inicializa a janela principal e o loop de eventos do Tkinter. |
| `core/key_engine.py` | Valida o desafio e calcula a chave de liberação. |
| `ui/main_window.py` | Cria os componentes visuais, recebe a entrada e apresenta o resultado. |

## 🚀 Como executar

### Pré-requisitos

- Python 3 instalado.
- Suporte ao Tkinter na instalação do Python.

### 1. Clone o repositório

```bash
git clone https://github.com/Biellima2811/CIGS-Key-Generator.git
```

### 2. Entre na pasta

```bash
cd CIGS-Key-Generator
```

### 3. Execute a aplicação

**Windows:**

```powershell
py main.py
```

**Linux/macOS (com Tkinter instalado):**

```bash
python3 main.py
```

## 📖 Como utilizar

1. Abra a aplicação.
2. Digite o **código de desafio** no campo indicado.
3. Clique em **Gerar Chave de Liberação** ou pressione **Enter**.
4. Confira a chave apresentada no visor.
5. Utilize **Copiar Chave para Área de Transferência** para copiar o resultado.

Se o código informado for inválido, a aplicação apresenta uma mensagem de aviso.

## 🧩 Organização do código

A interface chama o método responsável pelo cálculo sem implementar a regra matemática diretamente:

```python
from core.key_engine import KeyEngine

chave = KeyEngine.gerar_chave("123")
```

Essa separação permite evoluir a interface sem precisar reescrever a lógica de validação e cálculo.

## 🎯 Objetivo do projeto

Além de atender à necessidade de geração de chaves CIGS, este repositório serve como projeto prático de estudos de Python, com foco em:

- Classes e métodos.
- Métodos de classe (`@classmethod`).
- Anotações de tipos (*type hints*).
- Tratamento de exceções (`try`/`except`).
- Eventos e componentes do Tkinter.
- Separação de responsabilidades entre módulos.

## 🔐 Aviso de segurança

Este projeto reproduz uma lógica de cálculo local e **não deve ser considerado, por si só, um sistema seguro de licenciamento ou autenticação**. Em aplicações comerciais, mecanismos de liberação devem ser avaliados conforme os requisitos de segurança e autorização de uso.

## 👨‍💻 Autor

Desenvolvido por [Biellima2811](https://github.com/Biellima2811).

---

*Projeto desenvolvido para prática de Python e interfaces gráficas desktop.*
