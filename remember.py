import time
import os
import subprocess
import datetime

# path del file
path = "./remember.txt"

# funzione per aprire il file
def open_file():
    try :
        # se il file non esiste, lo crea
        if not os.path.exists(path):
            with open(path, "w") as file:
                file.write("Ciao\n\nRicordati di fare qualcosa di bello oggi!\n\nTipo:  PAGA LE TASSE UNIVERSITARIE!")
        else:
            with open(path, "r") as file:
                print(file.read())
                subprocess.run(["open", path])
    except FileNotFoundError:
        print("File not found")



# funzione per controllare l'ora
# se è le 10:00, apre il file
# altrimenti, aspetta 1 minuto e controlla di nuovo
def check_time():

    while True:
        current_time = time.localtime()
        print(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
        if current_time.tm_hour == 10 and current_time.tm_min == 30:
            open_file()
            break
        else:
            time.sleep(60)
check_time()
