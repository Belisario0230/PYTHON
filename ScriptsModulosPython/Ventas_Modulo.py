import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Reemplaza estos valores con tus propios valores
gmail_usuario = 'bbltrabajo@gmail.com'
gmail_contraseña = '97446691beli'
destinatario = 'buitragolievanob3002@hotmail.com'
asunto = 'Correo de prueba'
cuerpo = 'Este es un correo de prueba enviado utilizando Python.'

# Configura las credenciales de OAuth 2.0
SCOPES = ['https://mail.google.com/']
ARCHIVO_DE_CUENTA_DE_SERVICIO = 'ruta/a/tu/archivo_de_cuenta_de_servicio.json'

credenciales = service_account.Credentials.from_service_account_file(
    ARCHIVO_DE_CUENTA_DE_SERVICIO, scopes=SCOPES)

# Configura el cliente de la API de Gmail
servicio_de_gmail = build('gmail', 'v1', credentials=credenciales)

# Crea el mensaje
msg = MIMEMultipart()
msg['From'] = gmail_usuario
msg['To'] = destinatario
msg['Subject'] = asunto
msg.attach(MIMEText(cuerpo, 'plain'))

# Envía el correo
mensaje_raw = base64.urlsafe_b64encode(msg.as_bytes())
mensaje_raw = mensaje_raw.decode()

servicio_de_gmail.users().messages().send(userId='me', body={'raw': mensaje_raw}).execute()