## Lissie Chin
## Homework 16
## Due April 12, 2019


## 1 – Write program
      ## Ask user for name of file
      ## attempt to open file and print contents
      ## if unable to open – exception – print helpful error message

filename = input("enter file name:")
try:
      File = open(filename, "r")
except:
      print ("file is not found")

else:
      print (File.read())
File.close()


## 2 – consider following code
      ## Function B() adds list of numbers but if contains non-numerical entry,
      ## function will rise a TypeError

      ## Modify function A() so the call to function B() is inside try block and
      ## any TypeError is handled by printing a helpful message
      
def B(b_list): 
      s = 0 
      for i in b_list:
            s += i
      return s
      
def A(a_list):
      try:
            return B(a_list)
      except TypeError:
            return ("Type error – there is a non-numerical entry")

print(A([1, 2, 3]))
print(A([1, "two", 3]))
