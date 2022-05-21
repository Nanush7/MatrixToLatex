"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
"""


class LatexGen:
    """
    Generar LaTeX.
    """
    def __init__(self, matrix, m: int, n: int):
        self.matrix = matrix
        self.m = m
        self.n = n

    def get_latex(self, m_type: str = 'pmatrix') -> str:
        """
        Return LaTeX.
        :return: str.
        """
        start = f'\\begin{{{m_type}}}'
        end = f'\\end{{{m_type}}}'
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
