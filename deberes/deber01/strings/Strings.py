from Parameters import Parameters
from models.PickleData import loadData


class Strings:

    dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)

    @staticmethod
    def changeLanguage(language):

        if language == Parameters.language_spanish:
            Strings.dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_spanish)
        elif language == Parameters.language_english:
            Strings.dictionary = loadData(Parameters.FOLDER_FILES + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_english)
        else:
            print("Idioma no soportado, no se pudo cambiar al idioma ", language)
