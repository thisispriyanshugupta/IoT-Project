from flask import Flask, render_template, request
from gpiozero import OutputDevice
from time import sleep

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

# Use the PiGPIOFactory with the address of the Raspberry Pi
pi_address = '192.168.1.10'  # Replace with the IP address of your Raspberry Pi
pin_factory = PiGPIOFactory(host=pi_address)
led = LED(17, pin_factory=pin_factory)

# Define the GPIO pins connected to the water pump and soil moisture sensor
pump_pin = 17
sensor_pin = 18

# Set up the water pump as an OutputDevice and turn it off initially
pump = OutputDevice(pump_pin)
pump.off()

# Define a function to read the soil moisture level from the sensor
def read_soil_moisture():
    # Read the analog value from the soil moisture sensor
    # Convert the value to a moisture level (0-100%)
    # Return the moisture level as an integer
    return int(100 * (1 - (analog_value / 1023)))

# Define the Flask web application
app = Flask(_name_)

# Define a route to display the sensor data and allow users to control the water pump
@app.route("/", methods=["GET", "POST"])
def index():
    # Read the soil moisture level from the sensor
    moisture_level = read_soil_moisture()

    # Handle POST requests to turn the water pump on or off
    if request.method == "POST":
        if "on" in request.form:
            pump.on()
        elif "off" in request.form:
            pump.off()

    # Render the template with the sensor data and control form
    return render_template("index.html", moisture_level=moisture_level)

# Define a loop to continuously monitor the soil moisture level and turn the water pump on or off
while True:
    # Read the soil moisture level from the sensor
    moisture_level = read_soil_moisture()

    # Check if the moisture level is below a certain threshold
    if moisture_level < 50:
        # If the moisture level is low, turn on the water pump
        pump.on()
    else:
        # If the moisture level is high enough, turn off the water pump
        pump.off()

    # Sleep for a short time to avoid excessive polling
    sleep(1)

# Start the Flask web application
if _name_ == "_main_":
    app.run(debug=True)
