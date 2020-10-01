import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = 'Its time to drink Water'
        message = 'Human Body Need 3.7 litres of Water Everyday So please Drink Water to complete that level'
        app_icon = 'icon.ico'
        timeout = 10
    )
