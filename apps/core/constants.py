import os

env = os.environ.get("ENV")

if env == "development":
    NOTIFICATION_PUSH_END = "http://localhost:7777/notify/"
    NOTIFICATION_LISTENER = "http://localhost:7777/"

else:
    NOTIFICATION_PUSH_END = "https://eassalnotif.herokuapp.com//notify/"
    NOTIFICATION_LISTENER = "https://eassalnotif.herokuapp.com/"
