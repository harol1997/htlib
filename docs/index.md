# HTLIB 

***
### class BSerial

~~~
__init__(self, **kargs)
~~~     

Parameters: 

- **kargs: init from Serial, more information in [pyserial Documentation](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)

    
    example:
    
    port: Device name
    
    baudrate(int): baud rate such as 9600 or 115200 
    

~~~
write_string_port(self, value)
~~~
    
method to send some value to serial port. Add '\n' to endLine, you have to control it.

Parameters:
    
- value (float): this value will convert to string to send it to serial port

~~~
start_read_string_port(self,command, separator="-"):
~~~

        
method to start to receive values.
If you want send many values from a device. You have to separate the values with '-'.
you can change it set a new separator like argument in this method.

Parameters:

- command (function): create in this "function" the actions to the value received

- sepatator (str): define separation between values has been readed


***