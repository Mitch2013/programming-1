###f string examples

name = 'alice'
age = 25
message = f"My name is {name.upper()} and I am {age} years old"
print(message)

total = 20
report = f"""
sales: ${total}
"""
print(report)

###math examples

import math
print(math.sqrt(64))  ##8
print(math.pow(2, 3)) ##8

x = 42
print(math.sin(x)**2+math.cos(x)**2) ##should equal 1
print((2+3*6)/10-5) ##-3

### \n splits the line to the line below
print("a really long statement \nthat would exceed 80 characters")

### creating a function

def create_name():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    return full_name

# This works
result = create_name()
print(result)


### calculator and \n at the end to have the user input below the question

import math

print("-"*80)

item=(input("What item did you buy?\n"))
price_item=(float(input(f"How much did the {item} cost?\n" )))
item_amount=int(input(f"How many {item} did you buy?\n" ))
sales_tax=(float(input("What is the sales tax percentage?\n" )))

tax_rate=sales_tax/100
subtotal=price_item*item_amount
tax=tax_rate*subtotal
total=tax+subtotal

### Grade calculator

print("="*80)
print("RECEIPT")
print("="*80)

print(f"{item}: {item_amount} * ${price_item:.2f} = ${subtotal:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({sales_tax}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

score = float(input("Enter your score (0-100): \n"))

print("*"*80)
print(" "*34, "GRADE REPORT")
print("_"*80)

if score < 0 or score > 100:
    print("Please enter a valid score between 0 and 100")
elif score == 100:
    grade = "A"
    feedback = "And they say nobody's perfect!"
elif score >= 90:
    grade = "A"
    feedback = "Fantastic Effort!"
elif score >= 80:
    grade = "B"
    feedback = "Well Done!"
elif score >= 70:
    grade = "C"
    feedback = "Adequate job."
elif score >= 60:
    grade = "D"
    feedback = "This could be improved"
else:
    grade = "F"
    feedback = "Unsatisfactory"

if 0 <= score <= 100:
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")
print("*"*80)

# 'greeting' has a default argument of "Hello"
# 'punctuation' has a default argument of "!"
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

# 1. Use both default arguments
print(greet("Alice"))  
# Output: Hello, Alice!

# 2. Override only the first default argument
print(greet("Bob", "Good morning"))  
# Output: Good morning, Bob!

# 3. Override both default arguments
print(greet("Charlie", "Welcome", "."))  
# Output: Welcome, Charlie.

# 4. Override a specific default argument using a keyword argument
print(greet("Dana", punctuation="?"))  
# Output: Hello, Dana?