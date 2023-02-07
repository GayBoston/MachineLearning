#1

def func():
	print("Hello world")


#2

def summ(a,b):
	print(a+b)


#3

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fib(n-2)+fib(n-1)

for i in range(0, 8):
    print(fib(i))
 
   # this code is contributed by gangarajula laxmi

#4

def vowels(string):
	counter = 0
	for letter in string:
		if letter.lower() == 'o' or letter.lower() == 'i' or letter.lower() == 'e' or letter.lower() == 'u' or letter.lower() == 'a':
			counter += 1
	return counter


print(vowels("Hello my friend"))

#5

def largest(numbers):
	largest = None
	for el in numbers:
		if el > largest:
			largest = el
		else: continue
	print(largest)

sett = [1, 2, 6, -122, 190]
largest(sett)

#6

def c2f(deg):
	far = deg * 9 / 5 + 32
	return far

print c2f(12)

def f2c(deg):
	cel = (deg - 32) * 5 / 9
	return cel

print f2c(12)

#7

def prime(n):
	if n > 1:
		for i in range(2, int(n/2)+1):
			if (n%i) == 0:
				print(n, "is not prime")
				break
		else:
			print(n, "is a prime number")
	else:
		print(n, "is not a prime number")

prime(137)

#8

def fact(n):
	fact = 1
	for i in range(1,n):
		fact *= i
	print(fact)

fact(10)

#9

def letter_count(string):
	d = {}
	for letter in string:
		if d.has_key(letter) == False:
			d[letter] = 1
		else:
			d[letter] += 1
	for key in d:
		print(key, d[key])

letter_count("Hello world")

#10

def concatenate(strings):
	return ' '.join(strings)

strings = ["Hello", "my", "dearest", "friend"]
print(concatenate(strings))

#11

def first_n_even(n):
    i = 2
    count = 0
    while count < n:
        yield i
        i += 2
        count += 1

for n in first_n_even(10):
	print(n)


#12
old_list = [1, 6, 34, 2, -5, 3, -5, 2, -5, 2]

new_list = [x for x in old_list if x>0]

print(new_list)

#13

def squares_gen(n):
    for i in range(1, n + 1):
        yield i**2

def sum_squares(n):
	s = 0
	for i in squares_gen(n):
		s += i
	return s

print(sum_squares(15))

#14

old_str = "Hello there my dear friend"

def unique_chars(strings):
    return {char for string in strings for char in string}

print(unique_chars(old_str.split()))

#15

def square_dict(nums):
	return({num: num**2 for num in nums})

print(square_dict([1,2,3,4,5,6,7]))

#16

def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

for divisor in divisors(1000):
	print(divisor)


#17

def specific_letter(strings, letter):
	return([x for x in strings if x.startswith(letter)])

print(specific_letter("Hello my dear friends I love my mom".split(), "m"))

#18
# Write a generator expression that computes the dot product of two vectors represented as lists.
def dot_prod(v1, v2):
    return(sum(x * y for x, y in zip(v1, v2)))

print(dot_prod([1,4,6],[1,64,2]))

#19

def pal(strings):
    return {string for string in strings if string == string[::-1]}

print(pal(["hi", "my", "mom", "loves", "racecar", "watching"]))

#20

def even_odd_dict(nums):
	return({num: num%2==0 for num in nums})

print(even_odd_dict([1,2,3,4,5,6,7]))