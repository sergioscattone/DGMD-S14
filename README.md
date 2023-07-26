# Air Quality team - Wearable Devices and Computer Vision

## Solution

Our project aims to create an air quality sensor that could be used as a wearable and inform the user if the air quality around them is poor, prompting them to take action by turning on an air purifier or wearing a mask. <br/>
We will use an Arduino dust sensor to build out a physical device, and display the output on a dashboard. <br/>
On the dashboard we will also pull in air quality measures from other sources, like the Environmental Protection Agency (EPA). <br/>

## Definitions

### AQI
The EPA developed the AQI, which reports levels of ozone, particle pollution, and other common air pollutants on the same scale. <br/>
An AQI reading of 101 corresponds to a level above the national air quality standard - the higher the AQI rating, the greater the health impact. <br/>
To know more about the AQI you can go to: [https://docs.airnowapi.org/aq101] <br/>

### PM
We will be focusing on measuring levels of particulate matter (PM) in the immediate area of the device using an Arduino dust sensor. <br/>
The Arduino dust sensor collects counts of particles greater than 1 micron in size as air flows through the sensor. <br/>
From those particle counts, we will have to estimate the total mass of particles present, as mass is the official reported standard for particulate matter used by the EPA. <br/>
From those masses, we will be able to determine the Air Quality Index (AQI) measurement for particulate matter. <br/>

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
We are using colab as tool to interact with each other and apply advances in our code. <br/>
For that reasons we have our graph solutions made in python with [Matplotlib](https://matplotlib.org/). <br/>
For gathering the enviromental information we are calling different APIs from [AirNowAPI](https://docs.airnowapi.org/). <br/>
Here it is our [colab notebook](https://colab.research.google.com/drive/1L0fGcY5KhRBeFsvSIR6Plb1Gl8LK7w7u) where we have many examples of API calls, examples of different many analysis of parameters with their correlative graphs. <br/>
In the colab file you will find evaluation of Temperature measure, Relative Humidity measure, Particulates Matter measure, a simulation of the effect of an air purifier, an AQI calculator and a comparative from the values inside the house and outside using the AirNowApi.

### Dashboard: Temperature, Relative Humidity, Particulates Matter, and AQI

Here it is an screenshot of the dashboard that groups most useful graphs from all the ones we presented on our colab notebook.
![Dashboard](img/dashboard.png.png)
In this dashboard, for the first four graphs we are showing the Temperature measures with its mean and standar deviation. <br/>
The last one is an histogram of the AQI values, and it also says the relation with the AQI outside the house (locating the user zone by its zipcode or by latitude and longitude). <br/>
There it is also an implementation of audio alerts for the users, that prevents them in case the consentration of PM are too high, that the relative humidity is above 95%, or that the celsius degrees are above 46 which both things provoke the air dust sensor to fail.

### Colab and python files 

In this repository you will find the colab notebook in the `colab_notebook.ipynb` file and all the python code in the `dashboards_and_data.py` file which basically is the colab notebook exported as python code.

### Sensonrs data

For collecting the sensors' data we use an script that is in `get_pm/get_pm.ino`. <br/>
The algorithms used to calculate the AQI from the sensor data is modularized in the `pm_utils.py` file.  <br/>
However, both colab notebook and python dashboard files have integrated all that is needed to run without the need to include the `get_pm/get_pm.ino` file.

### Samples

In the `data_samples` you will see two files with samples that we have taken with the Andruino device. In them we have put the sensors close to a kitchen while using it to see the efects in the measures.