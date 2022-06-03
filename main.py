import asyncio
import socketio
import random
import time

sio = socketio.AsyncClient()
print('Enter speed:')
speed = 100
print('Enter Temp:')
Temp = 50
print('Enter Amp:')
Amp = 10
print('Enter Volt:')
Volt = 250

@sio.event
async def connect():
    print('connection established')

@sio.event
async def message(data):
    print('message received with ', data)
    while True:
        await sio.emit('fromAPI', {"id": 1,  
        
    "speed":random.randint(0,100),

    "Temp":random.randint(0,90),

    "Amp":random.randint(0,50),

    "Volt":random.randint(0,9),
"Temprature" : random.randint(0,9), "Humidity": random.randint(0,9)})
        await sio.sleep(0)
        

@sio.on('my_message')
async def on_message(data):
    #while True:
    print('I received a message!', data)
    await sio.sleep(1)
        

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(message(data))
        asyncio.ensure_future(on_message(data))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("closing thread")
        loop.close()

if __name__ == '__main__':
    asyncio.run(main())