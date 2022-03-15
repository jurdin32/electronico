#enviar correo por:
from email import encoders
from email.mime.base import MIMEBase
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import  formatdate
import smtplib



datos_email={
    'servidor_smtp':'mail.elguabo.gob.ec',
    'puerto':587,
    'use_tls':True,
    'usuario':'facturacion@elguabo.gob.ec',
    'password':'Facturas*2020',
}

def enviarEmail(destinatarios=[], asunto="", mensaje="", archivos=[], is_html=False):
    msg = MIMEMultipart()
    msg['From'] = datos_email['usuario']
    msg['To'] = ", ".join(destinatarios)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = asunto
    try:
        if is_html:
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(mensaje)
            print("[1] Se marco como contenido en html..!")
        else:
            print("[1] No tiene contenido html..!")
            msg.attach(MIMEText(mensaje))
        if archivos:
            print("[2] Tiene datos adjuntos")
            for path in archivos:
                part = MIMEBase('application', "octet-stream")
                with open(path, 'rb') as file:
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(Path(path).name))
                    msg.attach(part)
        else:
            print("[2] No tiene datos adjuntos..!")

        smtp = smtplib.SMTP(datos_email['servidor_smtp'], datos_email['puerto'])
        print("[3] Paso lo validación se cargo usuario y contraseña y puerto de configuración")
        if datos_email['use_tls']:
            smtp.starttls()
            print("[4] Se marco como seguro..!")
        else:
            print("[4] No se envia como seguro..!")
        smtp.login(datos_email['usuario'], datos_email['password'])
        print("[5] Login Exitoso..!")
        smtp.sendmail(datos_email['usuario'],destinatarios, msg.as_string())
        print("[6] Envio del texto..!")
        smtp.quit()
        print("[7] Mensaje enviado exitosamente..!")
    except Exception as error:
        print("[x] Error General: %s"%error)

enviarEmail(['urdin-23@live.com',],"Mensaje de Prueba","Hola que tal como estamos",['D:\\Documentos\\bit.png'])