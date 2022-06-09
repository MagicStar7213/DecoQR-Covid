from setuptools import setup

setup(
    name='qrcovid-decode',
    version='0.1.0',
    packages=['qrdecode'],
    url='https://github.com/MagicStar7213/DecoQR-Covid',
    license='AGPL-3.0',
    author='MagicStar',
    author_email='',
    description='EU Covid Certificate Decodificator',
    python_requires='>=3.5',
    install_requires = ["setuptools>=42", "pyzbar>=0.1.8", "opencv-python>=4.4.0.46", "base45>=0.4.0", "cbor2>=5.2.0"],
)
