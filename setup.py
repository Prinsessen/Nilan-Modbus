from setuptools import setup

install_requires = [
    "pyserial",
    "minimalmodbus",
    "RPi.GPIO"
]

tests_require = [
    "pyModbusTCP"
]

setup(
    name='NilanModbus',
    version='0.0.1-SNAPSHOT',
    install_requires=install_requires,
    tests_require=tests_require,
)
