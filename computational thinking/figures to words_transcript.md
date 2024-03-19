**_give code for the following problem: convert figures to words_**

Certainly! Here's an example code in Python that converts figures (numbers) into words:

python

    # Define lists for number words
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    # Function to convert a number less than 1000 to words
    def num_to_words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
        elif num < 1000:
            return ones[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + num_to_words(num % 100))
        else:
            return 'Number out of range'

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                num = int(input("Enter a number (0 to exit): "))
                if num == 0:
                    break
                elif num < 0 or num > 999:
                    print("Number out of range")
                else:
                    words = num_to_words(num)
                    print(f'{num} in words is "{words}"')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code defines a function `num_to_words` that converts a given number into words up to 999. It also includes a main program loop where you can input numbers to convert them into words until you input `0` to exit the program.

\
\


**_this code is considering numbers only in the range 0 to 999, modify the code so that it works even for very large numbers correctly_**

To handle very large numbers correctly and convert them into words, you can modify the code to support numbers beyond the range of 0 to 999. Here's an updated version of the code that can convert numbers up to trillions (10^12) into words:

python

    # Define lists for number words
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    # Function to convert a number less than 1000 to words
    def num_to_words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
        elif num < 1000:
            return ones[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + num_to_words(num % 100))
        else:
            for i, suffix in enumerate(suffixes):
                if num < 1000 ** (i + 1):
                    return num_to_words(num // (1000 ** i)) + ' ' + suffix + ('' if num % (1000 ** i) == 0 else ', ' + num_to_words(num % (1000 ** i)))

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                num = int(input("Enter a number (0 to exit): "))
                if num == 0:
                    break
                words = num_to_words(abs(num))
                if num < 0:
                    words = 'Minus ' + words
                print(f'{num} in words is "{words}"')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code now includes a `suffixes` list to handle numbers beyond 999. It separates numbers into groups of three digits (thousands, millions, billions, etc.) and appends the corresponding suffixes while converting them into words. It also handles negative numbers by adding the word "Minus" before the converted words if the input number is negative.

\


**_the code works fine but it considers only the western naming system, could you modify it to make it convert even in Indian naming system ?_**

Sure, I can modify the code to convert numbers into words using the Indian numbering system. In the Indian numbering system, numbers are grouped in sets of two digits instead of three as in the Western system. Here's the updated code to convert numbers into words using the Indian numbering system:

python

    # Define lists for number words in Indian numbering system
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes = ['', 'Thousand', 'Lakh', 'Crore', 'Arab', 'Kharab', 'Neel', 'Padma', 'Shankh']

    # Function to convert a number less than 100 to words
    def num_to_words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])

    # Function to convert a number to words using the Indian numbering system
    def indian_num_to_words(num):
        if num == 0:
            return ones[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 2 != 0:
                words.append(num_to_words(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:2])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words(current_num))
                    else:
                        words.append(num_to_words(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words(current_num % 100))

                num_str = num_str[2:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes[num_len // 2])

        return ' '.join(words)

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                num = int(input("Enter a number (0 to exit): "))
                if num == 0:
                    break
                words = indian_num_to_words(abs(num))
                if num < 0:
                    words = 'Minus ' + words
                print(f'{num} in words is "{words}"')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code uses the Indian numbering system suffixes like 'Thousand', 'Lakh', 'Crore', etc., and groups numbers in sets of two digits for conversion. It also handles negative numbers by adding the word "Minus" before the converted words if the input number is negative.

\
\


**_if the conversion is possible in both the systems as per the choice of the user it would be more great, could you modify it that way correctly?_**

Certainly! I can modify the code to allow the user to choose between the Western and Indian numbering systems for number-to-words conversion. Here's the updated code that includes a choice for the user:

python

    # Define lists for number words in both numbering systems
    ones_western = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens_western = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens_western = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes_western = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    ones_indian = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens_indian = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens_indian = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes_indian = ['', 'Thousand', 'Lakh', 'Crore', 'Arab', 'Kharab', 'Neel', 'Padma', 'Shankh']

    # Function to convert a number less than 100 to words (Western system)
    def num_to_words_western(num):
        if num < 10:
            return ones_western[num]
        elif num < 20:
            return teens_western[num - 10]
        elif num < 100:
            return tens_western[num // 10] + ('' if num % 10 == 0 else ' ' + ones_western[num % 10])

    # Function to convert a number less than 100 to words (Indian system)
    def num_to_words_indian(num):
        if num < 10:
            return ones_indian[num]
        elif num < 20:
            return teens_indian[num - 10]
        elif num < 100:
            return tens_indian[num // 10] + ('' if num % 10 == 0 else ' ' + ones_indian[num % 10])

    # Function to convert a number to words using the Western numbering system
    def western_num_to_words(num):
        if num == 0:
            return ones_western[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 3 != 0:
                words.append(num_to_words_western(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:3])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_western(current_num))
                    else:
                        words.append(num_to_words_western(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_western(current_num % 100))

                num_str = num_str[3:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_western[num_len // 3])

        return ' '.join(words)

    # Function to convert a number to words using the Indian numbering system
    def indian_num_to_words(num):
        if num == 0:
            return ones_indian[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 2 != 0:
                words.append(num_to_words_indian(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:2])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_indian(current_num))
                    else:
                        words.append(num_to_words_indian(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_indian(current_num % 100))

                num_str = num_str[2:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_indian[num_len // 2])

        return ' '.join(words)

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                choice = input("Enter 'W' for Western system or 'I' for Indian system (0 to exit): ").strip().upper()
                if choice == '0':
                    break
                elif choice == 'W':
                    num = int(input("Enter a number: "))
                    words = western_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Western system) is "{words}"')
                elif choice == 'I':
                    num = int(input("Enter a number: "))
                    words = indian_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Indian system) is "{words}"')
                else:
                    print("Invalid choice. Please enter 'W' or 'I'.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code now includes two separate functions for converting numbers into words using the Western and Indian numbering systems. The user can choose the system by entering 'W' for the Western system or 'I' for the Indian system. The code then performs the conversion accordingly. It also handles negative numbers and provides the words in the chosen numbering system.

**_just limit the indian suffixes till crore_**

Sure, I'll limit the Indian numbering system suffixes till 'Crore' (10^7). Here's the modified code:

python

    # Define lists for number words in both numbering systems
    ones_western = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens_western = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens_western = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes_western = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    ones_indian = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens_indian = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens_indian = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    suffixes_indian = ['', 'Thousand', 'Lakh', 'Crore']

    # Function to convert a number less than 100 to words (Western system)
    def num_to_words_western(num):
        if num < 10:
            return ones_western[num]
        elif num < 20:
            return teens_western[num - 10]
        elif num < 100:
            return tens_western[num // 10] + ('' if num % 10 == 0 else ' ' + ones_western[num % 10])

    # Function to convert a number less than 100 to words (Indian system)
    def num_to_words_indian(num):
        if num < 10:
            return ones_indian[num]
        elif num < 20:
            return teens_indian[num - 10]
        elif num < 100:
            return tens_indian[num // 10] + ('' if num % 10 == 0 else ' ' + ones_indian[num % 10])

    # Function to convert a number to words using the Western numbering system
    def western_num_to_words(num):
        if num == 0:
            return ones_western[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 3 != 0:
                words.append(num_to_words_western(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:3])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_western(current_num))
                    else:
                        words.append(num_to_words_western(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_western(current_num % 100))

                num_str = num_str[3:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_western[num_len // 3])

        return ' '.join(words)

    # Function to convert a number to words using the Indian numbering system
    def indian_num_to_words(num):
        if num == 0:
            return ones_indian[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 2 != 0:
                words.append(num_to_words_indian(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:2])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_indian(current_num))
                    else:
                        words.append(num_to_words_indian(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_indian(current_num % 100))

                num_str = num_str[2:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_indian[num_len // 2])

        return ' '.join(words)

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                choice = input("Enter 'W' for Western system or 'I' for Indian system (0 to exit): ").strip().upper()
                if choice == '0':
                    break
                elif choice == 'W':
                    num = int(input("Enter a number: "))
                    words = western_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Western system) is "{words}"')
                elif choice == 'I':
                    num = int(input("Enter a number: "))
                    words = indian_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Indian system) is "{words}"')
                else:
                    print("Invalid choice. Please enter 'W' or 'I'.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code limits the Indian numbering system suffixes to 'Thousand', 'Lakh', and 'Crore' (10^7). It allows the user to choose between the Western and Indian systems and handles negative numbers as well.

\


**_since the keys are not contiguous using a dictionary would be better than a list_**

You're correct! Using a dictionary instead of a list for the Indian numbering system suffixes would be a better approach since it allows for non-contiguous keys. Here's the modified code using dictionaries for both Western and Indian numbering systems:

python

    # Define dictionaries for number words in both numbering systems
    ones_western = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    tens_western = {
        0: '', 10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    teens_western = {
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
    }
    suffixes_western = {
        0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'
    }

    ones_indian = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    tens_indian = {
        0: '', 10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    teens_indian = {
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
    }
    suffixes_indian = {
        0: '', 1: 'Thousand', 2: 'Lakh', 3: 'Crore'
    }

    # Function to convert a number less than 100 to words (Western system)
    def num_to_words_western(num):
        if num < 10:
            return ones_western[num]
        elif num < 20:
            return teens_western[num]
        elif num < 100:
            return tens_western[num // 10 * 10] + ('' if num % 10 == 0 else ' ' + ones_western[num % 10])

    # Function to convert a number less than 100 to words (Indian system)
    def num_to_words_indian(num):
        if num < 10:
            return ones_indian[num]
        elif num < 20:
            return teens_indian[num]
        elif num < 100:
            return tens_indian[num // 10 * 10] + ('' if num % 10 == 0 else ' ' + ones_indian[num % 10])

    # Function to convert a number to words using the Western numbering system
    def western_num_to_words(num):
        if num == 0:
            return ones_western[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 3 != 0:
                words.append(num_to_words_western(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:3])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_western(current_num))
                    else:
                        words.append(num_to_words_western(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_western(current_num % 100))

                num_str = num_str[3:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_western[num_len // 3])

        return ' '.join(words)

    # Function to convert a number to words using the Indian numbering system
    def indian_num_to_words(num):
        if num == 0:
            return ones_indian[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 2 != 0:
                words.append(num_to_words_indian(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:2])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words_indian(current_num))
                    else:
                        words.append(num_to_words_indian(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words_indian(current_num % 100))

                num_str = num_str[2:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_indian[num_len // 2])

        return ' '.join(words)

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                choice = input("Enter 'W' for Western system or 'I' for Indian system (0 to exit): ").strip().upper()
                if choice == '0':
                    break
                elif choice == 'W':
                    num = int(input("Enter a number: "))
                    words = western_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Western system) is "{words}"')
                elif choice == 'I':
                    num = int(input("Enter a number: "))
                    words = indian_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Indian system) is "{words}"')
                else:
                    print("Invalid choice. Please enter 'W' or 'I'.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

This code now uses dictionaries for both numbering systems, making the code more efficient and allowing non-contiguous keys for suffixes. The rest of the code remains the same, allowing the user to choose between the Western and Indian systems for number-to-words conversion.

\


**_the ones tens and teens are same in both the systems and defining them twice seems redundant, can you modify that ?_**

Absolutely, you're correct that the definitions for ones, tens, and teens are the same in both the Western and Indian numbering systems. We can define these common dictionaries once and then use them for both systems. Here's the modified code with a shared definition for these dictionaries:

python

    # Define common dictionaries for number words
    ones = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    tens = {
        0: '', 10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    teens = {
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
    }

    # Define specific suffixes for Western and Indian systems
    suffixes_western = {
        0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'
    }
    suffixes_indian = {
        0: '', 1: 'Thousand', 2: 'Lakh', 3: 'Crore'
    }

    # Function to convert a number less than 100 to words
    def num_to_words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num]
        elif num < 100:
            return tens[num // 10 * 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])

    # Function to convert a number to words using the Western numbering system
    def western_num_to_words(num):
        if num == 0:
            return ones[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 3 != 0:
                words.append(num_to_words(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:3])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words(current_num))
                    else:
                        words.append(num_to_words(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words(current_num % 100))

                num_str = num_str[3:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_western[num_len // 3])

        return ' '.join(words)

    # Function to convert a number to words using the Indian numbering system
    def indian_num_to_words(num):
        if num == 0:
            return ones[num]

        words = []
        num_str = str(num)
        num_len = len(num_str)

        while num_len > 0:
            if num_len % 2 != 0:
                words.append(num_to_words(int(num_str[0])))
                num_str = num_str[1:]
            else:
                current_num = int(num_str[:2])
                if current_num != 0:
                    if current_num < 100:
                        words.append(num_to_words(current_num))
                    else:
                        words.append(num_to_words(current_num // 100) + ' Hundred')
                        if current_num % 100 != 0:
                            words.append('and')
                            words.append(num_to_words(current_num % 100))

                num_str = num_str[2:]
            num_len = len(num_str)

            if num_len > 0 and int(num_str) != 0:
                words.append(suffixes_indian[num_len // 2])

        return ' '.join(words)

    # Main program
    if __name__ == '__main__':
        while True:
            try:
                choice = input("Enter 'W' for Western system or 'I' for Indian system (0 to exit): ").strip().upper()
                if choice == '0':
                    break
                elif choice == 'W':
                    num = int(input("Enter a number: "))
                    words = western_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Western system) is "{words}"')
                elif choice == 'I':
                    num = int(input("Enter a number: "))
                    words = indian_num_to_words(abs(num))
                    if num < 0:
                        words = 'Minus ' + words
                    print(f'{num} in words (Indian system) is "{words}"')
                else:
                    print("Invalid choice. Please enter 'W' or 'I'.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

In this code, the dictionaries for ones, tens, and teens are defined only once and then used in both the Western and Indian numbering systems. This reduces redundancy and makes the code more organized. The rest of the code remains the same, allowing the user to choose between the Western and Indian systems for number-to-words conversion
