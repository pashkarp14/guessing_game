from random import *
print('Добро пожаловать в числовую угадайку')
play=True
while play:
    co=0
    print('Введите диапазон чисел') 
    while True:    
        m, n = input(), input()
        if m.isdigit()==True and n.isdigit()==True and int(m)<int(n):
            e=int(m)
            f=int(n)
            break
        else:
            print('Укажите два целых числа, меньшее и большее')
    def is_valid(b):
        return str(b).isdigit() and e<=int(b)<=f
    print('Попробуйте угадать число от', e, 'до', f)
    a = randint(e,f)
    while True:
        n = input()
        if is_valid(n)==True:
            n=int(n)
            if n>a:
                print('Слишком много, попробуйте еще раз')
                co+=1
            elif n<a:
                print('Слишком мало, попробуйте еще раз')
                co+=1
            elif n==a:
                print('Поздравляем, вы угадали')
                print('Вам потребовалось', co, 'попыток')
                break
        else:
            print('А может быть все-таки введем целое число от', e, 'до', f,'?')
    print('Сыграем еще разок? да\нет')
    play = input()
    if play.lower()=='да':
        play = True
        print('Отлчно! Новая игра!')
    else:
        play = False
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
