# import socketio

# from .constants import *

# sio = socketio.Client()


# @sio.event
# def connect():
#     print("connection established")


# @sio.event
# def my_message(data):
#     print("message received with ", data)
#     sio.emit("my response", {"response": "my response"})


# @sio.event
# def disconnect():
#     print("disconnected from server")


# def main():
#     sio.connect(NOTIFICATION_LISTENER)
#     sio.wait()


# if __name__ == "__main__":
#     main()

import asyncio
import socketio
from .constants import *


sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("connection established")


@sio.event
async def my_message(data):
    print("message received with ", data)
    # await sio.emit("", {"response": "my response"})


@sio.on("context")
def on_message(data):
    print("I received a message! on on_message with context", str(data))


@sio.event
async def disconnect():
    print("disconnected from server")


async def main():
    await sio.connect("https://eassalnotif.herokuapp.com/")
    await sio.wait()


if __name__ == "__main__":
    asyncio.run(main())
