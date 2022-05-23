"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
Hecho para Belén.
"""
import re


class LatexGen:
    """
    Generar LaTeX.
    """
    MATRIX_TYPE = ('m', 'p', 'b', 'B', 'v', 'V', 'small')

    def __init__(self, matrix, m: int, n: int):
        self.matrix = matrix
        self.m = m
        self.n = n

    def get_matrix(self, m_type: MATRIX_TYPE = 'p') -> str:
        """
        Return LaTeX.
        :return: str.
        """
        start = f'\\begin{{{m_type}matrix}}'
        end = f'\\end{{{m_type}matrix}}'
        rows = ''
        for i in range(self.m):
            row = '  '
            for j in range(self.n):
                if j == 0:
                    row += f'{str(self.matrix[i, j])}'
                else:
                    row += f' & {str(self.matrix[i, j])}'
            row += ' \\\\\n'
            rows += row

        latex_code = f'{start}\n{rows}{end}'
        return latex_code

    @staticmethod
    def get_fraction(value: str) -> str:
        """
        Generar fracción en LaTeX.
        """
        # Separar los números de la fracción.
        operands = value.split('/')

        # Revisar que el número del denominador no sea 0.
        if operands[1] == '0':
            raise ZeroDivisionError

        return rf'{{{operands[0]} \over {operands[1]}}}'

    @staticmethod
    def get_index(value: str, operator: str) -> str:
        """
        Generar índice en LaTeX.
        """
        operands = value.split(operator)
        # Lo que queda a la derecha del operador
        # hay que separarlo donde haya espacios.
        right_operand = re.search(r'[\^/_]', operands[1])
        if right_operand is None:
            row = rf'{operands[0]}{operator}{{{operands[1]}}}'
        else:
            match_index = right_operand.span()[0]
            row = rf'{operands[0]}{operator}{{{right_operand.string[0:match_index]}}}{right_operand.string[match_index:]}'

        return row
