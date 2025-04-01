def calculate_discount(price, discount_percent): # creating a function with two parameters
    if discount_percent >= 20: # the disount percent is greater than or equal to 20
        # calculating the discount amount
        discount_amount = (price * discount_percent) / 100
        final_discount_price = price - discount_amount
        # return the final discount price
        return final_discount_price
    else:
        return price # return the original price
# the prompt is asking for the original price
price = float(input("Enter the original price: "))
# the prompt is asking for the discount percent
discount_percent = float(input("Enter the percentage discount: "))
# calling the function and storing the result in final_price
final_price = calculate_discount(price, discount_percent)
