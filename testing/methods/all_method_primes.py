# My problem was initially that I didn't notice that I could have given
# directly a list to the all() method. Behaviour that, on the other hand, is
# shown in here https://hyperskill.org/learn/step/7800#conditions
# My bad.

# First and explicit way
prime_numbers = []

for i in range(2, 1001):
    aux = []
    for j in range(2, i):
        aux.append(i % j)
    if all(aux):
        prime_numbers.append(i)

print(prime_numbers)


# Second way less explicit
prime_numbers2 = []
for i in range(2, 1001):
    if all([i % j for j in range(2, i)]):
        prime_numbers2.append(i)

print(prime_numbers2)


# Third way using list comprehension
p_ns = [i for i in range(2, 1001) if all([i % j for j in range(2, i)])]

print(p_ns)
