from PIL import Image
import sys
import traceback

import pyocr
import pyocr.builders

args = sys.argv
if len(args) != 3:
    print("ERROR: Wrong number of arguments.")
    sys.exit(1)

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("ERROR: Not found OCR Tool")
    sys.exit(1)

tool = tools[0]
print("Using OCR Tool: '%s'" % (tool.get_name()))

try:
    image = Image.open(args[1])
except FileNotFoundError:
    print("Target image file not found")
    sys.exit(1)

lang = args[2]

try:
    txt = tool.image_to_string(
        image,
        lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
except Exception as e:
    print("ERROR: TesseractError")
    print(e)
    print("======> Traceback")
    print(traceback.format_exc()) 
    sys.exit(1)

print("======> FINISH")
print(txt)
