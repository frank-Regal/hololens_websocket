#!/usr/bin/env python

# Import relevant libraries
import websockets
import asyncio
import json

# Server Data
ADDDRESS = "192.168.1.9"
PORT = 9090

# Terminal printout
print("[SERVER STARTED] Listening on port: " + str(PORT))

# Create a set of connected clients for multi-client broadcasting
connected = set()

# Define an asyncronous listener
async def listen(websocket, path):
    connected.add(websocket)
    print("Client Connected. " + str(len(connected)) + " clients total.")
    try:
        async for message in websocket:
            msg_type = type(message)
            if msg_type == bytes:
                json_message = json.loads(message)
                print("JSON message received: " + str(json_message))
            else:
                print("Received message from client: " + str(message))
            #await websocket.send("Pong: " + message) # send back a message to client
    except websockets.exceptions.ConnectionClosed as e:
        connected.remove(websocket)
        print("Client Disconnected. " + str(len(connected)) + " clients total.")

# Declare a server variable
start_server = websockets.serve(listen, ADDDRESS, PORT)

# Start the server & and run until closed
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()