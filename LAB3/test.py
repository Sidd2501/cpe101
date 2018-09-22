# Write a function that finds the sum of numbers between two given intervals that are divisible by 5.

'''def compute(x, y):
    i = x
    sum1 = 0
    while i <= y:
        if i % 5 == 0:
            sum1 += i
        i += 1
    return sum1


res = compute(5, 15)
print(res)'''


# Write a function that prints odd numbers between 122 and 248.

def f(x, y):
    sum = 0
    while x <= y:
        if x % 5 == 0:
            sum += 5
            x += 5
    return x


print(f(5, 20))
