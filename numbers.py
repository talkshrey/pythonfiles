myDict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
myDict2 = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def individual_digits(num):
    first_digit = int(num / 100)
    two_digit = int(num % 100)
    second_digit = int(two_digit / 10)
    third_digit = int(two_digit % 10)

    if first_digit == 0:
        if second_digit > 0:
            two_digit_word = myDict2.get(second_digit) + " " + myDict.get(third_digit)
            return two_digit_word
        else:
            third_digit_word = myDict.get(third_digit)
            return third_digit_word
    elif second_digit == 0 and third_digit == 0:
        first_word = myDict.get(first_digit)
        return first_word + " hundred"
    elif second_digit == 0 and third_digit != 0:
        first_word = myDict.get(first_digit)
        third_digit_word = myDict.get(third_digit)
        return first_word + " hundred and " + third_digit_word

    elif second_digit != 0 and third_digit == 0:
        first_word = myDict.get(first_digit)
        two_digit_word = myDict2.get(second_digit)
        return first_word + " hundred and " + two_digit_word

    else:
        first_word = myDict.get(first_digit)
        two_digit_word = myDict2.get(second_digit) + " " + myDict.get(third_digit)
        return first_word + " hundred and " + two_digit_word


x = int(input("enter any num between 1 to 1000: "))
if 1 <= x < 1000:
    print(individual_digits(x))
else:
    print("invalid input")
