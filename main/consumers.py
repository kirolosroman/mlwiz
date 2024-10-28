import json
from channels.generic.websocket import AsyncWebsocketConsumer
import matplotlib.pyplot as plt
import io
import base64
from asyncio import sleep
import pickle
import pandas as pd
import numpy as np

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
        plt.xticks(rotation=90)
        plt.scatter(x, y)
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


class PlotResultConsumerHD(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)

        df=pd.read_csv("main/mlmodels/heart-disease.csv")
        X=df.drop("target",axis=1)
        x = data.get('x', [])
        y = data.get('y', [])
        input_df = pd.DataFrame([y], columns=X.columns)
        X = pd.concat([input_df,X],axis=0)
        
        load_clf = pickle.load(open('main/mlmodels/random_forest_model_heartd.pkl', 'rb'))
        prediction = load_clf.predict(X)    
        prediction_proba = load_clf.predict_proba(X)
        #print(prediction)
        label_final=prediction_proba.tolist()
        #print(label_final)
        prediction_text = 'Positive: This patient has a Heart Disease' if prediction[0] == 1 else 'Negative: This patient doesnot has a Heart Disease'
        await self.send(text_data=json.dumps({
             'label_text_negative': label_final[0][0],
             'label_text_positive': label_final[0][1],
             'prediction_text': prediction_text
        }))
        
    async def keep_alive(self):
        while True:
            await self.send(text_data=json.dumps({'type': 'ping'}))
            await sleep(10)  # Send ping every 10 seconds
                
    def disconnect(self, close_code):
            pass