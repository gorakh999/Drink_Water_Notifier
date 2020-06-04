import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = 'Please Drink Water Now'
        message = 'Human Body Need 3.7 litres of Water Everyday So please Drink Water to complete that level'
        app_icon = 'icon.ico'
        timeout = 10
    )
