from rembg import remove
import easygui
from PIL import Image

inputPath = 'cat.jpg'
outputPath = 'out.png'
input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)