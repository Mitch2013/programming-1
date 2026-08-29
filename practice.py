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

#math examples

import math
print(math.sqrt(64))  ##8
print(math.pow(2, 3)) ##8

x = 42
print(math.sin(x)**2+math.cos(x)**2) ##should equal 1
print((2+3*6)/10-5) ##-3

