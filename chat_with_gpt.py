def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    if n == 0:
        return "zero"

    words = ""

    if n >= 1000:
        words += ones[n // 1000] + " thousand "
        n %= 1000

    if n >= 100:
        words += ones[n // 100] + " hundred "
        n %= 100
        if n > 0:
            words += "and "

    if n >= 20:
        words += tens[n // 10] + " "
        n %= 10

    if n >= 11 and n <= 19:
        words += teens[n - 10] + " "
        n = 0

    if n == 10 or n == 20:
        words += tens[n // 10] + " "
        n = 0

    if n > 0:
        words += ones[n]

    return words.strip()


def count_letters_in_range(start, end):
    total_letters = 0
    for number in range(start, end + 1):
        words = number_to_words(number)
        words_no_spaces = words.replace(" ", "").replace("-", "")
        total_letters += len(words_no_spaces)
    return total_letters


total_letters = count_letters_in_range(1, 10000)
print(total_letters)