from PIL import Image
import numpy as npy
import sys

#Membuka file gambar
img = Image.open('gambarrgb.jpg') 
mode = img.mode
width, height = img.size
gamma = float(input('Masukkan nilai gamma: '))
if mode == 'L':
	newImage = Image.new('L', (width, height))
else:
	newImage = Image.new('RGB', (width, height))
for i in range(width):
	for j in range(height):
		pixel = img.getpixel((i,j))
		if mode == 'L':
			newPixel = int(255 * (pixel / 255) ** gamma)
		else:
			R = int(255 * (pixel[0] / 255) ** gamma)
			G = int(255 * (pixel[1] / 255) ** gamma)
			B = int(255 * (pixel[2] / 255) ** gamma)
			newPixel = (R, G, B)
		newImage.putpixel((i,j), newPixel)
	#Menyimpan gambar
	newImage.save('gammargb2.jpg')