# Arduino Code for reading from the dust sensor

This .ino code works with an arduino board with attached temperature and humidity sensors
as well as an attached dust sensor. It reads temperature, humidty, and particle count then outputs 
those values to the serial port to be read by an external system.

We limit on board processing currently to minimize the work required of the microcontroller.