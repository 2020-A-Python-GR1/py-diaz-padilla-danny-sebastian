from Parameters import Parameters  # para generar congruencia
from strings.Strings import Strings as s
from models.ChatGroup import ChatGroup as Chat
from models.Integrant import Integrant

# Asegurarse primero que el diccionario a utilizar tenga todos las
# claves necesarias
s.changeLanguage(Parameters.language_spanish)
run = True


chats_counter = 1
group_chats = dict()  # key -> id, value -> object
# Habrá un diccionario con todos los integrantes para evitar repeticiones innecesarias
total_integrants = dict()  # key -> id, value -> object


def createIntegrant(integrant_id):
    pass


def assignIntegrantsToChatGroup():
    pass


def createChatGroup(chat_id):
    name_group = input("DEBUG: Nombre del grupo: ")
    capacity_maximun = int(input("DEBUG: Capacidad máxima "))
    group_chats[chat_id] = Chat(chat_id, name_group, capacity_maximun)

    option_integrants = input("DEBUG: Agregar integrantes? (s: si, N: no) ")

    if option_integrants == "s":
        if len(total_integrants) > 0:
            assignIntegrantsToChatGroup()
        else:
            print("DEBUG: Todavia no hay integrantes creados, desea crear uno y asignarlo? (s: si, N: no) ")
            if option_integrants == "s":
                createIntegrant(integrant_id=Integrant.generateNewId())



def getActualIntegrants():
    integrants_name = ""
    for i, integrant in enumerate(total_integrants.values()):
        integrants_name += "(" + integrant.user_name + " con ID= " + str(integrant.user_id) +")"
        if i < len(total_integrants) - 2:
            integrants_name += ", "
        if i == len(total_integrants) - 2:
            integrants_name += s.dictionary["string_and"] + " "
    return integrants_name


def getActualGroupsOfChats():
    groups_name = ""
    for i, group_chat in enumerate(group_chats.values()):
        groups_name += "(" + group_chat.name_group + " con ID = " + str(group_chat.chat_id) + ")"
        if i < len(group_chats) - 2:
            groups_name += ", "
        if i == len(group_chats) - 2:
            groups_name += s.dictionary["string_and"] + " "
    return groups_name


while run:

    try:

        print("Lista actual de nombres de grupos: " + getActualGroupsOfChats())
        option = int(input(
            """
            
            DEBUG:
            Escriba una opción:
            1. Crear chat grupal
            2. Leer la información de un chat grupal
            3. Actualizar un dato de un chat grupal
            4. Eliminar un chat grupal
            5. Gestionar Integrantes de un chat grupal
            100. Salir
            Opción: """
        ))

        if option == 1:
            chat_id = Chat.generateNewId()
            createChatGroup(chat_id)
            print("DEBUG: Se ha creado el grupo con id=%i " % chat_id)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 100:
            run = False
        else:
            print("DEBUG: Opcion no válida")

    except Exception as error:
        print(s.dictionary["msg_error_general"], error)

print("DEBUG: Fin del programa")
