from PIL import Image, ImageDraw, ImageFont

def add_num(image):
	draw = ImageDraw.Draw(image)
	fillcolor = "#ff0000"
	#zmyfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
	width,height= image.size
	draw.text((width-80,10),'99',fill=fillcolor)
	image.save('result.png')


if __name__=='__main__':
	image=Image.open('mouse.png')
	add_num(image)

