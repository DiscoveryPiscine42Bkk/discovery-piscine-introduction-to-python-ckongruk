def print_multiplication_tables():
    print("multiplication Tables")
    print("---------------------")

    for i in range(1, 11):
        print(f"Table for {i}:")
        for j in range(1, 11):
            result = i * j
            print(f" {i} x {i} = {result}")
        
        print("")

    print_multiplication_tables()