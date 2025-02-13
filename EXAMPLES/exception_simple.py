
try:  # Execute code that might have a problem
    x = 5
    f = open("wombats.csv")
    # raise KeyError("this is bad")
    # m = x / 0
    y = "cheese"
    z = x + y
    print("Bottom of try")

except (TypeError, ValueError) as err:    # Catch the expected error; assign error object to err
    # raise  # reraise this exception
    print("Naughty programmer! ", err)
except ZeroDivisionError as err:
    print("DID NOT EXPECT THAT!")
except Exception as err:
    print("OK!", err)

print("After try-except")  # Get here whether or not exception occurred
