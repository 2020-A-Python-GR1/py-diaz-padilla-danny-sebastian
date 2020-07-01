import datetime
from strings.Strings import Strings as s


class ChatGroup:

    __chats_created_counter = 0  # Variable estática

    integrants = []  # de Tipo Integrant

    def __init__(self, chat_id, name_group,
                 capacity_maximun=100,
                 date_creation=str(datetime.datetime.today()).split()[0],
                 active=True,
                 delay=11.1):

        self.chat_id = chat_id  # integer
        self.name_group = name_group  # string
        self.capacity_maximun = capacity_maximun  # integer
        self.date_creation = date_creation  # string
        self.active = active  # Boolean
        self.delay = delay

        ChatGroup.__chats_created_counter += 1

    # CRUD Operations
    # create ya es el constructor
    def read(self):
        return s.dictionary['format_summary_chat_group'] % \
               (self.chat_id, self.name_group, self.capacity_maximun,
                self.date_creation,
                s.dictionary['string_yes'] if self.active else s.dictionary['string_no'])

    def update_chat_id(self, new_chat_id):
        self.chat_id = new_chat_id  # integer

    def update_name_group(self, new_name_group):
        self.name_group = new_name_group  # string

    def update_capacity_maximun(self, new_capacity_maximun):
        self.capacity_maximun = new_capacity_maximun  # integer

    def update_date_creation(self, new_date_creation):
        self.date_creation = new_date_creation  # string

    def update_state_active(self, new_state_active):
        self.active = new_state_active  # Boolean

    # Delete se hace desde ejecución

    # Operaciones sobre la lista

    def add_integrant(self, integrant):
        self.integrants.append(integrant)

    def remove_integrant(self, integrant):
        self.integrants.remove(integrant)

    @staticmethod
    def generateNewId():
        print("Id nuevo generado para un chat grupal")
        return ChatGroup.__chats_created_counter + 1
