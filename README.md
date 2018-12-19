## 公式README

[ReadMe_J.txt](./ReadMe_J.txt)を読むこと。

    [ご使用にあたって]
    ・本サンプルコードおよびドキュメントの著作権はオムロンに帰属します。
    ・本サンプルコードは動作を保証するものではありません。
    ・本サンプルコードは、Apache License 2.0にて提供しています。

このサンプルコードは、Apache License 2.0の範囲内で使用しています。

## python環境の準備

python 2系

僕の環境ではpipコマンドはpython3にバインドされてた

```bash
pip2 install pyserial
pip2 install pillow
```

### 実行

```bash
cd lib
python execution.py /dev/tty.usbmodem11 921600 OFF
```

### デモ作るよ

```bash
pip2 install flask
```

インタラクティブにテスト

```pyton
import sys
import time
import lib.p2def as p2def
from lib.serial_connector import SerialConnector
from lib.hvc_p2_api import HVCP2Api
exec_func = p2def.EX_FACE\
          | p2def.EX_DIRECTION\
          | p2def.EX_AGE\
          | p2def.EX_GENDER\
          | p2def.EX_EXPRESSION\
          | p2def.EX_HAND
connector = SerialConnector()
hvc_p2_api = HVCP2Api(connector, exec_func, p2def.USE_STB_OFF)

output_img_type = p2def.OUT_IMG_TYPE_QVGA
hvc_camera_angle = p2def.HVC_CAM_ANGLE_0
portinfo = '/dev/tty.usbmodem11'
baudrate = 921600
hvc_p2_api.connect(portinfo, p2def.DEFAULT_BAUD, 10)
hvc_p2_api.set_uart_baudrate(baudrate)
hvc_p2_api.disconnect()
```