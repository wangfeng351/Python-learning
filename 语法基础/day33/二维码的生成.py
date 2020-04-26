"""
二维码
@Date 2020.04.05
"""
import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=8, border=4)
qr.add_data('Hello World')
img = qr.make_image()
img.save('./语法基础/res/image/code.png')

qr.add_data('https://www.baidu.com')
img1 = qr.make_image(fill_color='rgb(250,130,70)',
                     back_color='rgb(190,120,160)')
img1.save('./语法基础/res/image/code1.png')