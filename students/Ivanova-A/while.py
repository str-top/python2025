chislo = int(input('Введите число'))
while chislo < 5:
  chislo+=1 
  if chislo == 2:
    continue
  elif chislo == 6:
    break
  else:
    print(chislo)
