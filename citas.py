import json
import os
def loadInfoCitas():
    try:
        with open('citas.json','r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return[]
def GuardarCitas(citas):
    with open('citas.json','w') as archivo:
        json.dump(citas, archivo, indent = 4)
#Menu del programa
def MainMenu():
    if __name__:"__main__"
    isActivate = True
    opcion = 0
    while isActivate:
        os.system("clear")
        print('+','-'*34,'+')
        print("|{:^10}{}{:^10}|".format(" ","gestión de citas"," ").upper())
        print('+','-'*34,'+')
        print(" 1.Agregar Cita\n 2.Buscar Cita\n 3.Modificar Cita\n 4.Cancelar Cita\n 5.Salir")
        print('+','-'*34,'+')
        opcion = int(input("Seleccione una opción: "))
        #Agregar Citas
        if (opcion == 1):
            os.system("clear")
            def AgregarCita():
                print('+','-'*34,'+')
                print("|{:^11}{}{:^12}|".format(" ","Agregar citas"," ").upper())
                print('+','-'*34,'+')
                nombre = input("Ingrese el nombre del paciente: ")
                fecha = input("Ingrese la fecha de la cita(dd/mm/aaaa): ")
                hora = input("Ingrese la hora de la cita(hh:mm): ")
                motivo = input("Ingrese el motivo de la consulta: ")
                newCitas = {
                    'nombre': nombre,
                    'fecha': fecha,
                    'hora': hora,
                    'motivo': motivo
                }
                citas = loadInfoCitas()
                citas.append(newCitas)
                GuardarCitas(citas)
                print("La cita esta agregado correctamente.")
                os.system("pause")
            AgregarCita()
        #Buscar las Citas
        elif opcion == 2:
            def BuscarCita():
                os.system("clear")
                print('+','-'*34,'+')
                print("|{:^9}{}{:^10}|".format(" ","Buscador de citas"," ").upper())
                print('+','-'*34,'+')
                criterio = input("Ingrese un criterio de busqueda(nombre,fecha,hora o motivo): ")
                valor = input(f"Ingrese el valor de {criterio}: ")
                citas = loadInfoCitas()
                foundcitas = []
                for cita in citas:
                    if cita[criterio] == valor:
                        foundcitas.append(cita)
                if foundcitas:
                    print("Citas encontradas:")
                    for cita in foundcitas:
                        print("Nombre:", cita['nombre'])
                        print("Fecha:", cita['fecha'])
                        print("Hora:", cita['hora'])
                        print("Motivo:", cita['motivo'])
                        os.system("pause")
                else: 
                    print("No hay citas registradas.")
                    os.system("pause")
            BuscarCita()
        #Modificar las Citas
        elif opcion == 3:
            def ModificarCita():
                os.system("clear")
                print('+','-'*34,'+')
                print("|{:^10}{}{:^10}|".format(" ","edición de citas"," ").upper())
                print('+','-'*34,'+')
                citas = loadInfoCitas()
                if not citas:
                    print("No hay citas registradas.")
                    os.system("pause")
                    return
                print("Selecciones la cita que desea editar:\n")
                for i, cita in enumerate(citas):
                    print(f'{i+1}. Nombre: {cita["nombre"]},Fecha: {cita["fecha"]},Hora: {cita["hora"]},Motivo: {cita["motivo"]}')
                opcion = int(input("\nSeleccione el número que deseas editar: ")) 
                if opcion < 1 or opcion > len(citas):
                    print("Opción Inválida")
                    return
                os.system("clear")
                cita = citas[opcion - 1]
                print("Cita seleccionada:")
                print('Nombre: ',cita['nombre'])
                print('Fecha: ',cita['fecha'])
                print('Hora: ',cita['hora'])
                print('Motivo: ',cita['motivo'])
                nombre = input("\nIngrese el nuevo nombre del paciente (presione enter para omitir): ")
                fecha = input("Ingrese la nueva fecha de la cita ((dd/mm/aaaa) presione enter para omitir): ")
                hora = input("Ingrese la nueva hora de la cita ((hh:mm) presione enter para omitir): ")
                motivo = input("Ingrese el nuevo motivo de la consulta (presione enter para omitir): ")
                if nombre:
                    cita['nombre'] = nombre
                if fecha:
                    cita['fecha'] = fecha
                if hora:
                    cita['hora'] = hora
                if motivo:
                    cita['motivo'] = motivo
                GuardarCitas(citas)
                print("\nLa cita se ha editado correctamente.")
                os.system("pause")
            ModificarCita()
        #Cancelar las Citas
        elif opcion == 4:
            def CancelarCita():
                os.system("clear")
                print('+','-'*34,'+')
                print("|{:^8}{}{:^8}|".format(" ","eliminación de citas"," ").upper())
                print('+','-'*34,'+')
                citas = loadInfoCitas()
                if not citas:
                    print("No hay citas registradas.")
                    os.system("pause")
                    return
                print("Seleccione la cita que desea eliminar:\n")
                for i, cita in enumerate(citas):
                    print(f'{i+1}. Nombre: {cita["nombre"]}, Fecha: {cita["fecha"]}, Hora: {cita["hora"]}, Motivo: {cita["motivo"]}')
                opcion = int(input("\nSeleccione una opción para eliminar: "))
                if opcion < 1 or opcion > len(citas):
                    print("Opción invalida")
                    return
                cita = citas.pop(opcion - 1)
                GuardarCitas(citas)
                print("La cita se ha cancelado correctamente.")
                os.system("pause")
            CancelarCita()
        #Salir del programa
        elif opcion == 5:
            isActivate = False
            print("\n{:^3}{}{:^3}".format(" ","¡Hasta Luego! Gracias por utilizar el programa.\n"," ").upper())
        #else para si colocan otra opcion me salga "opcion invalida"
        else:
            print("Opción Inválida.")
            os.system("pause")
MainMenu()