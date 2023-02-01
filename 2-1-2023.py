#1

def func():
	print("Hello world")


#2

def sum(a,b):
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

fact(120)

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

