from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="decoqr-covid",
    version="0.1.0",
    author="Example Author",
    author_email="author@example.com",
    description="A EU Digital COVID Certificate Scanner and Decoder",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/MagicStar7213/DecoQR-Covid",
    project_urls={
        "Bug Tracker": "https://github.com/MagicStar7213/DecoQR-Covid/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "qrdecode"},
    packages=find_packages(where="qrdecode"),
    python_requires=">=3.5",
    install_requires=["setuptools>=42", "pyzbar>=0.1.8", "opencv-python>=4.4.0.46", "base45>=0.4.0", "cbor2>=5.2.0"]
)