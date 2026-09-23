"""
PROJECT 1: CALCULATOR
======================
WHAT THIS TEACHES:
- Writing small, single-purpose functions
- Using a dictionary as a "dispatch table" (instead of a long if/elif chain)
- Handling bad input gracefully with try/except
- A basic program loop (the "REPL" pattern: Read, Evaluate, Print, Loop)
"""

# --- Step 1: Define one function per operation. -----------------------
# Each function does ONE thing. This is a core Python habit: small,
# testable functions instead of one giant block of code.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Division can fail (divide by zero), so we guard against it here
    # rather than letting the program crash.
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# --- Step 2: Map symbols to functions. ---------------------------------
# Instead of writing:
#     if op == "+": result = add(a, b)
#     elif op == "-": result = subtract(a, b)
#     ...
# we store the functions themselves as dictionary VALUES. Functions are
# "first-class objects" in Python -- you can pass them around like any
# other variable. This is called a "dispatch table" and it scales much
# better than a long elif chain if you add more operators later.
OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    """Keep asking until the user gives a valid float. Demonstrates
    input validation with a while loop + try/except."""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' isn't a valid number, try again.")


def main():
    print("Simple Calculator. Type 'q' to quit.\n")

    while True:  # main program loop -- keeps running until user quits
        op = input(f"Choose an operation {list(OPERATIONS.keys())} or 'q': ").strip()

        if op == "q":
            print("Goodbye!")
            break  # exits the while loop

        if op not in OPERATIONS:
            print("Unknown operation, try again.\n")
            continue  # skips the rest of this loop iteration

        a = get_number("First number: ")
        b = get_number("Second number: ")

        try:
            # OPERATIONS[op] retrieves the FUNCTION, then we call it with (a, b)
            result = OPERATIONS[op](a, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            # This catches the "Cannot divide by zero" error raised above
            print(f"Error: {e}\n")


# This check means "only run main() if this file is executed directly,
# not if it's imported into another file." Standard Python convention.
if __name__ == "__main__":
    main()
