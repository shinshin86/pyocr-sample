# pyocr-sample

pyocr sample.  
This project uses pipenv.

## Setup

```sh
pipenv install
```

And the OCR engine, [Tesseract](https://github.com/tesseract-ocr/tesseract), must be installed.

## Using

```bash
pipenv run start {target image path} {read lang name}
```

Example

```bash
# Read the image of Japanese
pipenv run start test.jpg jpn
```

Results can also be exported to a text file.

```sh
pipenv run start test.jpg jpn output.txt
```