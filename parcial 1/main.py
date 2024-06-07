#IGNACIO RODOLFO MORALES / PRIMER PARCIAL PROGRAMACION / TM COMISION 113


import bicicletas
import os

def main():
    lista_bicicletas = []
    while True:
        print('\nMenú:')
        print('1) Cargar archivo .CSV')
        print('2) Imprimir lista')
        print('3) Asignar tiempos')
        print('4) Informar ganador')
        print('5) Filtrar por tipo')
        print('6) Informar promedio por tipo')
        print('7) Mostrar posiciones')
        print('8) Guardar posiciones')
        print('9) Salir')
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            def get_path_actual(nombre_archivo):
                import os 
                directorio_actual = os.path.dirname(__file__)
                return os.path.join(directorio_actual, nombre_archivo)

            with open(get_path_actual('bicicletas.csv'), 'r', encoding='utf-8') as archivo:
                lista = []
                encabezado = archivo.readline().strip('\n').split(',')

                for linea in archivo.readlines():
                    bici = {}
                    linea = linea.strip('\n').split(',')
                    id_bike, nombre, tipo, tiempo = linea

                    bici['id_bike'] = int(id_bike)
                    bici['nombre'] = (nombre)
                    bici['tipo'] = (tipo)
                    bici['tiempo'] = (tiempo)
                    lista.append(bici)
        elif opcion == '2':
            for bici in lista:
                print(bici)
        
        elif opcion == '3':
            bicicletas.asignar_tiempos(lista_bicicletas)
        
        elif opcion == '4':
            bicicletas.informar_ganador(lista_bicicletas) #error
        
        elif opcion == '5':
            tipo = input('Ingrese el tipo de biciceta: ')
            nombre_archivo = input('Ingrese el nombre del archivo csv: (DEBE TERMINAR CON .csv) ')
            bicicletas.filtrar_por_tipo(lista_bicicletas, tipo, nombre_archivo)
        
        elif opcion == '6':
            bicicletas.promedio_por_tipo(lista_bicicletas)
        
        elif opcion == '7':
            bicicletas.mostrar_posiciones(lista_bicicletas)
        
        elif opcion == '8':
            nombre_archivo = input('Ingrese el nombre del archivo JSON: (DEBE TERMINAR CON .json) ')
            bicicletas.guardar_posiciones(lista_bicicletas, nombre_archivo)
            print(f'Archivo {nombre_archivo} guardado con exito.')
        
        elif opcion == '9':
            break
        
        else:
            print('Error, intente nuevamente')

if __name__ == '__main__':
    main()



#corregir asignar tiempos informas ganador y crear archivo csv, no llegue profe :(