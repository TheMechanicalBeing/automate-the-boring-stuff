from PIL import Image, ImageDraw, ImageFont


if __name__ == '__main__':
    with open('guests.txt') as f:
        for index, line in enumerate(f):
            guest = line.strip()
            image_object = Image.new('RGBA', (288, 360), 'white')

            draw = ImageDraw.Draw(image_object)
            draw.text((35, 130), guest, fill='crimson', font=ImageFont.truetype('arial.ttf', 40))
            draw.rectangle((0, 0, 288, 75), fill='pink', outline='purple')
            draw.rectangle((0, 285, 288, 360), fill='pink', outline='purple')
            draw.rectangle((0, 0, 30, 360), fill='purple', outline='purple')
            draw.rectangle((258, 0, 288, 360), fill='purple', outline='purple')

            image_object.save(f'./images/guest-{index+1}.png')
