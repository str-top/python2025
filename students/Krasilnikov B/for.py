friends = ['Самат','Тагир','Данил','Некит']

for friend in friends:
	if friend.lower()=='самат':
		continue
	elif friend.lower()=='некит':
		break
	else:
		print(friend + ', Привет!')
print('цикл завершен')



