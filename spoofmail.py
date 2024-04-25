import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP y credenciales
smtp_server = 'tu_servidor_smtp'
port = 587  # Puerto para TLS
sender_email = 'tu_correo@gmail.com'  # Remitente
receiver_email = 'destinatario@example.com'  # Destinatario
password = 'tu_contraseña'

# Crear el objeto del mensaje
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Asunto del correo'

# Cuerpo del mensaje
body = 'Hola,\n\nEste es un correo de prueba enviado desde Python.'
message.attach(MIMEText(body, 'plain'))

# Establecer la conexión con el servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Habilitar seguridad TLS
    # Iniciar sesión en el servidor SMTP y enviar el correo
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Correo enviado correctamente!')
except Exception as e:
    print('Error al enviar el correo:', str(e))
finally:
    # Cerrar la conexión con el servidor SMTP
    server.quit()