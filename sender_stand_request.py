import requests
import data
import configuration

#Creacion de nuevo usuario usando metodo post
def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)
    print("User creation status code:", response.status_code)
    print("User creation response:", response.json())
    return response.json().get("authToken")

# Usuario nuevo creado y token
auth_token = post_new_user(data.user_body)

# Headers con actualizados con los requisitos de la API 
headers_with_auth = data.headers.copy() # Usando el header primario
headers_with_auth["Authorization"] = f"Bearer {auth_token}" #actualizando al header secundario

#Creacion de un kit unico con token autorizado
def post_personal_kit(auth_token):
    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=data.kitBody,
        headers=headers_with_auth
    )
    print("Personal kit creation status code:", response.status_code)
    return response
kit_response = post_personal_kit(auth_token)
print("Personal kit creation response:", kit_response.json())

def post_new_client_kit(kit_body, auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers_with_auth
    )
    print("Client kit creation status code:", response.status_code)
    return response

# Create client kit for the new user
client_kit_response = post_new_client_kit(data.kitBody, auth_token)
print("Client kit creation response:", client_kit_response.json())









