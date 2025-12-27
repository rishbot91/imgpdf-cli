import sys
import os
import img2pdf
from pathlib import Path

def get_downloads_folder():
    return Path.home() / "Downloads"

def jpg_to_pdf(images, output_name):
    downloads = get_downloads_folder()
    output_pdf = downloads / output_name

    if not images:
        print("No images provided.")
        return

    for img in images:
        if not os.path.exists(img):
            print(f"File not found: {img}")
            return

    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(images))
        print(f"PDF saved to: {output_pdf}")
    except Exception as e:
        print("Conversion failed:", e)


def main():
    args = sys.argv[1:]

    if len(args) < 3:
        print("Usage:")
        print('  python src/main.py jpg2pdf "a.jpg" "b.jpg" output.pdf')
        return

    command = args[0]

    if command == "jpg2pdf":
        *images, output_name = args[1:]
        jpg_to_pdf(images, output_name)
    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()
