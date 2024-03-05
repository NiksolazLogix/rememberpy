# istruzioni per l'installazione

- Apri il Terminale.
- Esegui il seguente comando:

```
  nano ~/.bash_profile
```

- Incolla il seguente codice alla fine del file, sostituendo path/to/remember.py con il percorso effettivo dello script:

```
  if [ -f ~/.bash_profile ]; then
    source ~/.bash_profile
  fi

  /usr/bin/python3 /path/to/remember.py
```

- Salva il file

```
.bash_profile
```

- Esci e riaccedi al tuo account utente

# ricordati di avere i permessi!
