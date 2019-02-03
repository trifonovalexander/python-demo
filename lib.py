def cashback(monthly_expenses): # объявление, выше вызывать нельзя
    # отступ внутри обязателен
    '''
    >>> cashback(10_000)
    300.0
    '''
    percent = 3
    result = percent * monthly_expenses / 100
    return result # return - возврат значения

def index_body_weight(weight, height):
    result = weight / (height ** 2)
    return result
print(index_body_weight(75, 185))

def bmi (weigth, height) : # shift + f6 - замена имени, зашиваем все входные параметры вверху, ниже просто ставим необходимые данные
    '''
    >>> bmi (106 , 1.8) # doctest: +ELLIPSIS (когда не нужно проверять все все числа, выделяем 2 цифры после запятой)
    32.71...
    '''
    result = weigth / (height * height)
    return result
print(bmi(106, 1.8))
bmi(106, 1.8)

