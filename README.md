# chicken-water-feeder
Chicken water feeder project repository. Plans, software, documentation, meeting notes.

## Summary

This project is for a chicken water feeder that controls the tempature of the water to prevent freezing, negating the need to manage animal water supply during the colder months.

## Goals

1. We only want to create a prototype.
2. We want to create the prototype quickly.
3. We want to use an iterative process in the future to add features, corrections, and enhancements.

## Requirements

- It shall regulate water temperature by turning on/off heating element
- It shall allow for setting the temperature range
- It shall be easily moveable
- It shall be installed manually (powering each device individually) - this might change
- it shall turn off when water level is too low

### Power

* How much water? 5 gal. Use the original water feeder.
* What is the easiest thing to do?
  * Power supply
  * Use heater with prebuilt protection circuit (OCP)
 
**Decision**

Use regular 120v for prototype (one outlet) 

### BOM

#### Electical

- 2 power elements (controller and heating element)
- Heating element https://www.amazon.com/gp/product/B0893T67LX/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1
- Thermostat/Sensor
  - DATASHEET: `https://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf`
  - github repo to look at: `https://github.com/matmunk/DS18B20`
  - Determined that -127*C is actuall an error code
  - Determined original setup might have been a bad parameter passed to the pinMode method, regardless added a physical pull up resistor of 5K1 oHms and observered reative tempature readings in serial monitor. Once heated temperature went up, when cooled the temperature went down.
- Rpi/breadboard/resisters/relays/jumpers/etc. (basically a well equiped start kit)
- liquid level sensor (Taidacent Non Contact Liquid Level Sensor) https://a.co/d/iqHP8Fy

- LED COLORS
  - green: system on
  - red: heat on
  - blue: cold (maybe not going to use)
  - yellow: warm
  - white: low water

#### Mechanical

- 5 gallon bucket (we have plenty around, cheap, easy to get)
- brackets/general hardware

# TODO

1. Calibrate temperature sensor within a few degrees

#### Development Tools
- EveryCircuit
- MultiSim
