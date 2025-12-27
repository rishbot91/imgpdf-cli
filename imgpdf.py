import sys
import os
import img2pdf
from pathlib import Path
from datetime import datetime


def get_downloads_folder():
    return Path.home() / "Downloads"


def generate_default_name():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"images_{timestamp}.pdf"


def jpg_to_pdf(images, output_name=None):
    downloads = get_downloads_folder()

    if not output_name:
        output_name = generate_default_name()

    output_pdf = downloads / output_name

    for img in images:
        if not os.path.exists(img):
            print(f"File not found: {img}")
            return

    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))

    print(f"PDF saved to: {output_pdf}")


def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage:")
        print('  convert jpg2pdf "a.jpg" "b.jpg" [output.pdf]')
        return

    command = args[0]
    files = args[1:]

    if command == "jpg2pdf":
        if files[-1].lower().endswith(".pdf"):
            *images, output = files
        else:
            images = files
            output = None

        jpg_to_pdf(images, output)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
