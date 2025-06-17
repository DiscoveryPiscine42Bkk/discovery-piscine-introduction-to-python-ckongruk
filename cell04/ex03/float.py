def main():
    user_input = input("Enter a number: ")
    
    try:
        number = float(user_input)
        
        if number.is_integer():
            print("The number you entered is not a decimal (it's an integer).")
        else:
            print("The number you entered is a decimal.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()