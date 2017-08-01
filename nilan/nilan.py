from communication_settings import *
from registers.input_registers import InputRegister
from registers.register_types import Register


class Nilan(minimalmodbus.Instrument):
    """ Instrument class for nilan heat pump. Communication via RS485 """

    def __init__(self):
        communication = CommunicationSettings()
        minimalmodbus.Instrument.__init__(self, communication.NILAN_SERIAL_PORT, communication.NODE_ADDRESS)

        self.serial.baudrate = communication.BAUD_RATE
        self.serial.parity = communication.PARITY
        self.serial.timeout = communication.TIMEOUT
        self.mode = communication.PROTOCOL

    ########################
    # read input registers #
    ########################
    def get_bus_address(self):
        return self.read_input_register(InputRegister.BUS_ADDRESS)

    def get_software_version(self):
        major_version = self.read_register(1)
        minor_version = self.read_register(2)
        release_version = self.read_register(3)

        return "{}.{}.{}".format(major_version, minor_version, release_version)

    def get_air_filter_alarm(self):
        return self.read_input_register(InputRegister.INPUT_AIRFILTER)

    def get_controller_board_temperature(self):
        return self.read_input_register(InputRegister.INPUT_T0_CONTROLLER)

    def get_fresh_air_intake_temperature(self):
        return self.read_input_register(InputRegister.INPUT_T1_INTAKE)

    def get_t11_top(self):
        return self.read_input_register(InputRegister.INPUT_T11_TOP)

    # read and write

    def set_airflow_ventset(self, speed=2):
        if (speed < 0) or (speed > 4):
            raise ValueError
        return self.write_register(InputRegister.AIRFLOW_VENTSET, speed)

    def get_aiflow_ventset(self):
        return self.read_input_register(InputRegister.AIRFLOW_VENTSET)

    ##########################
    # read holding registers #
    ##########################

    #####################
    # wrapper functions #
    #####################

    def read_input_register(self, register: InputRegister):
        return self.read_register(registeraddress=register.address, numberOfDecimals=register.scale,
                                  functioncode=Register.INPUT_REGISTER.functioncode)

    def write_input_register(self, register: InputRegister, value):
        return self.write_register(registeraddress=register.address, numberOfDecimals=register.scale, value=value)
