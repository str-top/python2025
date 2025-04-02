def calculate_discount(price, discount=10):
    if discount == 100:
        return print('вы заберете данный товар за 0 рублей')
    else:
        itog = price - (price / 100 * discount)
        return print(f'вы заберете данный товар со скидкой: {discount}% за {itog} рублей')


price_inp = int(input('введите цену на товар'))
discount_inp = input('введите размер скидки на этот товар')

try:
    discount_inp = int(discount_inp)
    calculate_discount(price_inp, discount_inp)
except ValueError:
    print('вы не ввели размер скидки, по этому она будет состоять 10%')
    calculate_discount(price_inp)
