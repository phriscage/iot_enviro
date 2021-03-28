# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position
"""
    This sample app will read all the Pinmoroni envirophat sensors for a given 
    time interval and write to a specified output. 

    https://shop.pimoroni.com/products/enviro-phat

    Enviro pHAT includes:
    
    An LSM303D accelerometer/magnetometer for detecting orientation, motion and heading
    A BMP280 temperature/pressure sensor
    A TCS3472 colour sensor, for detecting the amount and colour of light
    An ADS1015 analog sensor with four 3.3v tolerant channels for your external sensors
    A 5v power supply pin for powering your sensors, which you can regulate or divide to 3v if needed
    Two LEDs connected to GPIO #4 for illuminating objects over the colour sensor
"""

import sys
import time
from collections import defaultdict
import json
from datetime import datetime
import logging

from envirophat import light, weather, motion, analog, leds

logger = logging.getLogger(__name__)

SLEEP_SECONDS = 1


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

""" get the data from the envirophat """
def _get_data():
    light_values = {
        'sensor_type': 'TCS3472',
        'level': light.light(),
        **dict(zip(["red", "green", "blue"], light.rgb())) 
    }
    weather_values = {
        'sensor_type': 'BMP280', 
        'altitude': weather.altitude(), # meters
        'pressure': round(weather.pressure("Pa"), 2), # pascals
        'temperature': round(weather.temperature(), 2) # celcius
    }
    motion_values = { 
        'sensor_type': 'LSM303D',
        **dict(zip(["acceleration_x", "acceleration_y", "acceleration_z"], 
            [round(x, 2) for x in motion.accelerometer()])), # x, y and z acceleration as a vector in Gs.
        'heading': motion.heading(),
        **dict(zip(["magnetic_field_x", "magnetic_field_y", "magnetic_field_z"], motion.magnetometer())) # raw x, y and z magnetic readings as a vector.

    }
    analog_values = { 
        'sensor_type': 'ADS1015',
        **{"channel_%i" % k:v for k, v in enumerate(analog.read_all())}
    }
    data = {
        'created_at': datetime.utcnow().isoformat() + 'Z',
        'light':light_values,
        'weather': weather_values,
        'motion': motion_values,
        'analog': analog_values
    }
    return data

""" main """
def main():
    logger.info("Starting")
    try:
        while True:
            leds.on()
            logger.debug("Getting data...")
            data = _get_data()
            write(json.dumps(data) + '\n')
            #sys.stdout.write(json.dumps(data) + '\n')
            leds.off()
            logger.debug("Waiting %s seconds" % SLEEP_SECONDS)
            time.sleep(SLEEP_SECONDS)
    except KeyboardInterrupt:
        logger.warning("KeyboardInterrupt")
        pass
    logger.info("Finished.")

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
        format=("%(asctime)s %(levelname)s %(name)s[%(process)s] : %(funcName)s"
                " : %(message)s"),
    )
    main()
