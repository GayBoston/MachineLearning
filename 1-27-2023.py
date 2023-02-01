def inp():
	string = raw_input("Enter a string: ")
	return string

def reverse(string):
	x = string.split()
	new_string = " ".join(x[::-1])
	return new_string

def replace(string):
	x = string.split()
	word = raw_input("What word would you like to replace (case sensitive): ")
	ind = x.index(word)
	new_word = raw_input("What would you like to replace it with: ")
	x[ind] = new_word
	new_string = " ".join(x)
	return new_string

# def replace2(string):
# 	x = string.split()
# 	y = string.lower().split()
# 	word = raw_input("What word would you like to replace: ")
# 	cword = word.lower()
# 	ind = y.index(cword)
# 	new_word = raw_input("What would you like to replace it with: ")
# 	x[ind] = new_word
# 	new_string = " ".join(x)
# 	return new_string


def replace2(string):
    words = string.split()
    lower_words = string.lower().split()
    word = raw_input("What word would you like to replace: ")
    cword = word.lower()
    new_word = raw_input("What would you like to replace it with: ")

    if cword in lower_words:
        words[lower_words.index(cword)] = new_word
    else:
        return "Word not found"
    return " ".join(words)

ones = {
	"0": "zero",
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine"
}
tens = {
	"1": "teen",
	"2": "twenty",
	"3": "thirty",
	"4": "fourty",
	"5": "fifty",
	"6": "sixty",
	"7": "seventy",
	"8": "eighty",
	"9": "ninety"
}
special = {
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen"
}


def write_int(string):
	x = string.split()
	for word in range(len(x)):
		w = unicode(x[word], "utf-8")
		if w.isnumeric() == True:
			if len(x[word]) == 1:
				x[word] = ones[x[word]]
			if len(x[word]) == 2:
				if x[word][0] == '1':
					if int(x[word]) < 16:
						x[word] = special[x[word]]
						continue
					else:
						x[word] = ones[x[word][1]] + tens[x[word][0]]
						continue
				if x[word][1] == '0': 
					x[word] = tens[x[word][0]]
					continue
				x[word] = tens[x[word][0]] + "-" + ones[x[word][1]]
	new_string = " ".join(x)
	return new_string


if __name__ == '__main__':
	string = inp()
	# print("Reversed: " + reverse(string))
	# new_string = replace2(string)
	print(write_int(string))
	# print(new_string)
