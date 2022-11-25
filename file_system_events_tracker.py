import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Kaiowa/Downloads"
to_dir = "C:/Byjus/Arquivos_Documentos"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hello, {event.src_path} was created!")
    def on_deleted(self, event):
        print(f"oh! someone deleted {event.src_path}")


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(5)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()