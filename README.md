# Air Quality team - Wearable Devices and Computer Vision

## Solution

Our project aims to create an air quality sensor that could be used as a wearable and inform the user if the air quality around them is poor, prompting them to take action by turning on an air purifier or wearing a mask. <br/>
We will use an Arduino dust sensor to build out a physical device, and display the output on a dashboard. <br/>
On the dashboard we will also pull in air quality measures from other sources, like the Environmental Protection Agency (EPA). 

## Hardware

### Arduino

We have an Arduino Uno Board attached to a grove input shield. We connect this board to a laptop over USB which provides both power and a means of bi-directional data transfer. We use the microcontroller to take measurements every 30 seconds and pass that information to the serial port where additional processing or data transfer can take place. In our proof of concept we directly stream the serial port output and write it to a csv.

### Seeedlabs Temperature and humidity sensor

The Seedlabs temperature and humidity sensor outputs temperature in celsius and relative humidity
as digital values. We read these alongside the PM sensor as the sensor cannot properly function above 45 degrees celsius or 95% humidity. 

### Seeedlabs Grove Dust Sensor

The Seeedlabs Grove Dust Sensor is a Shinyei PPD42 dust sensor vendored by Seeed Labs to be connected to an  Arduino board over a grove connector that reliably measure particles in between 1um and 2.5ums in size. When there are particles present, the sensor switches from producing a high voltage output to a low voltage output. To calculate the particle concentration, we regularly sample the output of the sensor and  calulate the %age of  time that the sensor is producing low voltage output. We then use anequation (sourced from sensor documentation) to calculate the number of particles per 0.01 cubic feet of air taking the ratio of low pulse occupancy as input.

To calculate pm2.5 concentration as mass per cubic meter of air, we convert the particle count from particles per 0.01 cubic feet to particles per cubic meter. We then need to make two key assumptions to enable us to calculate PM mass. First we need to determine the size of the particle. To do this, we assume that all detected partcles are uniformly distributed in size within the sensors detectable range (1um-2.5um), therefore we assume that all particles are of  the mean of  that rante, with a diameter of 1.75um. We also assume that all particles have the unit density, an assumption we've seen applied by [past studies](https://academic.oup.com/annweh/article/50/8/843/154938) using low cost sensors. We then calculate the total mass by multiplying the volume of the average particle (assuming that it's spherical) by the unit density and multiplying it by the particle count.



### Video

Maybe some video here: (example of how to embed a videohttps://github.com/alelievr/Mixture/blob/0.4.0/README.md)

## Software

In this section we will take the input from the sensors and we will show it in different graphs.

### Tools

We are using collab as tool to interact with each other and apply advances in our code. <br/>
For that reasons we have our graph solutions made in python with [Matplotlib](https://matplotlib.org/). <br/>
For gathering the enviromental information we are calling different APIs from [AirNow](https://docs.airnowapi.org/). <br/>
Here it is our [collab notebook](https://colab.research.google.com/drive/1L0fGcY5KhRBeFsvSIR6Plb1Gl8LK7w7u) where we have many examples of API calls, examples of different graphs using Matplotlib and references for using and graphing linears and multi-linears regression (the bottom link).

### Graph1: Histogram of temperature, relative humidity and particle count



### Graph2

Linear graph of temperature, relative humidity, particle count during the hours of the day

### Graph3

Multi linear regression temperature, relative humidity, particle with pollutions by airnowapi (API call)
here we take some hours of data from andruino and airnowapi, and we try to see the relation between andruino meassures and environment pollution

### Graph4

AQI

### PM Utilities

The 

### Dashboard

shows all the grapsh, shows the data collected, and shows a button or something to start the air filtering (and maybe some schedule for filtering based on the data)