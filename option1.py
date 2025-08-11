
import requests
import os
# Get credentials from environment variables
API_KEY = os.getenv('VONAGE_API_KEY')
API_SECRET = os.getenv('VONAGE_API_SECRET')

url = 'https://rest.nexmo.com/sms/json'

def send_sms(to_number, message):
    payload = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'to': to_number,  # Reemplaza con el número de destino
        'from': 'VonageAPI',
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == '__main__':
    number = input("Ingresa el número destino (con código de país, ej. 521234567890): ")
    text = input("Ingresa el mensaje que quieres enviar: ")
    result = send_sms(number, text)
    print("Respuesta de Vonage:", result)
