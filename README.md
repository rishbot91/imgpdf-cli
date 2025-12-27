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

## Make cnvrt available globally on Windows

By default, the cnvrt command works only inside the virtual environment.
To use it from any folder in CMD or PowerShell, add the venv Scripts folder to Windows PATH.

### Activate your venv and run:

```bash
where cnvrt
```

### Example output

```bash
C:\Users\name\imgpdf-cli\.venv\Scripts\cnvrt.exe
```

### Add folder to Windows PATH

1. Press Win + R, type:

```bash
sysdm.cpl
```

2. Go to Advanced → Environment Variables
3. Under User variables, select Path → Edit
4. Click New → paste:

```bash
C:\Users\name\imgpdf-cli\.venv\Scripts
```

5. Click OK on all windows.
6. Restart all terminals.

## Usage

### Convert JPG to PDF

```bash
cnvrt jpg2pdf "photo.jpg"
```

Multiple images into one PDF:

```bash
cnvrt jpg2pdf "a.jpg" "b.jpg" output.pdf
```

If output file is not provided, the tool generates one automatically. All files are saved in your Downloads folder.

## Tech Stack

- Python
- img2pdf
- Pillow
- setuptools
