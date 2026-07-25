from services.publication.webhook_publisher import WebhookPublisher


payload = {

    "product": {

        "title": "Mouse Logitech G203"

    }

}

try:

    resposta = WebhookPublisher.publish(payload)

    print(resposta)

except Exception as e:

    print(e)