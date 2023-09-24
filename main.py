# print("Project start")

"""
У всіх завданнях використовувати обробку винятків

1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

3. Користувач вводить два числа та матем дію: + - * або /

Залежно від введеної матем дії вивести результат
"""
task_n = 1

while task_n !=4:
    try:
            task_n = int(input("##################################################\n"
                        "Select please task number, that you want to check: \n"
                        "\t1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.\n"
                        "\t2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання\n"
                        "\t3. Користувач вводить два числа та матем дію: + - * або /\n"
                        "\t4. Stop checking tasks\n"
                        "Enter choise here: "))

            match task_n:
                case 1:
                    try:
                        num_t1 = int(input("Enter please day number per week to show it's name: "))

                        match num_t1:
                            case 1:
                                print("\tThis is Monday!")
                            case 2:
                                print("\tThis is Tuesday!")
                            case 3:
                                print("\tThis is Wednesday!")
                            case 4:
                                print("\tThis is Thursday!")
                            case 5:
                                print("\tThis is Friday!")
                            case 6:
                                print("\tThis is Saturday!")
                            case 7:
                                print("\tThis is Sunday!")
                            case _:
                                raise Exception("Please enter a valid day number!")
                    except ValueError as e:
                        print("\tError: Please enter only integers!")
                    except Exception as e:
                        print(f"\tError: {e}")
                case 2:
                    try:
                        num1_t2 = float(input("Enter please first number: "))
                        num2_t2 = float(input("Enter please second number: "))

                        if num1_t2 == num2_t2:
                            print("\tNumbers are equal.")
                        else:
                            if num1_t2 > num2_t2:
                                print(f"\tHere is the bigger number: {num1_t2}. Do what you need with this information, Neo!")
                            else:
                                print(f"\tHere is the bigger number: {num2_t2}. Do what you need with this information, Neo!")
                    except ValueError as e:
                        print("\tError: Please enter only numbers!")
                case 3:
                    try:
                        num1_t3 = float(input("Enter please first number: "))
                        num2_t3 = float(input("Enter please second number: "))
                        action_t3 = input("Select action, that you want to do with these number (+, -, * or /): ")

                        match action_t3:
                            case "+":
                                print("\tSum of two numbers: "+ str(num1_t3 + num2_t3))
                            case "-":
                                print("\tSubtraction of two numbers: " + str(num1_t3 - num2_t3))
                            case "*":
                                print("\tMultiplying of two numbers: " + str(num1_t3 * num2_t3))
                            case "/":
                                print("\tDividing of two numbers: " + str(num1_t3 / num2_t3))
                            case _:
                                raise Exception("Please enter a valid action!")
                    except ValueError as e:
                        print("\tError: Please enter only numbers!")
                    except ZeroDivisionError as e:
                        print("\tError: We can't divide by 0.")
                    except Exception as e:
                        print(f"\tError: {e}")
                case 4:
                    print("\tThanks for your time!")
                    break
                case _:
                    raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")