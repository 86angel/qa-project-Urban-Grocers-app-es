import requests
import configuration
import data

# CREACIÓN de un NUEVO USUARIO
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# CREACIÓN de un NUEVO KIT de usuario
def post_new_user_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

