while True:
    num = input("Enter a number (or 0 to exit): ")

    if num == 0:
        print("Exiting... Goodbye!")
        break

    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
