import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("CHANGES", "r", encoding="utf-8") as ch:
    changes = ch.read()

setuptools.setup(
    name="seletools",
    version="1.2.0",
    author="Dmitrii Bormotov",
    author_email="squier7@gmail.com",
    description="Helpful tools for Selenium on Python",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bormando/selenium-tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=[
        'seletools',
    ],
    package_data={
        'seletools': ['drag_and_drop.js']
    },
    python_requires='>=3.6',
)
