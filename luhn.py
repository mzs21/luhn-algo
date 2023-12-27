def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] # Reversing the card_number. [(start value) : (end value) : (step)]
    odd_digits = card_number_reversed[::2] # Assigning the odd digits from card_number_reversed

    for digit in odd_digits:  # Looping through all the odd_digits
        sum_of_odd_digits += int(digit) # Adding each digit

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2] # Assigning the even digits from card_number_reversed

    for digit in even_digits:
        number = int(digit) * 2 # Double the value of every digit

        if number >= 10:  # To prevent the multiplication of one digit from being greater than 9, we need to check if the product (value of number) is greater than or equal to 10

            number = (number // 10) + (number % 10) #  sum the digits of the products

        sum_of_even_digits += number # Adding each number

    total = sum_of_odd_digits + sum_of_even_digits
    
    return total % 10 == 0 # If the sum of all the digits (total) is a multiple of 10, then the number is valid; else it is not valid.

def main(cardNumber):
    card_number =  cardNumber 

    card_translation = str.maketrans({'-': '', ' ': ''}) # Replacing the LHS values with RHS values (if exist)

    translated_card_number = card_number.translate(card_translation) 

    if verify_card_number(translated_card_number): # If the function return 'True'
        print('VALID!')
    else:
        print('INVALID!')


cardNumber = input('Enter the card number: ')

# '4111-1111-4555-1142'  (Valid)
# '4111-1111-4555-1141' (Invalid)

main(cardNumber)