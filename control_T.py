from sensor_T import *
import time

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

relayPin = 26
gpio.setup(relayPin, gpio.OUT)

sT = sensor_T(None)
T = sT.read()
print(T)

gpio.output(relayPin, gpio.HIGH)
l_on = True
time.sleep(2)

statusFile = "status.log"
dataFile = "data.log"

status = {
    'maxT': 100,
    'minT': 99.5,
    'dt': 5,
    'log_dt': 60,
    'post_dt': 300,
    'start_t': time.time()
}

# data = {
#     t: [],
#     T: [],
#     on: []
# }

last_log = -1

while True:
    T = sT.read()
    TF = (T *9/5)+32
    print(T, TF, TF > 99.5)

    if (TF < 99.5):
        #print("less than 99.5")
        gpio.output(relayPin, gpio.HIGH)
        l_on = True
    if (TF > 100):
        #print("more than")
        gpio.output(relayPin, gpio.LOW)
        l_on = False


    # write data to file
    run_t = round(time.time() - status["start_t"], 2)
    log_n = int(run_t / status["log_dt"])

    if log_n > last_log:
        now = time.time()
        with open(dataFile, "a") as df:
            df.write(f'{now},{run_t},{T},{l_on}\n')

        last_log = log_n


    time.sleep(status["dt"])
