#!/usr/bin/env python
# coding: utf-8

# In[3]:


def computer_guess(number):
    '''Используется классический алгоритм бинарного поиска. Функция принимает в качестве аргумента загаданное 
       пользователем число в диапазоне от 1 до 100, а алгоритм отгадывает его за минимальное количество попыток. 
       
       Каждое предложенное в качестве отгадки число - медиана все сокращающегося диапазона в зависимости от того, 
       меньше или больше отгадка по сранению с загаданным числом.
    '''
    lower_bond = 1   #Нижняя граница изначального диапазона.
    upper_bond = 100   #Верхняя граница изначального диапазона.
    guess = 50   #Первоначальная отгадка.
    count = 0   #Счетчик количества попыток.
    
    if number<1 or number>100:
        print("The number must be in range [1, 100]")
    else:
        while guess != number:
            count +=1
            guess = (lower_bond+upper_bond)//2  #Шаблон для выдачи отгадки.
            print("Computer's guess is...", guess)
        
            #Постепенное сокращение диапазона (границ) отгадки.
            if guess > number:
                upper_bond = guess
            elif guess < number:
                lower_bond = guess + 1

        print('The computer guessed', guess, 'in only', count, 'attempts!')
        
#computer_guess()

