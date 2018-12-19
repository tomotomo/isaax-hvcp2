import os
from datetime import datetime
import time
import ambient
import requests

class AmbientConnector():
    def __init__(self):
        self.am = ambient.Ambient(os.environ['AM_CHANNEL_ID'], os.environ['AM_WRITE_KEY'])
        self.datas = []
        self.last_posted_at = datetime.now()

    def buffer(self, faces):
        happiness = 0
        anger = 0
        neg_pos = 0
        for i, face in enumerate(faces):
            '''
            class ExpressionResult
            '''
            (exp, score) = face.expression.get_top1()
            happiness = face.expression.happiness
            anger = face.expression.anger
            neg_pos = face.expression.neg_pos
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {'created': now, 'd1': happiness, 'd2': len(faces), 'd3': anger, 'd4': neg_pos}
        self.datas.append(data)

        if (datetime.now() - self.last_posted_at).seconds > 15:
            self.send()
        return data
    
    def send(self):
        r = self.am.send(self.datas)
        if (r.status_code == 200):
            self.datas = []
            self.last_posted_at = datetime.now()
            print('Ambient send successful')
        else:
            print('Ambient send error')