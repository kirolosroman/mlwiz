import json
from channels.generic.websocket import AsyncWebsocketConsumer
import matplotlib.pyplot as plt
import io
import base64
from asyncio import sleep

class PlotUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Update your plot with the received data
        # For example, this can be a random update just to show functionality:
        x = data.get('x', [])
        y = data.get('y', [])

        plt.figure()
        #plt.bar(x, y)
        plt.plot(x, y)
        plt.title('Live Plot Update')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        image_base64 = base64.b64encode(image_png).decode('utf-8')
        await self.send(text_data=json.dumps({
            'plot': image_base64
        }))
    async def keep_alive(self):
        while True:
            await self.send(text_data=json.dumps({'type': 'ping'}))
            await sleep(10)  # Send ping every 10 seconds
                
    def disconnect(self, close_code):
            pass


