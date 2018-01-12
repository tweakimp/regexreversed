import random
import string

repetitionlimit = 5
digits = string.digits
letters = string.ascii_letters  # concatenation of lowercase and uppercase
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase


def sanitizeInput(regex):
    output = ""
    for i in regex:
        output += str(i)
    return output


def analyseRegex(regex):
    expressionlist = []
    i = 0
    while len(regex) != 0:
        if regex[i] == "[":
            substring = ""
            while regex[i] != "]":
                substring += str(regex[i])
                i += 1
            else:
                substring += str(regex[i])
                i += 1
            expressionlist.append(str(substring))
            regex = regex[i:]
            i = 0
        else:
            expressionlist.append(str(regex[0]))
            regex = regex[1:]

    output = expressionlist
    return output


def printExpressions(regex, examplecount):
    distinctoutput = []
    for n in range(examplecount):
        outputlist = []
        output = ""
        for i in regex:
            if i == "[0-9]":
                outputlist.append(random.choice(digits))
            elif i == "[A-Z]":
                outputlist.append(random.choice(uppercase))
            elif i == "[a-z]":
                outputlist.append(random.choice(lowercase))
            elif i == "[a-zA-Z]":
                outputlist.append(random.choice(letters))
            elif i[0] == "[":
                substring = i[1:-1]
                outputlist.append(random.choice(substring))
                del substring
            elif i == "*":
                repetition = random.choice(range(0, repetitionlimit + 1))
                substring = outputlist[-1] * repetition
                del outputlist[-1]
                outputlist.append(substring)
                del substring
            elif i == "+":
                repetition = random.choice(range(0, repetitionlimit + 1))
                substring = outputlist[-1] * repetition
                outputlist.append(substring)
                del substring
            elif i == "?":
                repetition = random.choice(range(0, 2))
                substring = outputlist[-1] * repetition
                del outputlist[-1]
                outputlist.append(substring)
                del substring
            else:
                outputlist.append(i)
        for j in outputlist:
            output += j
        distinctoutput.append(output)
    distinctoutput = sorted(list(set(distinctoutput)), key=len)
    for i in range(len(distinctoutput)):
        print(distinctoutput[i])


print("\n___________")
regex = str(input())
print("input:", regex)
regex = sanitizeInput(regex)
regex = analyseRegex(regex)
printExpressions(regex, 40)


# if __name__ == "__main__":
# printExpressions(10)
