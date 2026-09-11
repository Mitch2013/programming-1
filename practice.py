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


### calculator

import math

print("-"*80)

item=(input("What item did you buy? "))
price_item=(float(input(f"How much did the {item} cost? ")))
item_amount=int(input(f"How many {item} did you buy? "))
sales_tax=(float(input("What is the sales tax percentage? ")))

tax_rate=sales_tax/100
subtotal=price_item*item_amount
tax=tax_rate*subtotal
total=tax+subtotal

print("="*80)
print("RECEIPT")
print("="*80)

print(f"{item}: {item_amount} * ${price_item:.2f} = ${subtotal:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({sales_tax}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

