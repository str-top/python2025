import random

secr_num = random.randint(1, 100)    

att = 0  
max_att = 10                                                                      
answer = ''
print("Привет, хочешь, поиграть в угадай число?") 
while answer.lower() != 'да' and  answer.lower() != 'нет':
    answer = input('напиши "да" или "нет"')
if answer.lower() == 'да':
    print(f"У тебя есть {max_att} попыток, чтобы угадать число от 1 до 100.")
    
    while att < max_att:                                                         
        quess = input("Введи число (или 'выход' для завершения): ")            
        if quess.lower() == 'выход':                                                        
            print("Эх,ты был так близок:", secret_number)
            break                                                                           
        
        if not quess.isdigit():                                                            
            print("Ошибка! Пожалуйста, введите число.")
            continue                                                                    
    
        quess = int(quess)
        att += 1                                                                      
        if quess == secr_num:                                                          
            print(f"Ура! Ты выйграл за {att} попыток, загаданное число: {secr_num}.")  
            break                                                                           
        elif quess < secr_num:
            print("Как то маловато, двигайся в большую сторону.")
        else:                                                                              
            print("как то многовато, попробуй шо нибудь поменьше.")
        
        if att == max_att:                                                       
            print(f"За все {max_att} попыток(ки) ты не смог угадать,ты меня расстроил! загаданное число было:", secr_num)
    else:
        
        print("На этом все, удачи в следующих разах!")
        
else:
    print('очень жаль, пока(')

    
