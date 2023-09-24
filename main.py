# print("Project start")

"""
У всіх завданнях використовувати обробку винятків

1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

3. Користувач вводить два числа та матем дію: + - * або /

Залежно від введеної матем дії вивести результат
"""
task_n = 1

while task_n == 1 or task_n == 2 or task_n == 3:
    try:
            task_n = int(input("Select please task number, that you want to check: \n"
                        "\t1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.\n"
                        "\t2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання\n"
                        "\t3. Користувач вводить два числа та матем дію: + - * або /\n"
                        "\t4. Stop checking tasks\n"
                        "Enter choise here: "))

            match task_n:
                case 1:
                    try:
                        num_t1 = int(input("Enter please day number pew week to show it's name: "))

                        match num_t1:
                            case 1:
                                print("This is Monday!")
                            case 2:
                                print("This is Tuesday!")
                            case 3:
                                print("This is Wednesday!")
                            case 4:
                                print("This is Thursday!")
                            case 5:
                                print("This is Friday!")
                            case 6:
                                print("This is Saturday!")
                            case 7:
                                print("This is Sunday!")
                            case _:
                                raise Exception("Please enter a valid day number!")
                    except ValueError as e:
                        print("Error: Please enter only integers!")
                    except Exception as e:
                        print(f"Error: {e}")
                case 2:
                    try:
                        num1_t2 = float(input("Enter please first number: "))
                        num2_t2 = float(input("Enter please second number: "))

                        if num1_t2 == num2_t2:
                            print("Numbers are equal.")
                        else:
                            if num1_t2 > num2_t2:
                                print(f"Here is the bigger number: {num1_t2}. Do what you need with this information, Neo!")
                            else:
                                print(f"Here is the bigger number: {num2_t2}. Do what you need with this information, Neo!")
                    except ValueError as e:
                        print("Error: Please enter only numbers!")
                case 3:
                    try:
                        num1_t3 = float(input("Enter please first number: "))
                        num2_t3 = float(input("Enter please second number: "))
                        action_t3 = input("Select action, that you want to do with these number (+, -, * or /): ")

                        match action_t3:
                            case "+":
                                print("Sum of two numbers: "+ str(num1_t3 + num2_t3))
                            case "-":
                                print("Subtraction of two numbers: " + str(num1_t3 - num2_t3))
                            case "*":
                                print("Multiplying of two numbers: " + str(num1_t3 * num2_t3))
                            case "/":
                                print("Dividing of two numbers: " + str(num1_t3 / num2_t3))
                            case _:
                                raise Exception("Please enter a valid action!")
                    except ValueError as e:
                        print("Error: Please enter only numbers!")
                    except Exception as e:
                        print(f"Error: {e}")
                case 4:
                    print("Thanks for your time!")
                    break
                case _:
                    raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("Error: Please enter only integers!")
    except Exception as e:
        print(f"Error: {e}")