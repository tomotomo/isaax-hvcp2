#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from flask import Flask, render_template, Response
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(path):
    while True:
        frame = path
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen('img.jpg'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print('import success')
    app.run(host='0.0.0.0', debug=False, threaded=True)
    main()
