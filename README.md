# IoT-Project
Smart Irrigation System
The Smart Irrigation System is a project that uses a Raspberry Pi, a soil moisture sensor, and a water pump to automate the process of watering plants. The system continuously monitors the soil moisture level and turns the water pump on or off to keep the soil moist.

Getting Started
To set up the Smart Irrigation System, you will need the following components:

Raspberry Pi (any model)
Soil moisture sensor
Water pump
Jumper wires
Breadboard
Connect the soil moisture sensor and water pump to the Raspberry Pi as follows:

Connect the VCC pin of the soil moisture sensor to a 5V pin on the Raspberry Pi
Connect the GND pin of the soil moisture sensor to a GND pin on the Raspberry Pi
Connect the analog output pin of the soil moisture sensor to an analog input pin on the Raspberry Pi (e.g. pin 18)
Connect the positive wire of the water pump to a GPIO pin on the Raspberry Pi (e.g. pin 17)
Connect the negative wire of the water pump to a GND pin on the Raspberry Pi
Install the required Python libraries by running the following command:

Code
pip install gpiozero flask
Clone or download the repository and run the following command to start the Flask web application:

Code
python app.py
Access the web interface by navigating to http://localhost:5000 in your web browser.

Usage
The Smart Irrigation System will automatically turn the water pump on or off based on the soil moisture level. The web interface displays the current soil moisture level and allows users to turn the water pump on or off manually.

Contributing
Contributions to the Smart Irrigation System project are welcome! Please fork the repository and submit a pull request with your changes.
