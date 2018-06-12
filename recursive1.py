# 5! = 5*4*3*2*1
# 5! = 5 * 4!

def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number-1)

# print(fact(997))

def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + " " + explode(word[1:])

def removeDupes(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDupes(word[1:])
    else:
        return word[0] + removeDupes(word[1:])

print(explode("banana"))
print(removeDupes("hello"))
