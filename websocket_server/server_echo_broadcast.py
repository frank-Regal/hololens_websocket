#!/usr/bin/env python

# Import relevant libraries
import websockets
import asyncio

# Server Data
ADDDRESS = "localhost"
PORT = 9090 # local connection port

print("[SERVER STARTED] Listening on port: " + str(PORT))

connected = set()

# Define an async function (Main Function)
async def echo(websocket, path):
    
    connected.add(websocket)
    print("Client Connected. " + str(len(connected)) + " clients total.")
    try:
        # message comes from websocket
        async for message in websocket:
            print("Received message from client: " + message)
            # this await function makes sure that the message received is 
            # echoed back before a new message is handled
            for this_connected_ws in connected:
                if this_connected_ws != websocket:
                    await this_connected_ws.send("You got mail: " + message)      
    except websockets.exceptions.ConnectionClosed as e:
        connected.remove(websocket)
        print("Client Disconnected. " + str(len(connected)) + " clients total.")

start_server = websockets.serve(echo, ADDDRESS, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

