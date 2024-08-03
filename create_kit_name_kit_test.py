#Imports
import sender_stand_request
import data

#Funciones
def get_user_body(first_name):
    user_body = data.user_body.copy()
    user_body["firstName"] = first_name
    return user_body

def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]

def get_kit_body(name):
    kit_body = {"name": name}
    return kit_body

def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body, auth_token)

def test_create_kit_special_caracter_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("№%@',")
    positive_assert(kit_body, auth_token)

def test_create_kit_0_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_numbers_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_spaces_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("A aaa")
    positive_assert(kit_body, auth_token)

def test_create_kit_no_parameter_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = {} 
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_type_number_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body(123)
    negative_assert_code_400(auth_token, kit_body)
