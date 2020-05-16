""" class .ext where have a updater method - see doc"""
from telegram.ext import Updater, CommandHandler

def main():
    """ open("./bot_token").read(), use_context=True -> Si queremos import un archivo externo. """
    updater = Updater(token="nameToken")

    """ 
        CommandHandler: Manejador de commandos.
        Reaccionando al comando /start
        disaptcher : recibir actualizaciones del update y dice a los manejadores que tienen que hacer.
        handler: responde y reaccionan al los commandos de telegram.
    """
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    updater.disaptcher.add_handler(CommandHandler("suma", suma))

    """ Empezamos a pedir notificaciones a Telegram"""
    updater.start_polling()
    """ Si alguien quiere cerrar, va a avisar al bot que acabe sus tareas antes de cerrarse.
        Captura en resumen una señal de parada.
    """
    updater.idle()

""" Funcion para el manejador """
def start(update, context):
    update.message.reply_text("Hola, soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args = [2, 2] 
    result = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("The result is " + str(result))

main()
