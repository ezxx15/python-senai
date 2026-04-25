# Autor: Enzo 
# projeto sistema para
# download de videos do youtube

# import dos recursos da biblioteca
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input('Digite a url do vídeo: ')
yt = YouTube(url,on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print("baixando vídeo")
ys.download()
print("Download concluído com sucesso")