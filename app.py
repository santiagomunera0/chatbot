from services.whatsapp import Whatsapp
from chat.chatflow import send_message
from config import whatsapp
from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def hello_world():
    return 'Hola Mundo!'

@app.route('/wa/webhook', methods=['GET'])
def wa_verify_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == whatsapp.token and challenge != None:
            print('token correcto')
            return challenge
        else:
            return 'token incorrecto', 403
    except Exception as e:
        return e,403
    
@app.route('/wa/webhook', methods=['POST'])
def wa_webhook():
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = message['from']
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = Whatsapp.get_message(message)

        send_message(text, number, messageId, name)
        return 'enviado'

    except Exception as e:
        return 'no enviado ' + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
