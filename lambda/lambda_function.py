import json
import random

def lambda_handler(event, context):

    mensajes = [
        "DevOps funcionando",
        "Pipeline ejecutado",
        "Infraestructura automatizada",
        "CloudFormation activo",
        "Monitoreo habilitado"
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }
