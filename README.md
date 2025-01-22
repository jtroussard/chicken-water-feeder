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
- Rpi/breadboard/resisters/relays/jumpers/etc. (basically a well equiped start kit)
- float sensor (switch or capacitive)

#### Mechanical

- 5 gallon bucket (we have plenty around, cheap, easy to get)
- brackets/general hardware
- float apparatus 

#### Development Tools
- EveryCircuit
- MultiSim
