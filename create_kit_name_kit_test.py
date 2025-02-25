import sender_stand_request
import data

# Cambio en el parametro "name" en el kit
def get_kit_body(name_kit):
    current_body = data.kitBody.copy()
    current_body["name"] = name_kit
    return current_body

# Pruebas positivas
def positive_assert(name_kit):
    kit_body = get_kit_body(name_kit)
    positive_kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token=() )
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()["name"] == name_kit

# Pruebas negativas
def negative_assert(name_kit):
    kit_body = get_kit_body(name_kit)
    negative_kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token=())
    assert negative_kit_response.status_code == 400
    assert negative_kit_response.json()["name"] 
    
    
#Prueba 1, numero de caracteres permitidos (1)
def test_create_user_kit_1_letter_success_response():
    positive_assert("a")        
#Prueba 2, numero de 511 caracteres permitido 
def test_create_user_kit_511_letters_success_response():   
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#Prueba 3, numero de caracteres menor que la permitida    
def test_create_user_kit_empty_get_error_response():
    negative_assert("")   
#Prueba 4,  número de caracteres es mayor que la cantidad permitida 
def test_create_user_kit_512_letters_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5, caracteres especiales permitido
def test_create_user_kit_special_char_succes_response():
    positive_assert("%$&*")
    
#Prueba 6, se permiten espacios en el campo "name"
def test_create_user_kit_spaces_between_char_succes_response():
    positive_assert(" A Aaa ")
    
#Prueba 7, se permiten numeros en el campo "name"
def test_create_user_kit_numers_succes_response():
    positive_assert("123")   
    
def negative_assert_no_name(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token=auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 8, anulando el campo de "name" en la solicitud
def test_create_user_kit_with_no_name_key_get_error_response():
    kit_body = data.kitBody.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body, auth_token=())

# Prueba 9, con un integer en el campo name (tipo de parametro diferente)
def test_create_user_kit_with_number_type_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token=())
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()