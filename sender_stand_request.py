import requests
import configuration


# CREACIÓN de un NUEVO USUARIO
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body)

# CREACIÓN de un NUEVO KIT de usuario
def post_new_user_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

# OBTENER lista de USUARIO EXISTENTES
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PAT
