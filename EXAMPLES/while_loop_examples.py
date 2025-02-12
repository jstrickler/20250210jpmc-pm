
print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    guess = 13
    input_str = input(f"Is {guess} your number?")
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("Please enter the ticket quantity")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    print(f"sending {quantity} ticket(s)")

# x +=1  # x = x + 1