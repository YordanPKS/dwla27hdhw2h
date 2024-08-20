from pyrogram import Client, filters
import yt_dlp
import os
import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
import instaloader
import time
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
    app.send_message(message.chat.id,"Bienvenido al bot de descargas:\n*Actualmente solo soporta:\n>YouTube\n>Instagram.\n>Facebook\n>Pinterest\n\nModo de uso:\nEnvie la URL al bot y listo\n\nDesarrollado por @Yordan_PKS")


@app.on_message(filters.text)
def download_video_insta(client, message):
    if message.text.startswith('/'):
        return
    url = re.search(r'https?://\S+', message.text).group(0)
    if "instagram.com" in url:
      
     instameg = app.send_message(message.chat.id, """
                      𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔10℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖☻   ❘
❘________❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""") 
     time.sleep(2)
     loader = instaloader.Instaloader()
     app.edit_message_text(message.chat.id, instameg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔40℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙿𝚛𝚎𝚙𝚊𝚛𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
     time.sleep(2)
     # Aquí puedes cargar tu sesión de cookies
     try:
         loader.load_session_from_file('yordan09prueba', filename='seccion/seccion_nueva')  # Reemplaza "tu_usuario" con tu nombre de usuario
     except FileNotFoundError:
         app.send_message(message.chat.id, "No se encontró la sesión. Asegúrate de haber iniciado sesión previamente.")
         return
     app.edit_message_text(message.chat.id, instameg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔80℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙳𝚎𝚜𝚌𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
     shortcode = url.split('/')[-2] 
     post = instaloader.Post.from_shortcode(loader.context, shortcode) 
     loader.download_post(post, target='ab')  # Se descarga en el directorio actual 
    
     filename = f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_UTC.mp4" 
     Titulo = f"{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_UTC.txt" 

     with open(f"ab/{Titulo}", 'r', encoding='utf-8') as file: 
         contenido = file.read() 
     app.edit_message_text(message.chat.id, instameg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔99℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙴𝚗𝚟𝚒𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
     nombre_archivo = filename 
     app.send_video(message.chat.id, f"ab/{nombre_archivo}", caption=contenido)
     app.edit_message_text(message.chat.id, instameg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔➔100℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
     print("enviando")
     #youtube
     #youtube
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
        ytmeg = app.send_message(message.chat.id, """
                      𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔10℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Youtube☻   ❘
❘________❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""") 
        time.sleep(3)
        app.edit_message_text(message.chat.id, ytmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔40℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙿𝚛𝚎𝚙𝚊𝚛𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Youtube☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        time.sleep(2) 

        limite_tamano = 2 * 1024 * 1024 * 1024
        app.edit_message_text(message.chat.id, ytmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔80℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙳𝚎𝚜𝚌𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Youtube☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
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
            app.edit_message_text(message.chat.id, ytmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔99℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙴𝚗𝚟𝚒𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Youtube☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
            app.send_video(message.chat.id, nombre_video, caption= solo_nombre)
            app.edit_message_text(message.chat.id, ytmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔➔100℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Youtube☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
            os.remove(nombre_video)

        #FACEBOOK 
        #FACEBOOK    
    elif "facebook.com" in url:
        download_folder = 'Downloads'
        facmeg = app.send_message(message.chat.id, """
                      𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔10℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Facebook☻   ❘
❘________❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""") 
        time.sleep(3)
        archivo_cookies = "www.facebook.com_cookies.txt"
        app.edit_message_text(message.chat.id, facmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔40℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙿𝚛𝚎𝚙𝚊𝚛𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Facebook☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        time.sleep(2) 
        opciones = {
            'format': 'best',
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Nombre del archivo
            'cookiefile': archivo_cookies,    # Ruta al archivo de cookies
            }
        app.edit_message_text(message.chat.id, facmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔80℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙳𝚎𝚜𝚌𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Facebook☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            resul = ydl.extract_info(url, download=True)
            nombre_vide = ydl.prepare_filename(resul)
            solo_nombr = os.path.basename(nombre_vide)
            print(nombre_vide)
        app.edit_message_text(message.chat.id, facmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔99℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙴𝚗𝚟𝚒𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Facebook☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        app.send_video(message.chat.id, nombre_vide, caption= solo_nombr)
        app.edit_message_text(message.chat.id, facmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔➔100℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Facebook☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        os.remove(nombre_vide)



    elif "pinterest.com" in url:
        pmeg = app.send_message(message.chat.id, """
                      𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔10℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Pinterest☻   ❘
❘________❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""") 
        time.sleep(3)
        download_folder = 'Downloads'
        app.edit_message_text(message.chat.id, pmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔40℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙿𝚛𝚎𝚙𝚊𝚛𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Pinterest☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        time.sleep(2)
        opciones = {
        'format': 'best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Nombre del archivo
        'cookiefile': archivo_cookies,    # Ruta al archivo de cookies
        }
        archivo_cookies = 'www.pinterest.com_cookies.txt'
        app.edit_message_text(message.chat.id, pmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔80℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙳𝚎𝚜𝚌𝚊𝚛𝚐𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Pinterest☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            resulta = ydl.extract_info(url, download=True)
            nombre_videos = ydl.prepare_filename(resulta)
            solo_nombres = os.path.basename(nombre_videos)
        app.edit_message_text(message.chat.id, pmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔99℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙴𝚗𝚟𝚒𝚊𝚗𝚍𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Pinterest☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        app.send_video(message.chat.id, nombre_videos, caption= solo_nombres)
        app.edit_message_text(message.chat.id, pmeg.id, """𝕊𝕦 𝕥𝕒𝕣𝕖𝕒 𝕖𝕤𝕥𝕒 𝕤𝕚𝕖𝕟𝕕𝕠 𝕡𝕣𝕠𝕔𝕖𝕤𝕒𝕕𝕒!
   [➔➔➔➔➔➔➔➔100℅]
❘𝙴𝚜𝚝𝚊𝚍𝚘: 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚘!⇍ ❘
❘𝚃𝚒𝚙𝚘: #Pinterest☻   ❘
❘____❘

𝚈𝚘𝚛𝚍𝚊𝚗𝙿𝙺𝚂!Ⓡ""")
        os.remove(nombre_videos)
        
    else:
        app.send_message(message.chat.id,"La URL enviada no pertenece a ninguna de las plataformas soportadas")

print("Ejecutando")
app.run()
