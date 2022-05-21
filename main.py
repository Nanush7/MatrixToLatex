"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
Hecho para Belén.
"""
import os
from time import sleep
from typing import List
import pyperclip

import numpy as np

from latex import LatexGen
from output import Output
from utils import query_yes_no


class App:
    """
    Agregar descripción.
    """

    def __init__(self):
        use_colors = query_yes_no('¿Utilizar salida de colores?', 'si')
        self.out = Output(color=use_colors)
        self.os = os.name
        self.m: int = 0
        self.n: int = 0

    def get_matrix(self):
        """
        Obtener la matriz del sistema a calcular.
        """
        # Obtener cantidad de filas y columnas.
        while True:
            try:
                # m = filas (ecuaciones).
                # n = columnas (incógnitas).
                m = int(input('m (cantidad de filas) = '))
                n = int(input('n (cantidad de columnas) = '))
                self.m = m
                self.n = n
                if m < 1 or n < 1:
                    self.out.error('m y n deben ser mayores o iguales a 1.')
                    continue
                break
            except ValueError:
                self.out.error('m y n deben ser números de tipo int.')

        self.clear()

        # Obtener valores.
        self.out.info(
            'Para ingresar una fila a la matriz, tenés que escribir todos los coeficientes separados por espacios.\n')
        print('Para poner una fracción bla/bla.')
        print('Para poner un subíndice: bla_bla (la gracia es que no tenés que poner bla_{bla}).')
        print('Para poner un superíndice: bla^bla (lo mismo de arriba).\n')
        self.out.warning('No se pueden usar los tres operadores de arriba al mismo tiempo (Próximamente (? ).\n')
        self.out.info(f'Tenés que poner {n} números por fila.')

        # ¿float64?
        matrix = np.zeros((m, n), dtype=np.chararray)

        # Se agrega fila por fila a la matriz.
        for row_index in range(m):
            print('----------------------')
            while True:
                self.out.info(f'Fila: {row_index + 1}')

                try:
                    user_input = input('--> ')
                    row_list = self._get_string_list(user_input)
                    if len(row_list) != n:
                        raise IndexError

                    # Preguntar al usuario si la fila es correcta.
                    if query_yes_no('¿Continuar?', 'si'):
                        # Agregar la fila a la matriz.
                        matrix[row_index] = row_list
                        break

                except IndexError:
                    self.out.error(f'La fila debe tener {m} columnas.')
                except ZeroDivisionError:
                    sleep(1)
                    self.out.error('Acaba de morir un gatito :(')
                    sleep(2)

        return LatexGen(matrix, m, n)

    @staticmethod
    def _get_string_list(string_input: str) -> List[str]:
        # Separar el input donde hay espacios.
        string_list = string_input.split(' ')

        # Verificar y crear objetos de fracciones.
        for index, val in enumerate(string_list):  # TODO: Permitir los tres operadores.
            if '/' in val:
                # Obtener los números de la fracción.
                values = val.split('/')

                # Revisar que el número del denominador no sea 0.
                if values[1] == '0':
                    raise ZeroDivisionError

                # Reemplazar por la fracción el LaTeX.
                string_list[index] = rf'{{{values[0]} \over {values[1]}}}'

            elif '_' in val:
                # Generar subíndice en LaTeX.
                values = val.split('_')
                string_list[index] = rf'{values[0]}_{{{values[1]}}}'

            elif '^' in val:
                # Generar subíndice en LaTeX.
                values = val.split('^')
                string_list[index] = rf'{values[0]}^{{{values[1]}}}'

        return string_list

    def clear(self) -> None:
        if self.os == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def run(self):
        """
        Correr aplicación.
        """
        self.clear()

        self.out.info('Ctrl-C para salir.')

        matrix = self.get_matrix()

        self.clear()

        result = matrix.get_latex()
        self.out.success('LaTeX:\n')
        print(result + '\n')

        if query_yes_no('¿Querés copiarlo al portapapeles?'):
            pyperclip.copy(result)

        del matrix


if __name__ == '__main__':
    app = App()
    while True:
        try:
            app.run()
        except KeyboardInterrupt:
            print('Ta luego.')
            break
