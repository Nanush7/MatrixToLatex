"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
Hecho para Belén.
"""


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
        values = value.split('/')

        # Revisar que el número del denominador no sea 0.
        if values[1] == '0':
            raise ZeroDivisionError

        return rf'{{{values[0]} \over {values[1]}}}'

    @staticmethod
    def get_superscript(value: str) -> str:
        """
        Generar superíndice en LaTeX.
        """
        values = value.split('^')
        return rf'{values[0]}^{{{values[1]}}}'

    @staticmethod
    def get_subscript(value: str) -> str:
        """
        Generar subíndice en LaTeX.
        """
        values = value.split('_')
        return rf'{values[0]}_{{{values[1]}}}'
