from PIL import Image
import sys
import argparse
import traceback
import pyocr
import pyocr.builders
import pathlib


def main(img, lang, output):
    try:
        image = Image.open(img)
    except FileNotFoundError:
        print("Target image file not found")
        sys.exit(1)

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

    if output:
        try:
            with open(output, mode="w") as f:
                f.write(txt)
        except NotADirectoryError as e:
            print("ERROR: This is not a valid file path.")
            print(e)
            sys.exit(1)
        except FileNotFoundError as e:
            print("ERROR: This is not a valid file path.")
            print(e)
            sys.exit(1)


    print("======> FINISH")
    print(txt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OCR sample")
    parser.add_argument("img", metavar="img", type=pathlib.Path, help="Target image path")
    parser.add_argument("lang", metavar="lang", help="Language")
    parser.add_argument("output", metavar="output", type=pathlib.Path, nargs="?", default=False, help="Path to output text file")
    args = parser.parse_args()

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("ERROR: Not found OCR Tool")
        sys.exit(1)

    tool = tools[0]
    print("Using OCR Tool: '%s'" % (tool.get_name()))

    main(args.img, args.lang, args.output)