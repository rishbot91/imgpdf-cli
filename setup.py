from setuptools import setup

setup(
    name="imgpdf",
    version="1.0",
    py_modules=["imgpdf"],
    entry_points={
        "console_scripts": [
            "cnvrt=imgpdf:main"
        ]
    },
)
