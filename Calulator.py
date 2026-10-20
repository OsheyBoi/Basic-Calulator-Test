a = input("Input Number:")
b = input("Input Math Symbol (+ | - | * | /  | ^")
c = input("Input Number:")

a = int(a)
c = int(c)

if b == "+":
    result = a + c

if b == "-":
    result = a - c

if b == "*":
    result = a * c

if b == "/":
    result = a / c

if b == "^":
    result = a^c

print("Result:" + str(result))

print("--------------------")

print("Test 2")
a = 12
b = 12
print ("a = ", a)

print ("a = " + str(a))

