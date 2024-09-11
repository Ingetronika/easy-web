import os
import json
import pandas as pd

class Datos:
    def __init__(self, ruta_carpeta):
        """
        Inicializa la clase con la ruta de la carpeta que contiene los archivos JSON y CSV.
        
        :param ruta_carpeta: Ruta a la carpeta con archivos JSON y CSV
        """
        self.ruta_carpeta = ruta_carpeta
        self.lista_diccionarios = []
        self.lista_dataframes = []
        self.cargar_datos()

    def cargar_datos(self):
        """
        Lee todos los archivos JSON y CSV en la carpeta especificada y almacena
        sus contenidos en listas separadas.
        """
        try:
            # Lista todos los archivos en la carpeta
            archivos = os.listdir(self.ruta_carpeta)

            # Filtra los archivos JSON y CSV
            archivos_json = [archivo for archivo in archivos if archivo.endswith('.json')]
            archivos_csv = [archivo for archivo in archivos if archivo.endswith('.csv')]

            # Procesa archivos JSON
            for archivo_json in archivos_json:
                ruta_archivo = os.path.join(self.ruta_carpeta, archivo_json)
                with open(ruta_archivo, 'r') as archivo:
                    # Carga el contenido del archivo JSON en un diccionario
                    diccionario = json.load(archivo)
                    # Añade el diccionario a la lista
                    self.lista_diccionarios.append(diccionario)

            # Procesa archivos CSV
            for archivo_csv in archivos_csv:
                ruta_archivo = os.path.join(self.ruta_carpeta, archivo_csv)
                # Lee el archivo CSV en un DataFrame
                dataframe = pd.read_csv(ruta_archivo)
                # Añade el DataFrame a la lista
                self.lista_dataframes.append(dataframe)
        
        except Exception as e:
            print(f"Error al cargar datos: {e}")

    def obtener_datos_json(self):
        """
        Devuelve la lista de diccionarios leída desde los archivos JSON.

        :return: Lista de diccionarios
        """

        return self.lista_diccionarios

    def obtener_datos_csv(self):
        """
        Devuelve la lista de DataFrames leída desde los archivos CSV.

        :return: Lista de DataFrames
        """
        return self.lista_dataframes


