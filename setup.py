from setuptools import setup

with open("README.md", "rt", encoding="utf8") as f:
    README = f.read()

setup(
    name="komoe-sass",
    version="0.1.0",
    description="Sass plugin for komoe",
    long_description=README,
    long_description_content_type="text/markdown",
    license="Public domain",
    author="Louis DEVIE",
    url="https://github.com/louisdevie/komoe-sass",
    packages=["komoe_sass"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=[
        "komoe",
        "sass",
        "scss",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Komoe>=0.2.1",
    ],
)
