x = int(input('введи число'))
y=0

while y<x:
	x+=1
	if x==5:
		print('пропуск итерации на числе(цифре) '+ str(x))
		continue
	if x==8:
		print('остановка итераций на числе(цифре)  '+str(x) )
		break
else:
	print('цикл завершен')
print('цикл завершен полностью')

