import unittest

import minimalmodbus
import serial

from communication_settings import CommunicationSettings


class TestCommunicationSettings(unittest.TestCase):
    """ Ensures the correct communication parameter values for the Modbus CTS-602 """

    @classmethod
    def setUpClass(cls):
        cls.communication = CommunicationSettings()

    def test_PROTOCOL_should_be_present_with_correct_value(self):
        expected_value = minimalmodbus.MODE_RTU
        self.assertEqual(self.communication.PROTOCOL, expected_value, "Please define 'PROTOCOL' in the settings file")

    def test_NODE_ADDRESS_should_be_present_with_correct_value(self):
        expected_value = 30
        self.assertEqual(self.communication.NODE_ADDRESS, expected_value,
                         "Please define 'NODE_ADDRESS' in the settings file")

    def test_BAUDRATE_should_be_present_with_correct_value(self):
        expected_value = 19200
        self.assertEqual(self.communication.BAUD_RATE, expected_value, "Please define 'BAUDRATE' in the settings file")

    def test_DATABITS_should_be_present_with_correct_value(self):
        expected_value = 8
        self.assertEqual(self.communication.DATABITS, expected_value, "Please define 'DATABITS' in the settings file")

    def test_STOPBITS_should_be_present_with_correct_value(self):
        expected_value = 1
        self.assertEqual(self.communication.STOPBITS, expected_value, "Please define 'STOPBITS' in the settings file")

    def test_PARITY_should_be_present_with_correct_value(self):
        expected_value = serial.PARITY_EVEN
        self.assertEqual(self.communication.PARITY, expected_value, "Please define 'PARITY' in the settings file")

    def test_MAX_PACKET_SIZE_should_be_present_with_correct_value(self):
        expected_value = 255
        self.assertEqual(self.communication.MAX_PACKET_SIZE, expected_value,
                         "Please define 'TIMEOUT' in the settings file")

    def test_NILAN_SERIAL_PORT_should_be_present_with_correct_value(self):
        expected_value = 255
        self.assertEqual(self.communication.MAX_PACKET_SIZE, expected_value,
                         "Please define 'TIMEOUT' in the settings file")

    def test_TIMEOUT_should_be_present_with_correct_value(self):
        expected_value = 1.0
        self.assertEqual(self.communication.TIMEOUT, expected_value, "Please define 'TIMEOUT' in the settings file")


if __name__ == '__main__':
    unittest.main()
