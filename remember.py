"""
creare uno script che ogni mattina alle 10:00 apre un file di testo txt e mi mostri il contenuto
"""

import time
import os

# path del file
path = "./remember.txt"

# funzione per aprire il file
def open_file():
    try :
        # se il file non esiste, lo crea
        if not os.path.exists(path):
            with open(path, "w") as file:
                file.write("hello world")
        else:
            with open(path, "r") as file:
                print(file.read())
    except FileNotFoundError:
        print("File not found")



# funzione per controllare l'ora
# se è le 10:00, apre il file
# altrimenti, aspetta 1 minuto e controlla di nuovo
def check_time():

    while True:
        current_time = time.localtime()
        if current_time.tm_hour == 9 and current_time.tm_min == 7:
            open_file()
            break
        else:
            time.sleep(60)
check_time()
