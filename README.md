# Convert - JPG to PDF CLI tool
A lightweight command-line utility to convert JPG images to PDF files locally

All generated PDFs are automatically saved to your system Downloads folder.

## Installation

### Clone the repo
```bash
git clone https://github.com/rishbot91/imgpdf-cli.git
cd imgpdf-cli
```

### Create & activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Install CLI tool
```bash
pip install -e .
```

## Usage

### Convert JPG to PDF
```bash
convert jpg2pdf "photo.jpg"
```

Multiple images into one PDF:
```bash
convert jpg2pdf "a.jpg" "b.jpg" output.pdf
```

If output file is not provided, the tool generates one automatically. All files are saved in your Downloads folder.

## Tech Stack
- Python
- img2pdf
- Pillow
- setuptools




