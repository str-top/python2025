def calculate_discount(price, discount=10):
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
    
    discount_amount = (discount / 100) * price
    final_price = price - discount_amount
    
    return final_price

original_price = 1000
final_price = calculate_discount(original_price, discount=20)
print(f"Итоговая цена после скидки: {final_price} рублей")
