import random

'''
###
#  
###
  #
###
цифра 5
'''

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

'''
этапы нейросети

подготовка данных
выбор архитектуры CNN RNN
тренировка модели
проверка модели
'''

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
neirons = 15  # 15 нейронов, потому что сетка квадратов для цифр 3х5
cifra = 5  # тренируем нейросеть распознавать цифру 5
weights = []  # обнуляем веса
for i in range(neirons):
    weights.append(0)


def opredelenie(mas):
    summa = 0
    porog = 7
    for i in range(neirons):
        summa += int(mas[i])*weights[i]
    if summa > porog:
        return True
    else:
        return False

# получает цифру на вход
def plus(mas): # нейронка угадала цифру и увеличивает вес закрашенных квадратиков
    for i in range(neirons):
        if int(mas[i]) == 1:
            weights[i] += 1


def minus(mas): # нейронка не угадала цифру и уменьшает вес закрашенных квадратиков
    for i in range(neirons):
        if int(mas[i]) == 1:
            weights[i] -= 1


# тренировка сети
n = 1000
for i in range(n):
    rnd = random.randint(0, 9)
    res = opredelenie(nums[rnd])
    # if rnd == cifra:
    #     if res:
    #         plus(nums[rnd])
    # else:
    #     if not res:
    #         minus(nums[rnd])
    if rnd == cifra:
        if not res:
            plus(nums[rnd])
    if rnd != cifra:
        if res:
            minus(nums[rnd])


for n, w in enumerate(weights):
    print(w, end='\t')
    if (n+1) % 3 == 0:
        print('')


# проверка работы программы на обучающей выборке

print("0 это 5? ", opredelenie(num0))
print("1 это 5? ", opredelenie(num1))
print("2 это 5? ", opredelenie(num2))
print("3 это 5? ", opredelenie(num3))
print("4 это 5? ", opredelenie(num4))
print("5 это 5? ", opredelenie(num5))
print("6 это 5? ", opredelenie(num6))
print("7 это 5? ", opredelenie(num7))
print("8 это 5? ", opredelenie(num8))
print("9 это 5? ", opredelenie(num9))