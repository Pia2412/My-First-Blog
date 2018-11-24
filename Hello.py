print('Hello, Djangogirls! lol')
if 3<2:
	print('It works!')
else: 
	print('5 ist nicht größer als 2')
name= 'Sonja'
if name== 'Pia':
	print('Hey Pia!')
elif name== 'Sonja':
	print('Hey Sonja!')
else:
	print('Hey anonymous!')

volume=57
if volume<20:
	print("Das ist etwas leise!")
elif 20<= volume < 40:
	print("Das ist gut für Hintergrund-Musik!")
elif 40 <= volume < 60:
	print("Perfekt, ich kann alle Details hören!")
elif 60 <= volume < 80:
	print("Gut für Partys!!!")
elif 80 <= volume < 100:
	print ("Etwas laut!")
else:
	print("Mir tuen meine Ohren weh! :(")

if volume < 20 or volume > 80:
	volume = 50
	print("So ist es besser!")

