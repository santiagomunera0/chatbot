from services.whatsapp import Whatsapp

class chatflow:
    def init_chatflow(number, name):
        body = f"¡Hola {name}! 👋 Soy EliBot de Palcos & Boletas. ¿Cómo podemos ayudarte hoy?"
        footer = "Equipo de Palcos & Boletas"
        options = ["Comprar entradas", "Información", "Soporte"]

        data = Whatsapp.button_reply_message(number, options, body, footer, "sedd")
        Whatsapp.send_message(data)

    def buy_tickets(number):
        body = "¡Genial! ¿Para qué evento te gustaría comprar entradas?"
        footer = "Equipo de Palcos & Boletas"
        options = ["Concierto", "Partido", "Teatro"]

        data = Whatsapp.button_reply_message(number, options, body, footer, "sedd")
        Whatsapp.send_message(data)    

def send_message(text,number, messageId, name):
    text = text.lower()
    print("mensaje del usuario: ",text)

    if "hola" in text:
        chatflow.init_chatflow(number, name)

    elif "comprar entradas" in text:
        chatflow.buy_tickets(number) 