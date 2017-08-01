After the RS485 Shield is connected to the RaspberryPI execute the following commands.

Install dependency Libraries
1. Update source list
```commandline
    sudo apt-get update
```

2 . Install python-pip
```commandline
    sudo apt-get install python-pip
```

3.Use pip to install WiringPi (WiringPi is designed for raspberry pi to behave similarly to that of the wiring library under Arduino. After this library is installed, c, shell or python can use the function to configure and control GPIOs directly. :
```commandline
    sudo pip install wiringpi
```


4. Installed the associated library files of serial ports :
```commandline
    sudo apt-get install python-serial
```


5.Test whether the GPIO library and the serial library is installed or not:
```commandline
    python
```
```python
    import RPi.GPIO
    import serial
```

If there is no error , then the two libraries are installed correctly.
[Screenshot](http://cnlearn.linksprite.com/wp-content/uploads/2013/10/图片16.png)

6. We need to configure file `/boot/cmdline.txt` to remove the kernel booting information and debug message:
```commandline
    sudo nano /boot/cmdline.txt
```



You can see the following information:
```
    dwc_otg.lpm_enable = 0 console = ttyAMA0, 115200 kgdboc = ttyAMA0, 115200 console = tty1 root = / dev/mmcblk0p2 rootfstype = ext4 elevator = deadline rootwait
```
Remove `console = ttyAMA0, 115200 kgdboc = ttyAMA0, 115200` so that the information becomes:
```
    dwc_otg.lpm_enable = 0 console = tty1 root = / dev/mmcblk0p2 rootfstype = ext4 elevator = deadline rootwait
```


7. Disable log in from the serial port:
```commandline
   sudo nano /etc/inittab
```

and comment out `T0: 23: respawn :/ sbin / getty-L ​​ttyAMA0 115200 vt100`

8 Restart Raspberry Pi:
```commandline
    sudo reboot
```


Now you can use / dev/ttyAMA0 like the regular COM port.

Python

Test code(serial_test.py) :
```python
    #!/usr/bin/python
    # -*- coding: utf-8 -*- 
    import serial
     
    port = ”/dev/ttyAMA0″
     
    usart = serial.Serial(port,9600)
     
    usart.flushInput()
     
    print (“serial test: BaudRate = 9600″)
     
    usart.write(“please enter the character:\r”)
     
    while True:
     
       if( usart.inWaiting()>0 ) :
     
          receive = usart.read(1)
     
          print ”receive: ”,receive
     
          usart.write(“  send: ’”)
     
          usart.write(receive)
     
          usart.write(“‘\r”)
```