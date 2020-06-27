from Parameters import Parameters  # para generar congruencia
from strings.Strings import Strings as s


class Integrant:

    __integrants_created_counter = 0

    states = {
        Parameters.key_state_connected: 1,
        Parameters.key_state_disconnected: 2
    }

    def __init__(self, user_id, user_name, state, date_creation, allowed_to_talk):
        self.user_id = user_id  # integer
        self.user_name = user_name  # string
        self.date_creation = date_creation  # string
        self.state = state  # Integer. Definido en el diccionario de arriba
        self.allowed_to_talk = allowed_to_talk  # Boolean

        Integrant.__integrants_created_counter += 1

    # Operaciones CRUD
    # Create es el constructor
    def read(self):
        return s.dictionary['format_summary_integrant'] % \
               (self.user_id, self.user_name, self.date_creation,
                self.readStateInWords(),
                s.dictionary['string_yes'] if self.allowed_to_talk else s.dictionary['string_no'])

    def readStateInWords(self):
        if self.state == 1:
            return s.dictionary['string_connected']
        elif self.state == 2:
            return s.dictionary['string_disconnected']
        else:
            return s.dictionary['string_unknown']

    def update_user_id(self, new_user_id):
        self.user_id = new_user_id  # integer

    def update_user_name(self, new_user_name):
        self.user_name = new_user_name  # string

    def update_new_date_creation(self, new_date_creation):
        self.date_creation = new_date_creation  # string

    def update_state(self, new_state):
        self.state = new_state  # Definido en el diccionario de arriba. Number

    def update_allowed_to_talk(self, new_allowed_to_talk):
        self.allowed_to_talk = new_allowed_to_talk  # Boolean

    # Delete se hace desde ejecución
    @staticmethod
    def generateNewId():
        return Integrant.__integrants_created_counter + 1
