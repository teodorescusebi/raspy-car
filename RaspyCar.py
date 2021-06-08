from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time
import thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)  # lights
GPIO.setup(3,GPIO.OUT)  # break lights
GPIO.setup(4,GPIO.OUT)  # revers light
GPIO.setup(23,GPIO.OUT) #left blinker
GPIO.setup(24,GPIO.OUT) # right blinker

leftBlinker = 312
isLeftBlinking = False
rightBlinker = 313
isRightBlinking = False
lights = 307

breakLightsOff = 128
currentSpeed = 0
forward = [0, 127]

backward = [129, 255]

blinkersOff = 128
left = [0, 127]
right = [129, 255]


connected = False

def lightsFunction():
	if GPIO.input(2):
		GPIO.output(2,GPIO.LOW)
	else:
		GPIO.output(2,GPIO.HIGH)

def breakLightsOnFunction():
	GPIO.output(3, GPIO.HIGH)

def breakLightsOffFunction():
	GPIO.output(3, GPIO.LOW)

def reverseLightFunctionOn():
	GPIO.output(4, GPIO.HIGH)

def reverseLightFunctionOff():
	GPIO.output(4, GPIO.LOW)

def leftBlinkerFunction():
	if GPIO.input(23):
		GPIO.output(23, GPIO.LOW)
	else:
		GPIO.output(23, GPIO.HIGH)

def leftFlicker():
	while isLeftBlinking:
		leftBlinkerFunction()
		time.sleep(0.5)
		leftBlinkerFunction()
		time.sleep(0.5)

def rightBlinkerFunction():
	if GPIO.input(24):
		GPIO.output(24, GPIO.LOW)
	else:
		GPIO.output(24, GPIO.HIGH)

def rightFlicker():
	while isRightBlinking:
		rightBlinkerFunction()
		time.sleep(0.5)
		rightBlinkerFunction()
		time.sleep(0.5)


while not connected:
	try:
		gamepad = InputDevice('/dev/input/event7')
		connected = True
		print ("Controller connected!")

		for event in gamepad.read_loop():
			if event.type == 1 and event.value == 1:
				if event.code == lights:
					print("Lights controll")
					lightsFunction()

				elif event.code == leftBlinker:
					print("Left blinker controll")
					if isLeftBlinking:
						isLeftBlinking = False
					else:
						isLeftBlinking = True
						thread.start_new_thread(leftFlicker, ())

				elif event.code == rightBlinker:
					print("Right blinker controll")
					if isRightBlinking:
						isRightBlinking = False
					else:
						isRightBlinking = True
						thread.start_new_thread(rightFlicker, ())

			elif event.type == 3:
				if event.code == 0 or event.code == 1:
					if forward[0] <= event.value <= forward[1]:
						print("Going forward")
						if event.value < currentSpeed:
							breakLightsOnFunction()
						else:
							breakLightsOffFunction()
						currentSpeed = event.value

					elif event.value == breakLightsOff:
						print("Stop")
						breakLightsOffFunction()
						reverseLightFunctionOff()

					elif backward[0] <= event.value <= backward[1]:
						print("Going backwars")
						reverseLightFunctionOn()

				elif event.code == 2 or event.code == 5:
						if left[0] <= event.value <= left[1]:
							print("Going left")

						elif event.value == blinkersOff:
							isRightBlinking = False
							isLeftBlinking = False

						elif right[0] <= event.value <= right[1]:
							print("Going right")


	except IOError as e:
		connected = False
		print("Waiting for controller...")
		time.sleep(3)
	except OSError as e:
		connected = False
		print("Waiting for controller...")
		time.sleep(3)