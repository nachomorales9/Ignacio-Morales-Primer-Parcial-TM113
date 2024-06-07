import csv
import json
import random
from typing import List, Dict

def cargar_archivo_csv(nombre_archivo: str) -> List[Dict[str, str]]:
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        return [row for row in reader]

def imprimir_lista(bicicletas: List[Dict[str, str]]):
    for bicicleta in bicicletas:
        print(bicicleta)

def guardar_csv(bicicletas: List[Dict[str, str]], nombre_archivo: str):
    if bicicletas:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=bicicletas[0].keys())
            writer.writeheader()
            writer.writerows(bicicletas)

def asignar_tiempos(bicicletas: List[Dict[str, str]]):
    for bicicleta in bicicletas:
        bicicleta['tiempo'] = str(random.randint(50, 120))
    guardar_csv(bicicletas, 'asignar_tiempos.csv')
    imprimir_lista(bicicletas)

def filtrar_por_tipo(bicicletas: List[Dict[str, str]], tipo: str, nombre_archivo: str):
    filtradas = [bicicleta for bicicleta in bicicletas if bicicleta['tipo'].lower() == tipo.lower()]
    guardar_csv(filtradas, nombre_archivo)
    print(f'Archivo {nombre_archivo} creado con éxito.')

def promedio_por_tipo(bicicletas: List[Dict[str, str]]):
    tipos = set(bicicleta['tipo'] for bicicleta in bicicletas)
    promedios = {}
    for tipo in tipos:
        tiempos = [int(bicicleta['tiempo']) for bicicleta in bicicletas if bicicleta['tipo'] == tipo]
        promedio = sum(tiempos) / len(tiempos)
        promedios[tipo] = promedio
    for tipo, promedio in promedios.items():
        print(f'Promedio para {tipo}: {promedio:.2f}')

def ordenar_biblio(bicicletas: List[Dict[str, str]], key=lambda x: (x['tipo'], int(x['tiempo']))):
    for i in range(1, len(bicicletas)):
        key_item = bicicletas[i]
        j = i - 1
        while j >= 0 and key(bicicletas[j]) > key(key_item):
            bicicletas[j + 1] = bicicletas[j]
            j -= 1
        bicicletas[j + 1] = key_item
    return bicicletas

def mostrar_posiciones(bicicletas: List[Dict[str, str]]):
    bicicletas_ordenadas = ordenar_biblio(bicicletas, key=lambda x: (x['tipo'], int(x['tiempo'])))
    imprimir_lista(bicicletas_ordenadas)

def guardar_posiciones(bicicletas: List[Dict[str, str]], nombre_archivo: str):
    bicicletas_ordenadas = ordenar_biblio(bicicletas, key=lambda x: (x['tipo'], int(x['tiempo'])))
    with open(nombre_archivo, mode='w', encoding='utf-8') as archivo:
        json.dump(bicicletas_ordenadas, archivo, ensure_ascii=False, indent=4)
