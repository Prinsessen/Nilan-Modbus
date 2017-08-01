# Nilan (R) modbus communication bring-up
That project is supposed to provide software for basic communication with nilan heatpumps, containing the CTS-602 control board.

## Hardware Pre-Requirements
An RS485 adapter, because Nilan is using modbus on top of the physical RS485 layer.

# Connection description
HAZARD NOTE:
:warning: If you do not know how to carefully deal with electricity stop here. 
High voltage danger! No warranties.

The CTS-602 is inside the heatpump, and the correct connectors are on the
lower left corner on the circuit board (see picture). 
The pins on the RS485 connector have the following order: 

| | | |
|---|---|---|
| Pin 1	| 12 VDC output | |
| Pin 2	| COM1- RS 485 A | Modbus |
| Pin 3	| COM1 - RS 485 B | Modbus |
| Pin 4	| COM2 - RS 485 A | User panel |
| Pin 5	| COM2 - RS 485 B | User panel |
| Pin 6	| Ground |
| | |



As you would find it in the [Nilan Modbus Protocol](http://reader.livedition.dk/nilan/272/) manual. 
<!-- MOD-BUS-CTS602-GB.pdf --> 

For the modbus connection you need the pins 2,3,6. 
In the picture pins two and three are not connected.



## Further Reading
[API for MinimalModbus](https://minimalmodbus.readthedocs.io/en/master/apiminimalmodbus.html#minimalmodbus.Instrument.read_register)


[Nilan Modbus Protocol Specification](http://de.nilan.dk/startseite/download/archiv?Folder=%2fCTS+602)
