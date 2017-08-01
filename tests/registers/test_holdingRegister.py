from unittest import TestCase

from registers.holding_registers import HoldingRegister


class TestHoldingRegister(TestCase):

    def test_ADDRESS_matches(self):
        expected_value = 200
        self.assertEqual(HoldingRegister.OUTPUT_EXHAUSTSPEED.address, expected_value)

    def test_SCALE_matches(self):
        expected_value = 100
        self.assertEqual(HoldingRegister.OUTPUT_EXHAUSTSPEED.scale, expected_value)

    def test_UNIT_matches(self):
        expected_value = "%"
        self.assertEqual(HoldingRegister.OUTPUT_EXHAUSTSPEED.unit, expected_value)

    def test_DESCRIPTION_matches(self):
        expected_value = "Exhaust fan speed"
        self.assertEqual(HoldingRegister.OUTPUT_EXHAUSTSPEED.description, expected_value)
