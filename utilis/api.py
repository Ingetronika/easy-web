import pandas as pd
import tkinter as tk
from tkinter import messagebox
from utilis.datos import Datos

class ApiCorreccion:
    def __init__(self, api, temperatura):
        self.api = api
        self.temperatura = temperatura
        self.datos_api = Datos('C:/Users/Hugo Tovio/Desktop/EASY_v2/tablas')
        self.tablas_api = self.datos_api.obtener_datos_json()
        
        
        # los valores de api corregido están en el primer json de tablas api_corregido.json
        self.valores = list(self.tablas_api[2].values())
       

    def crear_matriz(self):
        # Ruta de los archivos CSV en la carpeta de tu proyecto
        file_path_1 = 'C:/Users/Hugo Tovio/Desktop/EASY_v2/tablas/api_corregido.csv'
        file_path_2 = 'C:/Users/Hugo Tovio/Desktop/EASY_v2/tablas/factor_correccion.csv'
        
        # Leer los archivos CSV
        df1 = pd.read_csv(file_path_1)
        df2 = pd.read_csv(file_path_2)
        
        # Convertir los DataFrames a matrices (listas de listas)
        matrix_corregido = df1.values.tolist()
        matrix_factor_correccion = df2.values.tolist()
        
        return matrix_corregido, matrix_factor_correccion


    def encontrar_indices(self):
        key_api = next(k for k, v in self.tablas_api[2].items() if v == self.api)
        key_tem = next(k for k, v in self.tablas_api[3].items() if v == self.temperatura)
        
        return key_api, key_tem
    
    def hallar_api_corregido(self, row_index, col_index, matrix):
        try:
            valor = matrix[row_index][col_index]
            return valor
        except IndexError:
            return "Índice fuera de rango"
    
    def hallar_factor_correccion(self, row_index, col_index, matrix):
        try:
            valor = matrix[row_index][col_index]
            return valor
        except IndexError:
            return "Índice fuera de rango"
    
    def encontrar_valor_mas_cercano(self, numero, lista):
        diferencia_minima = float('inf')
        valor_mas_cercano = None

        for valor in lista:
            diferencia = abs(numero - valor)
            if diferencia < diferencia_minima:
                diferencia_minima = diferencia
                valor_mas_cercano = valor
        
        return valor_mas_cercano

    def corregir_correccion(self):
        matrix_api_corregido, matrix_factor_correccion = self.crear_matriz()
        api_indice, temperatura_indice = self.encontrar_indices()
        # Ajuste según base 0
        apicor = self.hallar_api_corregido(int(temperatura_indice) - 1, int(api_indice), matrix_api_corregido)
        
        if isinstance(apicor, str):  # Manejo de errores en apicor
            print(f"Error: {apicor}")
            return None, None
        
        api_aprox = self.encontrar_valor_mas_cercano(apicor, self.valores)
              
        if api_aprox is None:
            print("No se encontró un valor cercano.")
            return None, None
        
        posicion = self.valores.index(api_aprox)
        factor_correccion = self.hallar_factor_correccion(int(temperatura_indice) - 1, int(posicion), matrix_factor_correccion) / 10000
        
        if isinstance(factor_correccion, str):  # Manejo de Errores en factor_correccion
            print(f"Error: {factor_correccion}")
            return None, None
        
        return apicor, factor_correccion



