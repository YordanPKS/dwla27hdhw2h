from pyrogram import Client, filters
import yt_dlp
import os
from linea import keep_alive
keep_alive()
nombre  = {}

nombre['file']  = ""
app = Client("boti",
             api_id="29739508",
             api_hash="c2dbd1337dab67791f6635670328e8e4",
             bot_token="7208754912:AAFfd7gY5HfOJTiW35vxskoaW4RgHJAzpsk")

@app.on_message(filters.document)
def descarga(client, message):
    nombre['file']= message.document.file_name
    message.download(nombre["file"])
    print("descargando..")
@app.on_message(filters.command("descargar"))
def download_file(client, message):
    url = message.text.split()[1]
    download_folder = '/downloads/'  # Replace with your desired download folder
    ydl_opts = {
    'format_id': 'best[height<=720]',
    'outtmpl': f'{download_folder}/%(title)s.%(ext)s', # Guarda los videos en la carpeta "downloads"
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'username': 'yordanpks9@gmail.com',  # Reemplaza con tu correo electrónico
    'password': 'maikol123'  # Reemplaza con tu contraseña
    }
    app.send_message(message.chat.id,"Espere mientras se descarga su video")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        nombre_video = ydl.prepare_filename(result)
        solo_nombre = os.path.basename(nombre_video)
    print(nombre_video)
    app.send_video(message.chat.id, nombre_video, caption= solo_nombre)
    os.remove(nombre_video)

@app.on_message(filters.command("start"))
def holap(app, message):
    app.send_message(message.chat.id,"Bienvenido al bot de descargas:\n*Actualmente solo soporta:\n>YouTube.\n\nModo de uso: /descargar (y la url)")
print("Ejecutando")
app.run()
