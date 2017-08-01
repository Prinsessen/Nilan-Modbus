import configparser
import logging
import os

import minimalmodbus
import serial


class CommunicationSettings:
    """ Holds the communication parameters for the nilan heat pump. """

    def __init__(self):
        self.logger = logging.getLogger()

        property_file = CommunicationSettings._get_property_file("../resources", "configuration.ini")

        config = configparser.ConfigParser()
        config.read(property_file)
        config.sections()

        self.PROTOCOL = CommunicationSettings.get_protocol(config['NILAN_MODBUS_SETTINGS']['PROTOCOL'])
        logging.debug("The configured PROTOCOL is %s", self.PROTOCOL)

        self.NODE_ADDRESS = int(config['NILAN_MODBUS_SETTINGS']['NODE_ADDRESS'])
        logging.debug("The configured NODE_ADDRESS is %s", self.NODE_ADDRESS)

        self.BAUD_RATE = int(config['NILAN_MODBUS_SETTINGS']['BAUD_RATE'])
        logging.debug("The configured BAUD_RATE is %s", self.BAUD_RATE)

        self.DATABITS = int(config['NILAN_MODBUS_SETTINGS']['DATABITS'])
        logging.debug("The configured DATABITS are %s", self.DATABITS)

        self.STOPBITS = int(config['NILAN_MODBUS_SETTINGS']['STOPBITS'])
        logging.debug("The configured STOPBITS is %s", self.STOPBITS)

        self.MAX_PACKET_SIZE = int(config['NILAN_MODBUS_SETTINGS']['MAX_PACKET_SIZE'])
        logging.debug("The configured MAX_PACKET_SIZE is %s", self.MAX_PACKET_SIZE)

        self.PARITY = CommunicationSettings.get_parity(config['NILAN_MODBUS_SETTINGS']['PARITY'])
        logging.debug("The configured PARITY is %s", self.PARITY)

        self.NILAN_SERIAL_PORT = config['NILAN_MODBUS_SETTINGS']['NILAN_SERIAL_PORT']
        logging.debug("The configured NILAN_SERIAL_PORT is %s", self.NILAN_SERIAL_PORT)

        self.TIMEOUT = float(config['NILAN_MODBUS_SETTINGS']['TIMEOUT']) / 1000
        logging.debug("The configured NILAN_SERIAL_PORT is %s", self.TIMEOUT)

    @staticmethod
    def get_protocol(protocol_name):
        default_protocol = minimalmodbus.MODE_RTU
        switcher = {
            'RTU': minimalmodbus.MODE_RTU,
            'ASCII': minimalmodbus.MODE_ASCII
        }
        return switcher.get(protocol_name.upper(), default_protocol)

    @staticmethod
    def get_parity(parity_name):
        default_parity = serial.PARITY_NONE
        switcher = {
            'NONE': serial.PARITY_NONE,
            'EVEN': serial.PARITY_EVEN,
            'ODD': serial.PARITY_ODD,
            'MARK': serial.PARITY_MARK,
            'SPACE': serial.PARITY_NAMES
        }
        return switcher.get(parity_name.upper(), default_parity)

    @staticmethod
    def _get_property_file(relative_path, filename):
        current_directory = os.path.abspath(os.path.dirname(__file__))
        return os.path.normpath(os.path.join(current_directory, relative_path, filename))
