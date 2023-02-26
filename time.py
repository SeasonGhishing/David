from David import say
import datetime
def now_time():
    hour = int(datetime.datetime.now().hour)
    minutes = int(datetime.datetime.now().minute)
    say(f"its {hour} {minutes} right now!")