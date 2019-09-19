__author__ = 'keith'

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size=20)
    fontColor = '#ff0000'
    width, height = img.size
    draw.text((width - 20,0), '7', font=myfont, fill=fontColor)
    # 文件名， 格式
    img.save('result.jpg', 'jpeg')
    return 0


if __name__ == "__main__":
    # image = Image.open('image.jpg')
    image = Image.open('image.jpg')

    add_num(image)