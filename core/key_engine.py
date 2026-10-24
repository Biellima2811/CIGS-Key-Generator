"""
core/key_engine.py
Módulo responsável exclusivamente pelo cálculo da chave de liberação CIGS.
"""
from __future__ import annotations

class KeyEngine:
    """Concentra as regras matemáticas e validações do desafio de liberação."""
    MULTIPLICADOR: int = 1337
    INCREMENTO: int = 9842

    @classmethod
    def gerar_chave(cls, entrada_desafio: str) -> int:
        """
        Valida a entrada e calcula a chave de liberação.
        Args:
            entrada_desafio: Texto digitado pelo usuário.
        Returns:
            int: Chave resultante do cálculo.
        Raises:
            ValueError: Se o valor estiver vazio, não for numérico ou for negativo.
        """
        texto_limpo = entrada_desafio.strip()

        if not texto_limpo:
            raise ValueError('O código de desafio não pode estar vazio')

        if not texto_limpo.isdigit():
            raise ValueError('O codigo de desafio deve conter apenas números inteiros, sem caracteres ou negativos.')

        codigo_numerico = int(texto_limpo)
        return (codigo_numerico * cls.MULTIPLICADOR) + cls.INCREMENTO