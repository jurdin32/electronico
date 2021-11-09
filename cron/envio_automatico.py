import os
import zeep
from electronico.settings import BASE_DIR

def envio_sri_programado():
    print("Hola soy crontab programado")
    path = os.path.join(BASE_DIR, 'media/firmado')
    for comprobante in os.listdir(path):
        nombre=comprobante.split('.')[0]
        if os.path.isfile(path+"/"+nombre+".json"):
            print('existe')
        else:
            path = os.path.join(BASE_DIR, 'media/firmado/%s.xml' % nombre)
            respuestas = os.path.join(BASE_DIR, 'media/firmado/%s.json' % nombre)
            print(path)
            comprobante = open(path, "rb")  # apertura del archivo xml
            xmlBytes = comprobante.read()  # creando mapa de bits del comprobante
            client = zeep.Client(wsdl='https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl')  # web service para envio depruebas
            print("Inicia el proceso de envio..!!")
            result = client.service.validarComprobante(xmlBytes)
            jsonarchivo = open(respuestas, "w")
            jsonarchivo.write(str(result))
            jsonarchivo.close()
            print("Respuesta: ", result)  # respuesta del servidor
            break

envio_sri_programado()