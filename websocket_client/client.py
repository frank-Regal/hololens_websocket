#!/usr/bin/env python

# importing the relevant libraries
import websockets # 
import asyncio    # this is a standard python package for async logic

# main function that will handle connuection and communication
# Listener for websocket
async def listen():
    url = "ws://192.168.1.9:9090" # address of the websocket server 

    try:
        # connect to server
        async with websockets.connect(url) as ws:
            await ws.send("Hello world")
            while True:
                msg = await ws.recv() # makes async request to execute before assigning value to websocket variable
                print(msg)
    except:
        print("something went wrong.")

# start the connection
asyncio.get_event_loop().run_until_complete(listen())
