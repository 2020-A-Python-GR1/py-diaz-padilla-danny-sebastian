
from Parameters import Parameters  # para generar congruencia
from models.PickleData import storeData



dictionary_en = {
    "string_connected": "Connected",
    "string_disconnected": "Disconnected",
    "string_unknown": "Unknown",
    "string_yes": "Yes",
    "string_no": "No",
    "string_look_for": "Search",
    "string_search": "Search",
    "string_create": "Create",
    "string_update": "Update",
    "string_delete": "Delete",
    "string_details": "Details",
    "string_none": "None",
    "string_creation": "Creation",
    "string_id": "Id",
    "string_language": "Language",
    "string_selection": "Selection",
    "string_date": "Date",
    "string_state": "State",
    "string_active": "Active",
    "string_inactive": "Inactive",
    "string_cancel": "Cancel",
    "text_update_list": "Update list",
    "text_create_grupal_chat": "Create group chat",
    "text_manage_integrants": "Manage Members",
    "text_main_window": "MAIN WINDOW",
    "text_creation_of_integrant": "Creation of a member",
    "text_update_integrants": "Update a member",
    "text_update_groups_chat": "Update a chat group",
    "text_creation_of_chat": "Chat group creation",
    "text_is_allowed_to_talk": "You are allowed to speak",
    "text_actual_integrants": "Current members",
    "text_manage_of_chats": "Manage group of chats",
    "text_rest_of_integrants": "Remaining members",
    "text_group_name": "Group name",
    "text_dont_forget_to_update_try_again": "Dont forget to update the list, try again",
    "text_maximun_capacity": "Maximum capacity",
    "text_date_creation": "Creation date",
    "text_update_of_chat": "Chat group update",
    "text_create_integrant": "Creation of a member",
    "text_manage_of_integrants": "Member Management",
    "text_update_of_integrants": "Update a member",
    "text_user_name": "Username",
    "format_summary_chat_group":
        """DETAILS OF THE GROUP CHAT
        
        Chat id:%i
        
        Group name:%s
        
        Maximum group capacity:%i members
        
        Creation date:%s
        
        Active: %s
        
        Mean delay: %.2f
        
        Members:
        %s
        """,
    "format_id_user_integrant": "Username:%s, Id:%i \n",
    "format_summary_integrant":
        """DETAILS OF THE MEMBER
        
        Member id:%i
        Member name:%s
        joined: %s
        State: %s
        Allowed to speak:%s
        Participation score: %.2f
        """,
    "msg_error_general":
        """An error has occurred, please try again verifying that you have successfully performed the operation!""",

    "msg_search_found_and_selected": "Search found and selected",
    "msg_search_not_found": "Search not found",
    "msg_should_select_something_first_from_actual": "You should select an item from the list of actual members, first",
    "msg_should_select_something_first_from_rest": "You should select an item from the list of members that are not included, first",

    "msg_success_deleted": "Successfully removed",
    "msg_that_name_already_exists": "That name already exists",
    "msg_success_create": "Creation successful, refresh list to see results",
    "msg_success_update": "Update successful, refresh the list to see results",
    "msg_not_valid_fields": "There are invalid fields"
}


FILE_RELATIVE_DIR = "../files/"
save = int(input("Save? (1: yes, 2: no) -> "))
if save == 1:
    # para protegerme de mi mismo en caso de guardar algo erroneo :v
    storeData(dictionary_en, FILE_RELATIVE_DIR + Parameters.FOLDER_DICTIONARIES + Parameters.filename_dictionary_english)
    print("saved dictionary in english")

