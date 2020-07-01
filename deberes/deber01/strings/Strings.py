from Parameters import Parameters
from models.PickleData import loadData


class Strings:

    dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)
    actual_language = "Español"

    @staticmethod
    def changeLanguage(language):

        if language == Parameters.language_spanish:
            Strings.dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)
            Strings.actual_language = "Español"
        elif language == Parameters.language_english:
            Strings.dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_english)
            Strings.actual_language = "English"
        else:
            print("Idioma no soportado, no se pudo cambiar al idioma ", language)


