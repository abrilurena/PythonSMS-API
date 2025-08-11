import vonage
import vonage_sms


# Autenticación usando el constructor correcto del SDK actual
auth = vonage.Auth(api_key="XX", api_secret="X")
client = vonage.Vonage(auth)

# Crear el mensaje SMS
message = vonage_sms.SmsMessage(
    to="XXXXXXXXXXX",  # Reemplaza con el número de destino
    from_="Vonage APIs",
    text="A text message sent using the Nexmo SMS API",
)

# Enviar el SMS
try:
    response = client.sms.send(message)
    print("Message sent successfully.")
    print(response)
except Exception as e:
    print(f"Message failed with error: {e}")