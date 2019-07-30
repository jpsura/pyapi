#!/usr/bin/env python3
import sys

# Start with an infinite loop
while True:
    try:
        z = "Successful Job"
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print('Handling run-time error:', zerr)
        x = "Error div by zero"
    # general error handling
    # a practical use might be exceptions we haven't designed solution for yet
    except ValueError as err:
        z = "Value Error detected"
    except:
        # sys.exc_info returns a 3 tuple with into about the exception handled
        print("We did not anticipate that error in this code")
        print(sys.exc_info()[0])
        z = sys.exc_info()[0]
        # raise by itself simply calls the previous exception that was thrown
        raise
    finally:
        with open("try02.log", "a") as log:
            log.write(z+"\n")
