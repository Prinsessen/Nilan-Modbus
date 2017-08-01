# coding=utf-8
from collections import namedtuple
from enum import Enum, unique


class Parameter(namedtuple('Parameter', "address scale unit description")):
    def __new__(cls, address, scale=None, unit=None, description=None):
        return super().__new__(cls, address, scale, unit, description)

    def __getnewargs__(self):
        return self.address, self.scale, self.unit, self.description


@unique
class InputRegister(Parameter, Enum):
    #  000 Device - Protocol and controller setup
    BUS_ADDRESS = Parameter(address=0, description="Protocol node address (default = 30)")

    #  100 Discrete I/O - Protocol and controller setup
    INPUT_USERFUNC = Parameter(address=100, description="User function")
    INPUT_AIRFILTER = Parameter(address=101, description="Air filter alarm")
    INPUT_DOOROPEN = Parameter(address=102, description="Door contact")
    INPUT_SMOKE = Parameter(address=103, description="Smoke alarm")
    INPUT_MOTORTHERMO = Parameter(address=104, description="Motor thermal fuse")
    INPUT_FROST_OVERHT = Parameter(address=105, description="Heating surface frost / overheat")
    INPUT_AIRFLOW = Parameter(address=106, description="Airflow monitor")
    INPUT_P_HI = Parameter(address=107, description="High pressure switch")
    INPUT_P_LO = Parameter(address=108, description="Low pressure switch")
    INPUT_BOIL = Parameter(address=109, description="Hot water boiling")
    INPUT_3WAYPOS = Parameter(address=110, description="Hot water 3-way valve position")
    INPUT_DEFROSTHG = Parameter(address=111, description="Hotgas defrost type selection")
    INPUT_DEFROST = Parameter(address=112, description="Defrost thermostat")
    INPUT_USERFUNC_2 = Parameter(address=113, description="User function 2")
    INPUT_DAMPERCLOSED = Parameter(address=114, description="Air damper closed position switch")
    INPUT_DAMPEROPENED = Parameter(address=115, description="Air damper closed position switch")

    #  200 Analog I/O - Input / output words
    INPUT_T0_CONTROLLER = Parameter(address=200, scale=100, unit="°C", description="Controller board temperature")
    INPUT_T1_INTAKE = Parameter(address=201, scale=100, unit="°C", description="Fresh air intake temperature")
    INPUT_T2_INLET = Parameter(address=202, scale=100, unit="°C", description="Inlet temperature (before heater)")
    INPUT_T3_EXHAUST = Parameter(address=203, scale=100, unit="°C", description="Room exhaust temperature")
    INPUT_T4_OUTLET = Parameter(address=204, scale=100, unit="°C", description="Outlet temperature")
    INPUT_T5_COND = Parameter(address=205, scale=100, unit="°C", description="Condenser temperature")
    INPUT_T6_EVAP = Parameter(address=206, scale=100, unit="°C", description="Evaporator temperature")
    INPUT_T7_INLET = Parameter(address=207, scale=100, unit="°C", description="Inlet temperature (after heater)")
    INPUT_T8_OUTDOOR = Parameter(address=208, scale=100, unit="°C", description="Outdoor temperature")
    INPUT_T9_HEATER = Parameter(address=209, scale=100, unit="°C", description="Heating surface temperature")
    INPUT_T10_EXTERN = Parameter(address=210, scale=100, unit="°C", description="External room temperature")
    INPUT_T11_TOP = Parameter(address=211, scale=100, unit="°C", description="Hot water top temperature")
    INPUT_T12_BOTTOM = Parameter(address=212, scale=100, unit="°C", description="Hot water bottom temperature")
    INPUT_T13_RETURN = Parameter(address=213, scale=100, unit="°C", description="EK return temperature")
    INPUT_T14_SUPPLY = Parameter(address=214, scale=100, unit="°C", description="EK supply temperature")
    INPUT_T15_ROOM = Parameter(address=215, scale=100, unit="°C", description="User panel room temperature")
    INPUT_T16 = Parameter(address=216, scale=100, unit="°C", description="AUX temperature (Hotwater anode)")
    INPUT_T17_PREHEAT = Parameter(address=217, scale=100, unit="°C", description="Preheater or earth tube air intake temperature")

    AirQual_RH = Parameter(address=221, scale=100, unit="°C", description="Humidity sensor value")
    AirQual_CO2 = Parameter(address=222, scale=100, unit="°C", description="Carbon dioxide sensor value")

    #  300 Time - Clock and calendar

    #  400 Alarm - Alarm and message handling
    ALARM_STATUS = Parameter(address=400, description="Alarm state bit mask"
                                                      "0x80 : Active alarm(s) are present"
                                                      "0x03 : Number of alarms listed")
    ALARM_LIST_1_ID = Parameter(address=401, description="Alarm 1 - Code"
                                                         "0x80 : (reserved future use)"
                                                         "0x7F : Display code 1..99")
    ALARM_LIST_1_DATE = Parameter(address=402, description="Alarm 1 - Date"
                                                           "Bit word packed in DOS date format"
                                                           "Year 0 = 1980"
                                                           "15     8 7      0"
                                                           "YYYYYYYM MMMDDDDD")
    ALARM_LIST_1_TIME = Parameter(address=403, description="Alarm 1 - Time"
                                                           "Bit word packed in DOS time format"
                                                           "Seconds are in scale 2 (0..29 = 0..58 seconds)"
                                                           "15     8 7      0"
                                                           "HHHHHMMM MMMSSSSS)")
    ALARM_LIST_2_ID = Parameter(address=404, description="Alarm 2 - Code")
    ALARM_LIST_2_DATE = Parameter(address=405, description="Alarm 2 - Date")
    ALARM_LIST_2_TIME = Parameter(address=406, description="Alarm 2 - Time")
    ALARM_LIST_3_ID = Parameter(address=407, description="Alarm 3 - Code")
    ALARM_LIST_3_DATE = Parameter(address=408, description="Alarm 3 - Date")
    ALARM_LIST_3_TIME = Parameter(address=409, description="Alarm 3 - Time")

    #  500 Week program - Calendar based programming
    #  600 User functions - User input function selection

    # 1000 Control - System control and status
    CONTROL_RUNACT = Parameter(address=1000, description="Actual on/off state"
                                                         "0 : Off"
                                                         "1 : On")
    CONTROL_MODEACT = Parameter(address=1001, description="Actual operation mode"
                                                          "0 : Off"
                                                          "1 : Heat"
                                                          "2 : Cool"
                                                          "3 : Auto"
                                                          "4 : Service")
    CONTROL_STATEDISPLAY = Parameter(address=1002, description="Actual control state"
                                                               "0 : Off"
                                                               "1 : Shift"
                                                               "2 : Stop"
                                                               "3 : Start"
                                                               "4 : Standby"
                                                               "5 : Ventilation stop"
                                                               "6 : Ventilation"
                                                               "7 : Heating"
                                                               "8 : Cooling"
                                                               "9 : Hot water"
                                                               "10 : Legionella"
                                                               "11 : Cooling + hot water"
                                                               "12 : Central heating"
                                                               "13 : Defrost"
                                                               "14 : Frost sequre"
                                                               "15 : Service"
                                                               "16 : Alarm"
                                                               "17 : Heating + hot water")
    CONTROL_SECINSTATE = Parameter(address=1003, unit="Sec", description="Actual time in state")

    # 1100 AirFlow - Ventilation control
    AIRFLOW_VENTSET = Parameter(address=1100, unit="Step", description="Actual ventilation step set point"
                                                                       "0 : Off"
                                                                       "1..4 : Step number")
    AIRFLOW_INLETACT = Parameter(address=1101, unit="Step", description="Actual inlet fan speed step"
                                                                        "0 : Off"
                                                                        "1..4 : Step number")
    AIRFLOW_EXHAUSTACT = Parameter(address=1102, unit="Step", description="Actual exhaust fan speed step"
                                                                          "0 : Off"
                                                                          "1..4 : Step number")
    AIRFLOW_SINCEFILTDAY = Parameter(address=1103, unit="Days", description="Days since last air filter change alarm"
                                                                            "One day is measured as 24 hours of active running time")
    AIRFLOW_TOFILTDAY = Parameter(address=1104, unit="Step", description="Days to next air filter change alarm"
                                                                         "One day is measured as 24 hours of active running time")

    # 1200 AirTemp - Room temperature control
    AIRTEMP_ISSUMMER = Parameter(address=1200, description="Summer state"
                                                           "0 : Off"
                                                           "1 : On")
    AIRTEMP_TEMPINLETSET = Parameter(address=1201, scale=100, unit="°C",
                                     description="Inlet temperature request (T7 setpoint)")
    AIRTEMP_TEMPCONTROL = Parameter(address=1202, scale=100, unit="°C",
                                    description="Actual value for controlled temperature")
    AIRTEMP_TEMPROOM = Parameter(address=1203, scale=100, unit="°C",
                                 description="Actual room temperature (T15 or T10)")
    AIRTEMP_EFFPCT = Parameter(address=1204, scale=100, unit="%",
                               description="Passive heat exchanger efficiency calculation")
    AIRTEMP_CAPSET = Parameter(address=1205, scale=100, unit="%", description="Requested capacity")
    AIRTEMP_CAPACT = Parameter(address=1206, scale=100, unit="%", description="Actual capacity")

    # 1400 AirHeat - Inlet air heater control
    # 1500 Compressor - Compressor operation control
    # 1600 Defrost - Defrosting control
    # 1900 AirQual - Air quality control (RH, CO2)

    # 2000 User panel - Display and keyboard
    DISPLAY_LED_1 = Parameter(address=2000, description="User Panel indicator light")
    DISPLAY_LED_2 = Parameter(address=2001)
    DISPLAY_TEXT_1_2 = Parameter(address=2002, unit="ascii", description="Text line 1 character 1-2")
    DISPLAY_TEXT_3_4 = Parameter(address=2003, unit="ascii", description="Text line 1 character 3-4")
    DISPLAY_TEXT_5_6 = Parameter(address=2004, unit="ascii", description="Text line 1 character 5-6")
    DISPLAY_TEXT_7_8 = Parameter(address=2005, unit="ascii", description="Text line 1 character 7-8")
    DISPLAY_ATTR_1_8 = Parameter(address=2006, description="Text line 1 flags")
    DISPLAY_TEXT_9_10 = Parameter(address=2007, unit="ascii", description="Text line 2 character 9-10")
    DISPLAY_TEXT_11_12 = Parameter(address=2008, unit="ascii", description="Text line 2 character 11-12")
    DISPLAY_TEXT_13_14 = Parameter(address=2009, unit="ascii", description="Text line 2 character 13-14")
    DISPLAY_TEXT_15_16 = Parameter(address=2010, unit="ascii", description="Text line 2 character 15-16")
    DISPLAY_ATTR_9_16 = Parameter(address=2011, description="Text line 2 flags")
