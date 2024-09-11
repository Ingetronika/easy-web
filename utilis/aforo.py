import math

from utilis.datos import Datos

class CalculadoraTanque:
    def __init__(self,altura_inicial,volumen_bruto_recibido,tanque):
        self.altura_inicial=altura_inicial
        self.volumen_bruto_recibido=volumen_bruto_recibido
        self.tanque=tanque
        
        
        self.tanques=[{
    662: 176.20,
    480: 14244.02,
    295: 28490.33,
    660: 377.85,
    475: 14628.98,
    290: 28875.44,
    655: 761.13,
    470: 15014.01,
    285: 29260.55,
    650: 1145.95,
    465: 15399.05,
    280: 29645.66,
    645: 1530.93,
    460: 15784.09,
    275: 30030.77,
    640: 1916.35,
    455: 16169.12,
    270: 30415.88,
    635: 2302.27,
    450: 16554.16,
    265: 30800.99,
    630: 2688.07,
    445: 16939.19,
    260: 31186.10,
    625: 3073.07,
    440: 17324.23,
    255: 31571.21,
    620: 3457.63,
    435: 17709.27,
    250: 31956.32,
    615: 3842.19,
    430: 18094.30,
    245: 32341.43,
    610: 4226.98,
    425: 18479.34,
    240: 32726.54,
    605: 4612.41,
    420: 18864.38,
    235: 33111.65,
    600: 4998.18,
    415: 19249.41,
    230: 33496.76,
    595: 5383.96,
    410: 19634.45,
    225: 33881.87,
    590: 5769.74,
    405: 20019.48,
    220: 34266.98,
    585: 6155.51,
    400: 20404.52,
    215: 34652.09,
    580: 6541.29,
    395: 20789.56,
    210: 35037.20,
    575: 6927.06,
    390: 21174.59,
    205: 35422.31,
    570: 7312.84,
    385: 21559.63,
    200: 35807.42,
    565: 7698.61,
    380: 21944.67,
    195: 36192.53,
    560: 8084.39,
    375: 22329.70,
    190: 36577.64,
    555: 8470.17,
    370: 22714.74,
    185: 36962.75,
    550: 8855.94,
    365: 23099.77,
    180: 37347.86,
    545: 9241.72,
    360: 23484.81,
    175: 37732.97,
    540: 9627.49,
    355: 23869.85,
    170: 38118.08,
    535: 10013.20,
    350: 24254.88,
    165: 38503.19,
    530: 10398.24,
    345: 24639.92,
    160: 38888.30,
    525: 10782.81,
    340: 25024.96,
    155: 39273.41,
    520: 11167.37,
    335: 25409.99,
    150: 39658.52,
    515: 11551.93,
    330: 25795.03,
    145: 40043.63,
    510: 11936.49,
    325: 26180.06,
    140: 40428.74,
    505: 12321.05,
    320: 26565.10,
    135: 40813.85,
    500: 12705.62,
    315: 26950.14,
    130: 41198.96,
    495: 13090.18,
    310: 27335.17,
    125: 41584.07,
    490: 13474.74,
    305: 27720.21,
    120: 41969.18,
    485: 13859.30,
    300: 28105.25,
    115.1: 42346.59,1: 76.98,
    2: 153.96,
    3: 230.94,
    4: 307.92,
    5: 384.90,
    6: 461.88,
    7: 538.86,
    8: 615.84,
    9: 692.83, 0.1: 7.70,
    0.2: 15.40,
    0.3: 23.09,
    0.4: 30.79,
   0.5: 38.49,
   0.6: 46.19,
   0.7: 53.89,
   0.8: 61.58,
   0.9: 69.28
}

]
        
    
        

    def mostrar_volumen(self, diccionario,numero ):
        if numero == 0:
            return 0

        if str(numero) in diccionario:
            nr=numero/10
            parte_decimal, parte_entera = math.modf(nr)
            claves=[parte_entera,parte_decimal]
            

        if 11 <= numero <= 99:
            primer_digito = numero // 10
            segundo_digito = (numero % 10) / 10
            claves = [primer_digito, segundo_digito]

            suma = sum(diccionario.get(str(clave), 0) for clave in claves)
            return round(suma, 2)

        claves = [math.floor(numero / 100) * 10]
        if numero >= 100:
            n = str(numero)
            claves.extend([int(n[2]), int(n[3]) / 10] if len(n) > 3 else [int(n[1]), int(n[2]) / 10])
        
        suma = sum(diccionario.get(str(clave), 0) for clave in claves)
        return round(suma, 2)




    def mostrar_altura(self, volume, aforo):
        aforo_tanque=self.preprocesar_datos(aforo)
        sorted_heights = sorted(aforo_tanque.keys())
        lower_height = None
        upper_height = None
        
        for i in range(len(sorted_heights) - 1):
            h1 = sorted_heights[i]
            h2 = sorted_heights[i + 1]
            
            v1 = aforo_tanque[h1]
            v2 = aforo_tanque[h2]
            
            if v1 <= volume <= v2:
                lower_height = h1
                upper_height = h2
                break  # Una vez encontrado el rango, podemos salir del bucle
        
        if lower_height is None or upper_height is None:
            return None  # El volumen está fuera del rango de datos
        
        v1 = aforo_tanque[lower_height]
        v2 = aforo_tanque[upper_height]
        
        height = lower_height + (volume - v1) * ((upper_height - lower_height) / (v2 - v1))
        
        return round(height * 10)
    def preprocesar_datos(self,aforo_tanque_json):
        """
        Convierte un diccionario JSON con claves en formato de cadena a claves numéricas (int o float).
        """
        aforo_tanque = {}
        for key, value in aforo_tanque_json.items():
            try:
                # Intenta convertir la clave a un número
                numeric_key = float(key)
                aforo_tanque[numeric_key] = value
            except ValueError:
                # Si no se puede convertir, maneja el error aquí
                print(f"Advertencia: La clave '{key}' no es un número válido y será ignorada.")
        return aforo_tanque




