
from Parameters import Parameters  # para generar congruencia
from models.PickleData import storeData



# Ejecutar cada vez que se agregue una palabra al diccionario.

dictionary_es = {
    "string_connected": "Conectado",
    "string_disconnected": "Desconectado",
    "string_unknown": "Desconocido",
    "string_yes": "Si",
    "string_no": "No",
    "string_language": "Idioma",
    "string_look_for": "Buscar",
    "string_search": "Búsqueda",
    "string_create": "Crear",
    "string_update": "Actualizar",
    "string_delete": "Delete",
    "string_details": "Detalles",
    "string_none": "Ninguno",
    "string_id": "Id",
    "string_selection": "Selección",
    "string_date": "Fecha",
    "string_creation": "Creation",
    "string_state": "Estado",
    "string_active": "Activo",
    "string_inactive": "Inactivo",
    "string_cancel": "Cancelar",
    "text_update_list": "Actualizar lista",
    "text_create_grupal_chat": "Crear chat grupal",
    "text_manage_integrants": "Administrar Integrantes",
    "text_creation_of_integrant": "Creación de un integrante",
    "text_update_integrants": "Actualización de un integrante",
    "text_update_groups_chat": "Actualización de un grupo de chat",
    "text_creation_of_chat": "Creación de grupo chat",
    "text_is_allowed_to_talk": "Se le permite hablar",
    "text_actual_integrants": "Integrantes actuales",
    "text_rest_of_integrants": "Integrantes restantes",
    "text_group_name": "Nombre del grupo",
    "text_maximun_capacity": "Capacidad máxima",
    "text_date_creation": "Fecha de creación",
    "text_dont_forget_to_update_try_again": "No olvide actualizar la lista, intente de nuevo",
    "text_update_of_chat": "Actualización de grupo de chat",
    "text_create_integrant": "Creación de un integrante",
    "text_manage_of_integrants": "Administración de integrantes",
    "text_manage_of_chats": "Administración de grupos de chat",
    "text_update_of_integrants": "Actualización de un integrante",
    "text_user_name": "Nombre de usuario",
    "text_main_window": "VENTANA PRINCIPAL",
    "format_summary_chat_group":
        """DETALLES DEL CHAT DE GRUPO
        
        Chat id: %i
        
        Nombre del grupo: %s
        
        Capacidad máxima del grupo: %i integrantes
        
        Fecha de creación: %s
        
        Activo: %s
        
        Retraso de señal promedio: %.2f
        
        Integrantes: 
        %s
        """,
    "format_id_user_integrant": "Nombre de usuario: %s, Id: %i\n",
    "format_summary_integrant":
        """ DETALLES DEL INTEGRANTE
        
        Id del integrante: %i
        Nombre del integrante: %s
        Se unió el %s
        Estado: %s
        Se le permite hablar: %s
        Score de participación: %.2f
        """,
    "msg_error_general":
        """¡Ha ocurrido un error, inténtelo de nuevo verificando que haya hecho correctamente la operación!""",

    "msg_search_found_and_selected": "Búsqueda encontrada y seleccionada",
    "msg_search_not_found": "Búsqueda no encontrada",
    "msg_should_select_something_first_from_actual": "Debería seleccionar un elemento de la lista de integrantes actuales, primero",
    "msg_should_select_something_first_from_rest": "Debería seleccionar un elemento de la lista de integrantes que no han sido agregados, primero",
    "msg_success_deleted": "Eliminado con éxito",
    "msg_that_name_already_exists": "Ese nombre ya existe",
    "msg_success_create": "Creación exitosa, actualice la lista para ver los resultados",
    "msg_success_update": "Actualización exitosa, actualice la lista para ver los resultados",
    "msg_not_valid_fields": "Hay campos no válidos"
}


FILE_RELATIVE_DIR = "../files/"
save = int(input("Guardar? (1: si, otra cosa: no) -> "))
if save == 1:
    # para protegerme de mi mismo en caso de guardar algo erroneo :v
    storeData(dictionary_es, FILE_RELATIVE_DIR + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)
    print("diccionario guardado")

