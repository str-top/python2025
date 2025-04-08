def calculate_discount(price, discount=10):
    if discount == 100:
        return print('вы приобретете данный товар за 0 рублей')
    else:
        itog = price - (price / 100 * discount)
        return print(f'вы приобретете данный товар со скидкой: {discount}% за {itog} рублей')
      
product_price = int(input('введите цену товара'))
discount_inp =  int(input('введите размер скидки на этот товар'))

try:
    calculate_discount(product_price, discount_inp)
except ValueError:
    print('вы не ввели размер скидки, по этому она будет состоять 10%')
    calculate_discount(product_price)
