from pyrogram import Client, filters
import yt_dlp
import os
import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
import instaloader
from linea import keep_alive
keep_alive()
nombre  = {}
calidad = {}
calidad['resolucion'] =  ''
nombre['file']  = ""
app = Client("boti",
             api_id="29739508",
             api_hash="c2dbd1337dab67791f6635670328e8e4",
             bot_token="7208754912:AAGUIaYdy1vKHlDiSpxUGJQS1lZkIDwuOMA")
@app.on_message(filters.command("start"))
def holap(app, message):
    app.send_message(message.chat.id,"Bienvenido al bot de descargas:\n*Actualmente solo soporta:\n>YouTube\n*Instagram.\n\nModo de uso:\nEnvie la URL al bot y listo\n\nDesarrollado por @Yordan_PKS")


@app.on_message(filters.text)
def download_video_insta(client, message):
    if message.text.startswith('/'):
        return
    url = re.search(r'https?://\S+', message.text).group(0)
    if "instagram.com" in url:
      
     app.send_message(message.chat.id, "Su video está siendo procesado, por favor espere. En caso de pasar más de un minuto, vuelva a intentarlo.") 
    
     loader = instaloader.Instaloader()
    
     # Aquí puedes cargar tu sesión de cookies
     try:
         loader.load_session_from_file('yordan09prueba', filename='seccion/seccion_nueva')  # Reemplaza "tu_usuario" con tu nombre de usuario
     except FileNotFoundError:
         app.send_message(message.chat.id, "No se encontró la sesión. Asegúrate de haber iniciado sesión previamente.")
         return

     shortcode = url.split('/')[-2] 
     post = instaloader.Post.from_shortcode(loader.context, shortcode) 
     loader.download_post(post, target='ab')  # Se descarga en el directorio actual 
    
     filename = f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_UTC.mp4" 
     Titulo = f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_UTC.txt" 

     with open(f"ab/{Titulo}", 'r', encoding='utf-8') as file: 
         contenido = file.read() 

     nombre_archivo = filename 
     app.send_video(message.chat.id, f"ab/{nombre_archivo}", caption=contenido) 
     print("enviando")
     #youtube
    elif "youtube.com" in url or "youtu.be" in url:
        download_folder = 'downloads'  # Replace with your desired download folder
        ydl_opts = {
            'format': 'best[height<=480]',
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s', # Guarda los videos en la carpeta "downloads"
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
         }],
         'cookiefile': 'cookies.txt'
     }
        print(ydl_opts["format"])
        app.send_message(message.chat.id,"Espere mientras su video es procesado\nEsto puede tardar varios segundos")
        limite_tamano = 2 * 1024 * 1024 * 1024
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
            nombre_video = ydl.prepare_filename(result)
            solo_nombre = os.path.basename(nombre_video)
         # Verifica el tamaño del archivo 
            tamano_archivo = os.path.getsize(nombre_video)  # Tamaño en bytes 
        if tamano_archivo > limite_tamano: 
            limite_tamano = 2 * 1024 * 1024 * 1024  # Límite de 2 GB 
            os.remove(nombre_video)  # Elimina el archivo si excede el límite 
            print(f"El archivo {nombre_video} ha sido eliminado porque excede el límite de {limite_tamano / (1024 * 1024 * 1024):.2f} GB.")
            app.send_message(message.chat.id,"Su video sobrepasa los 2GB, porfavor pruebe en otra resolucion")
        else:  
# Ejemplo de uso 
            limite_tamano = 2 * 1024 * 1024 * 1024  # Límite de 2 GB 
            print(nombre_video)
            app.send_video(message.chat.id, nombre_video, caption= solo_nombre)
            os.remove(nombre_video)
    else:
        app.send_message(message.chat.id,"La URL enviada no pertenece a ninguna de las plataformas soportadas")

Botones = [
    [
        InlineKeyboardButton("Menor de 720p", callback_data="720p"),
        InlineKeyboardButton("Menor de 480p", callback_data="480p"),
        InlineKeyboardButton("Menor de 360p", callback_data="360p"),
    ],
    [
        InlineKeyboardButton("Mayor calidad", callback_data="mayor")
    ]   
]
@app.on_message(filters.command("calidad"))
def holap(app, message):
    message.reply("En el siguiente menu seleccione la calidad que desea\nRecuerde que puedes saber la calidad usada desde /ver", reply_markup = InlineKeyboardMarkup(Botones))
@app.on_callback_query()
def cambiar_calidad(Client, CallbackQuery):
    if CallbackQuery.data == "720p":
        calidad["resolucion"] =  'best[height<=720]'
        CallbackQuery.edit_message_text("Calidad cambiada a 720p")
    elif CallbackQuery.data == "480p":
        calidad["resolucion"] =  'best[height<=480]'
        CallbackQuery.edit_message_text("Calidad cambiada a 480p")
    elif CallbackQuery.data == "360p":
        calidad["resolucion"] =  'best[height<=360]'
        CallbackQuery.edit_message_text("Calidad cambiada a 360p")
    elif CallbackQuery.data == "mayor":
        calidad["resolucion"] =  'best'
        CallbackQuery.edit_message_text("Calidad cambiada a la mayor")
@app.on_message(filters.command("ver"))
def holap(app, message):
    if calidad['resolucion'] == 'best[height<=720]':
        app.send_message(message.chat.id, f"La calidad actual es 720p")
    elif calidad['resolucion'] == 'best[height<=480]':
        app.send_message(message.chat.id, f"La calidad actual es 480p")
    elif calidad['resolucion'] == 'best[height<=360]':
        app.send_message(message.chat.id, f"La calidad actual es 360p")
    elif calidad['resolucion'] == 'best':
        app.send_message(message.chat.id, f"La calidad actual es la mayor posible")
print("Ejecutando")
app.run()
