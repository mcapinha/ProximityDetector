# ProximityDetector #
A proximity detector with a Raspberry Pi, HC-SR04 proximity detector and some Python

![Alt text](diagram.png?raw=true "Diagram")

## Description ##

Using a Raspberry Pi, a HC-SR04, three resitors, one led and some Python, create a simple proximity and presence detector.


## How it works ##

[A good introduction to the HC-SR04](https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/)

Using the Raspberry, we connect to the HC-SR04 and periodically poll it to determine the distance to any object in front of it.

If there's an object nearer than 150cm (configurable), blink a led!

## But why ?? ##
My kids love watching TV from 50cm away and I've given up asking them to move up.

Next step (if the led is not deterrent enough) is [Home Assistant](https://www.home-assistant.io/) integration, to actually turn of the TV!