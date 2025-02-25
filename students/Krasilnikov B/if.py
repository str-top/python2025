liters=int(input('сколько литров взять?'))

if liters>0:
	print('число введено корректно')

if liters<5:
	print('это норм')
elif liters<10:
	print('не многовато?')
else:
	print('не,я пас')

