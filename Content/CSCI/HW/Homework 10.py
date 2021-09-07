## Lissie
## Homework 10: 3, 4, 6, 8
## Due: 13 March 2019

## 3
## Count number of alphabetic characters and keeps track of how
## many are the letter 'e'
def count(p):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    eCount = 0
    for i in p:
        if (i in alpha) or (i in Alpha) == True:
            total +=1
            if i == "e":
                eCount += 1
    percent = (eCount/total) *100
    print("Your text contains", total, "alphabetic characters of which", eCount, "(", percent, "%)", "are 'e'.")
p = '''"Assign to a variable in your program a triple-quoted string that
contains your favorite paragraph of text - perhaps a poem, a 
speech, instructions to bake a cake, some inspirational verses, 
etc"'''
count(p)


## 4

print("\t\t\tMultiplication Tables\n")
for i in range(1,13):        
    print(i, end="\t")
    print("\n")

for row in range (1,13):
    for col in range (1,13):
        num = col*row
        print(num, end="\t")
    print("\n")

          
## 6  – write a function that reverses its string argument
def reverse(astring):
    r = ""
    for i in astring:
        r = i+r
    return (r)
astring = input("input a word")
reverse(astring)



##8
          
def remove_letter(theLetter, theString):
    new_string = ""
    for i in theString:
        if i != theLetter:
            new_string = new_string + i
    return new_string
print(remove_letter("t", "she thought that not that was what it was"))

