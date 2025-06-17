import math

def main():
    user_input = input("Enter a number: ")
    
    try:
        number = float(user_input)
        rounded_up = math.ceil(number)
        print(f"The number rounded up is: {rounded_up}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()