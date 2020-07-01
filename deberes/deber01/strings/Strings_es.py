from Parameters import Parameters  # para generar congruencia
from models.PickleData import storeData



# Ejecutar cada vez que se agregue una palabra al diccionario.

dictionary_es = {
    "string_connected": "Conectado",
    "string_disconnected": "Desconectado",
    "string_unknown": "Desconocido",
    "string_yes": "Si",
    "string_no": "No",
    "string_search": "Buscar",
    "string_create": "Crear",
    "string_update": "Actualizar",
    "string_delete": "Delete",
    "string_details": "Detalles",
    "text_create_grupal_chat": "Crear chat grupal",
    "text_manage_integrants": "Administrar Integrantes",
    "format_summary_chat_group":
        """
        Chat id: %i
        Nombre del grupo: %s
        Capacidad máxima del grupo: %i integrantes
        Fecha de creación: %s
        Activo: %s
        """,
    "format_summary_integrant":
        """
        Id del integrante: %i
        Nombre del integrante: %s
        Se unió el %s
        Estado: %s
        Se le permite hablar: %s
        """,
    "msg_error_general":
        """¡Ha ocurrido un error, inténtelo de nuevo verificando que haya hecho correctamente la operación!"""

}


FILE_RELATIVE_DIR = "../files/"
save = int(input("Guardar? (1: si, otra cosa: no) -> "))
if save == 1:
    # para protegerme de mi mismo en caso de guardar algo erroneo :v
    storeData(dictionary_es, FILE_RELATIVE_DIR + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)
    print("diccionario guardado")

