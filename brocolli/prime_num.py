""" A python code that takes in numbers  and returns a list of prime numbers """
set_num = int(input('How many numbers do you want to input: '))
y = []     # The list of inputed numbers
while len(y) <= set_num - 1:
    try:
        x = int(input('Enter a number: '))
        y.append(x)
    except ValueError:
        print(':) Enter a numerical value')
        continue
prime_num = []
not_prime = []
ck = True
for z in y:    # looping through the list of inputed numbers
    if z > 1:
        if z == 2:       # for the case when 2 is inputed
            prime_num.append(z)

        for i in range(2, z):
            if z % i == 0 :
                not_prime.append(z)
                break
            else:
                ck = False
                prime_num.append(z)

                if z % 3 == 0 and z != 3:
                    prime_num.remove(z)
                break

print(prime_num)

# print("-"*50)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(filter(is_odd, a))  # filtering
# print((b))
# c = list(map(add7, b))
# print(c)