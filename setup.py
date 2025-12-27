from setuptools import setup

setup(
    name="imgpdf",
    version="0.1",
    py_modules=["imgpdf"],
    entry_points={
        "console_scripts": [
            "cnvrt=imgpdf:main"
        ]
    },
)
