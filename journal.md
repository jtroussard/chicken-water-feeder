# ENTRY DATE: 03/19/2024

**Summary**

Today we converted the system from Ardunio to the Rpi platform. Using Rpi 3B+ we rewired the system and used chatgpt to quickly convert our code.
The code is still very simple, as it is just a single run file. We needed to go into the Rpi settings and enable a '1-wire' communication protocal,
which appears to be linked by default to the GPIO4 pin. Once we ran the system we observed the temperature outout values on the terminal and used a 
glass of ice water to cool the temperature prob and observe the temperature readings drop. Like the value outputs the leds behaved as expceted as
well, when the temperature threshold was broken (below 22*C) the red led turned on and the green shut off, the opposite occured once the the sensor
readings reached above the threshold. Christopher also prototyped the relay connection, and tested it out. While we will still need to figure out how
to build our own cusotm circuit for the relay and heater, we know in theory what the circuit should look like.

![IMG_4348](https://github.com/user-attachments/assets/3d8a8067-8ae3-4166-85b8-093a26e762b8)
![IMG_4350](https://github.com/user-attachments/assets/6628b013-ab87-40b8-a55a-e2ba16c61734)
![IMG_4351](https://github.com/user-attachments/assets/69cc86b7-c9b1-447a-afc1-defc1ab65a59)
![IMG_4352](https://github.com/user-attachments/assets/5527a959-f5ae-42f9-b438-6b69ee56d880)
![IMG_4353](https://github.com/user-attachments/assets/8f44e0b6-b722-4625-a273-3787c6522b7f)
![IMG_4354](https://github.com/user-attachments/assets/81f414fd-5501-45c6-9a9d-24bf0ca6754f)

![0D8C2F1E-F0F0-4489-BF85-1A64124DB752_1_105_c](https://github.com/user-attachments/assets/970e1b68-39f1-4dff-b1a8-3e5232c1e49f)

**Next Steps**

We discussed our plans for the next few meetings.

**Pre-meeting**

- gather necessary items to build our custom high voltage circuit
  - two prong wall socket
  - two prong electrical cord plug replacement
  - wire connectors (twist caps?)
- build a dashboard for the Rpi and simplify sharing the output

**04/03/2025**

- build the high voltage circuit
- verify high voltage circuit
- install high voltage circuit to the system
- test the complete prototype

**04/17/2025**

- Document the prototype thoroughly
- Shelf the prototype
- Design the production unit
  - shopping list
    - electrical
    - mechanical/hardware
  - rough draft skematics
 
Then the plan is to in our free time perfect the design/skematics before we are able to meet in person and undertake the final production build, concluding this project.

---

# ENTRY DATE: 2025-02-04

**Summary**  

We worked on setting up the temperature sensor with the Arduino and troubleshooting inaccurate sensor readings.

Key points from today’s session:
- Tested various wiring configurations to resolve issues.
- Switched the data pin from **10** to **2** on the Arduino for better results.
- Reviewed the sensor datasheet to double-check wiring and signal expectations.
- Encountered extreme and incorrect temperature readings (**-127°C**), likely caused by wiring or connection issues.

**Next Steps**  

We identified several next steps to resolve the sensor issues and improve reliability:
- Purchase **alligator clips** to improve sensor connections.
- Test manually adding a **pull-up resistor** to stabilize the data line.
- Re-verify the sensor wiring to confirm proper connections.
- Add **error handling** logic to the Arduino sketch to catch invalid readings.
- Finalize sensor wiring, resolve erroneous readings, and advance the Arduino sketch.

**Tasks**  

- **Jacques**: Acquire alligator clips and test the manual pull-up resistor setup.
- **Both**: Schedule the next meeting in two weeks for an extended troubleshooting session.

---

# ENTRY DATE: 2025-01-21

**Summary**  

We focused on connecting the DS18B20 temperature sensor to the Raspberry Pi and outlining the next development steps.

Key discussion points:
- Explored how the DS18B20 sensor integrates with the Raspberry Pi.
- Reviewed potential LED setups for status indication.
- Walked through the existing GitHub repository and example code.
- Examined the DS18B20 datasheet to understand signal behavior and output.
- Considered leveraging an Arduino library for sensor integration reference.

**Next Steps**  

The following tasks were outlined to prepare for the next meeting:
- Set up LED colors for status indication and document this on GitHub.
- Research and document proper DS18B20 wiring and connection to the Raspberry Pi.
- Test the DS18B20 sensor with the Raspberry Pi to verify signal output.
- Add the DS18B20 datasheet link to the GitHub repo for reference.
- Locate and add the GitHub repository link for a compatible DS18B20 Arduino library.
- Determine and document proper resistor values for the LEDs.
- Begin drafting the initial code for reading the temperature sensor and controlling the LEDs.
- Complete DS18B20 testing and start building out the control logic.

---

# ENTRY DATE: 2025-01-07

**Summary**  

We kicked off the Chicken Water Feeder project. The goal is to create a feeder system that prevents water from freezing.  

Key points from today’s discussion and planning:
- Created the GitHub repository for project management.
- Defined initial requirements:
  - Use a 5-gallon bucket as the main container.
  - Integrate a pre-built aquarium heater.
  - Ensure the system plugs into a standard 120V outlet.
  - Use a Raspberry Pi for control and automation.
- Discussed design elements:
  - Include temperature sensors to monitor water temperature.
  - Add LEDs to indicate system status.
  - Account for the non-linear readings typical of temperature sensors.
- Decided to start simple with a prototype:
  - Use LEDs to simulate the heating element for initial testing.

**Next Steps**  

We set individual action items to prepare for prototype development:
- **Jacques**:
  - Create a GitHub organization for better project tracking.
  - Provide specifications for the aquarium heater.
  - Set up the simulation environment.
- **Christopher**:
  - Review the GitHub setup.
  - Research temperature sensors best suited for the application.
  - Start drafting a schematic using the simulator.
  - Review research and schematic progress, finalize component choices for the prototype build.
