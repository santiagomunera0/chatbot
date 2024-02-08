import requests
import sett
import json
import time

class Whatsapp:

    def get_message(message):
        if 'type' not in message :
            text = 'mensaje no reconocido'
            return text

        typeMessage = message['type']
        if typeMessage == 'text':
            text = message['text']['body']
        elif typeMessage == 'button':
            text = message['button']['text']
        elif typeMessage == 'interactive' and message['interactive']['type'] == 'list_reply':
            text = message['interactive']['list_reply']['title']
        elif typeMessage == 'interactive' and message['interactive']['type'] == 'button_reply':
            text = message['interactive']['button_reply']['title']
        else:
            text = 'mensaje no procesado'
        
        
        return text

    def send_message(data):
        try:
            whatsapp_token = sett.whatsapp_token
            whatsapp_url = sett.whatsapp_url
            headers = {'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + whatsapp_token}
            print("se envia ", data)
            response = requests.post(whatsapp_url, 
                                    headers=headers, 
                                    data=data)
            
            if response.status_code == 200:
                return 'mensaje enviado', 200
            else:
                return 'error al enviar mensaje', response.status_code
        except Exception as e:
            return e,403
        
    def text_message(number,text):
        data = json.dumps(
                {
                    "messaging_product": "whatsapp",    
                    "recipient_type": "individual",
                    "to": number,
                    "type": "text",
                    "text": {
                        "body": text
                    }
                }
        )
        return data

    def button_reply_message(number, options, body, footer, sedd):
        buttons = []
        for i, option in enumerate(options):
            buttons.append(
                {
                    "type": "reply",
                    "reply": {
                        "id": sedd + "_btn_" + str(i+1),
                        "title": option
                    }
                }
            )

        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": body
                    },
                    "footer": {
                        "text": footer
                    },
                    "action": {
                        "buttons": buttons
                    }
                }
            }
        )
        return data

    def list_reply_message(number, options, body, footer, sedd):
        rows = []
        for i, option in enumerate(options):
            rows.append(
                {
                    "id": sedd + "_row_" + str(i+1),
                    "title": option,
                    "description": ""
                }
            )

        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": body
                    },
                    "footer": {
                        "text": footer
                    },
                    "action": {
                        "button": "Ver Opciones",
                        "sections": [
                            {
                                "title": "Secciones",
                                "rows": rows
                            }
                        ]
                    }
                }
            }
        )
        return data

    def document_message(number, url, caption, filename):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "document",
                "document": {
                    "link": url,
                    "caption": caption,
                    "filename": filename
                }
            }
        )
        return data

    def sticker_message(number, sticker_id):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "sticker",
                "sticker": {
                    "id": sticker_id
                }
            }
        )
        return data

    def get_media_id(media_name , media_type):
        media_id = ""
        if media_type == "sticker":
            media_id = sett.stickers.get(media_name, None)
        #elif media_type == "image":
        #    media_id = sett.images.get(media_name, None)
        #elif media_type == "video":
        #    media_id = sett.videos.get(media_name, None)
        #elif media_type == "audio":
        #    media_id = sett.audio.get(media_name, None)
        return media_id

    def reply_reaction_message(number, messageId, emoji):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "reaction",
                "reaction": {
                    "message_id": messageId,
                    "emoji": emoji
                }
            }
        )
        return data

    def reply_text_Message(number, messageId, text):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "context": { "message_id": messageId },
                "type": "text",
                "text": {
                    "body": text
                }
            }
        )
        return data

    def mark_read_message(messageId):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id":  messageId
            }
        )
        return data