"""
用myqr库制作二维码
@Date 2020.04.27
"""
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont

# 图片登录二维码， 如使用gif背景，则可以生成动态背景效果

def img_code():
    myqr.run(words='https://pbs.twimg.com/profile_images/1097995004058845184/p-M_eu3d_400x400.jpg',
            # 设置容错率为最高
            version=1,
            # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
            level='H',
            # 背景图
            picture='./语法基础/res/image/favorite.jpg',
            # 彩色二维码
            colorized=True,
            # 用以调节图片的对比度，1.0标识原始图片, 更小的值表示更低对比度，更大反之，默认为1.0
            contrast=1.0,
            # 用来调节图片的亮度, 其余用法和取值同上
            brightness=1.0,
            # 保存文件的名字，格式可以是jpg,png,bmp,gif
            save_name='QRCode1.png',
            # 保存位置
            save_dir=os.getcwd() + '/语法基础/res/image/')

def draw():
    img = Image.open('./语法基础/res/image/QRCode1.png')
    w, h = img.size
    txt = '不疯算疯子？'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./语法基础/res/font/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0,0,0), font=font)
    img.save('./语法基础/res/image/QRCode3.png')

if __name__ == '__main__':
    img_code()
    draw()