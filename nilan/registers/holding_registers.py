from collections import namedtuple
from enum import Enum, unique


class Parameter(namedtuple('Parameter', "address scale unit description")):
    def __new__(cls, address, scale=None, unit=None, description=None):
        return super().__new__(cls, address, scale, unit, description)

    def __getnewargs__(self):
        return self.address, self.scale, self.unit, self.description


@unique
class HoldingRegister(Parameter, Enum):
    #  000 Device - Protocol and controller setup
    BUS_VERSION = Parameter(address=0, description="Protocol version number")

    #  200 Analog I/O - Input / output words
    OUTPUT_EXHAUSTSPEED = Parameter(address=200, scale=100, unit="%", description="Exhaust fan speed")
    OUTPUT_INLETSPEED = Parameter(address=201, scale=100, unit="%", description="Inlet fan speed")
    OUTPUT_AIRHEATCAP = Parameter(address=202, scale=100, unit="%", description="Air heater capacity")
    OUTPUT_CENHEATCAP = Parameter(address=203, scale=100, unit="%", description="Central heater capacity")
    OUTPUT_CPRCAP = Parameter(address=204, scale=100, unit="%", description="Compressor capacity")
    OUTPUT_PREHEATCAP = Parameter(address=205, scale=100, unit="%",
                                  description="Preheater capacity or earth tube air intake fan speed")

    #  300 Time - Clock and calendar
    TIME_SECOND = Parameter(address=300, unit="ss", description="Second")
    TIME_MINUTE = Parameter(address=301, unit="nn", description="Minute")
    TIME_HOUR = Parameter(address=302, unit="hh", description="Hour")
    TIME_DAY = Parameter(address=303, unit="dd", description="Day")
    TIME_MONTH = Parameter(address=304, unit="mm", description="Month")
    TIME_YEAR = Parameter(address=305, unit="yyyy", description="Year")

    #  400 Alarm - Alarm and message handling
    ALARM_RESET = Parameter(address=400,
                            description="Clear one specific alarm code or all \n"
                                        "0 : No command \n 1..99 : (reserved internal commands) \n"
                                        "101..199 : Clear alarm display code 1..99 \n"
                                        "255 : Clear all alarms")

    #  500 Week program - Calendar based programming
    PROGRAM_SELECT = Parameter(address=500, description="Week program nb. select \n"
                                                        "0 : None \n"
                                                        "1 : Program 1 \n"
                                                        "2 : Program 2 \n"
                                                        "3 : Program 3 \n"
                                                        "4 : Erase")

    #  600 User functions - User input function selection
    # 1000 Control - System control and status
    # 1100 AirFlow - Ventilation control
    # 1200 AirTemp - Room temperature control
    # 1400 AirHeat - Inlet air heater control
    # 1500 Compressor - Compressor operation control
    # 1600 Defrost - Defrosting control
    # 1900 AirQual - Air quality control (RH, CO2)
    # 2000 User panel - Display and keyboard
