from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event7')

L1 = 310
L2 = 312

R1 = 311
R2 = 313

X = 307
A = 304
B = 305
Y = 308

Select = 314
Start = 315

DNeutru = 0
DLeft = -1 #(code 16)
DRight = 1 #(code 16)
DUp = -1 #(code 17)
DDown = 1 #(code 17)

LJoystickNeutru = 128
LJoystickUp = 0
LJoystickDown = 255
LJoystickClick = 317

RJoystickNeutru = 128
RJoystickLeft = 0
RJoystickRight = 255
RJoystickClick = 318

print(gamepad)

for event in gamepad.read_loop():
	if event.type == 1 and event.value == 1:
		if event.code == L1:
			print("L1")
		elif event.code == L2:
			print("L2")
		elif event.code == R1:
			print("R1")
		elif event.code == R2:
			print("R2")
		elif event.code == X:
			print("X")
		elif event.code == A:
			print("A")
		elif event.code == B:
			print("B")
		elif event.code == Y:
			print("y")
		elif event.code == Start:
			print("Start")
		elif event.code == Select:
			print("Select")
		elif event.code == LJoystickClick:
			print("LJoystickClick")
		elif event.code == RJoystickClick:
			print("RJoystickClick")

	elif event.type == 3:
		if event.code == 0 or event.code == 1:
			if event.value == LJoystickUp:
				print("LJoystickUp")
			elif event.value == LJoystickDown:
				print("LJoystickDown")
			elif event.value == LJoystickNeutru:
				print("LJoystickNeutru")
		elif event.code == 2 or event.code == 5:
			if event.value == RJoystickRight:
				print("RJoystickRight")
			elif event.value == RJoystickLeft:
				print("RJoystickLeft")
			elif event.value == RJoystickNeutru:
				print("RJoystickNeutru")
		elif event.code == 16:
			if event.value == DLeft:
				print("DLeft")
			elif event.value == DRight:
				print("DRight")
		elif event.code == 17:
			if event.value == DUp:
				print("DUp")
			elif event.value == DDown:
				print("DDown")