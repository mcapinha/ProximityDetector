import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_LED = 23

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

RANGE = 150
ledStatus = False
lastSeen = False

def setLed(status):
    GPIO.output(GPIO_LED, status)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    Stop = StartTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()

            if (dist > RANGE):
                ledStatus = False
                lastSeen = False
            else:
                ledStatus = (not ledStatus)
                if not lastSeen:
                    lastSeen = time.time()

            setLed(ledStatus)

            print ("Measured Distance = %.1f cm" % dist)
            if lastSeen:
                print ("Since %d seconds ago" % (time.time()-lastSeen) )
                time.sleep(1)

    #Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()