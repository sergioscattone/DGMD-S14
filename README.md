# Air Quality team - Wearable Devices and Computer Vision

## Solution

Our project aims to create an air quality sensor that could be used as a wearable and inform the user if the air quality around them is poor, prompting them to take action by turning on an air purifier or wearing a mask. We will use an Arduino dust sensor to build out a physical device, and display the output on a dashboard. On the dashboard we will also pull in air quality measures from other sources, like the Environmental Protection Agency (EPA). 

## Hardware

### Andruino

Brief description

### Sensor 1

Brief description

### Sensor 2

Brief description

### Sensor 3

Brief description

### Video

Maybe some video here: (example of how to embed a videohttps://github.com/alelievr/Mixture/blob/0.4.0/README.md)

## Software

### Tools

We are using collab as tool to interact with each other and apply advances in our code. <br/>
For that reasons we have our graph solutions made in python with [Matplotlib](https://matplotlib.org/). <br/>
For gathering the enviromental information we are calling different APIs from [AirNow](https://docs.airnowapi.org/). <br/>
Here it is our [collab notebook](https://colab.research.google.com/drive/1L0fGcY5KhRBeFsvSIR6Plb1Gl8LK7w7u) where we have many examples of API calls, examples of different graphs using Matplotlib and references for using and graphing linears and multi-linears regression (the bottom link).

### Graph1

Histogram of temperature, relative humidity, particle count

### Graph2

Linear graph of temperature, relative humidity, particle count during the hours of the day

### Graph3

Multi linear regression temperature, relative humidity, particle with pollutions by airnowapi (API call)
here we take some hours of data from andruino and airnowapi, and we try to see the relation between andruino meassures and environment pollution

### Graph4

AQI

### Dashboard

shows all the grapsh, shows the data collected, and shows a button or something to start the air filtering (and maybe some schedule for filtering based on the data)