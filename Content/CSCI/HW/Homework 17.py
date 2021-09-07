## Lissie
## Homework 17
## Due April 15,2019

## 1 – Caesar Cipher

# PART 1 ––– Tyqzcxletzy dpnfctej td xzcp txazcelye ezolj esly pgpc mpqzcp.
      # PLAIN TEXT: Information security is more important today than
      # ever before.

# PART 2 ––– M riih e vmhi xs xli emvtsvx xsqsvvsa.
      # Shift: -4
      # PLAIN TEXT: I need a ride to the airport tomorrow.




                        ### Function Below ###

##def caesarShift(char, num):
##    if char.islower():  #lowercase letters have ASCII values 97 to 122
##        val = ord(char) - 97 + num
##        return chr((val % 26) + 97)
##    else:               #uppercase letters have ASCII values 65 to 90
##        val = ord(char) - 65 + num
##        return chr((val % 26) + 65)
##
##
###do some encryption/decryption
##original = input("Enter some text: ")
##goodShift = False
##while goodShift == False:
##    try:
##        shift = int(input("Enter the shift amount: "))
##    except ValueError:
##        print("Invalid input, please try again and enter a number.")
##    else:
##        goodShift = True
##
##transformed = ""
##
##for char in original:
##    if char.isalpha():
##        transformed = transformed + caesarShift(char, shift)
##    else:
##        transformed = transformed + char
##
##print(transformed)



## 2 – Digital Signatures

#PART 1 –  where are we meeting?.octagon
      # SHA-1 : ebba51ba0053c0247f8f00805a395d18198c4718
      # Where are we meeting?4be1e96b

#PART 2 – meet at the LAB



                              ### work below ####

import hashlib

#function to return the SHA-1 digest of a message
def SHA1(msg):
    s = hashlib.sha1()
    s.update(msg.encode())
    return s.hexdigest()


#prompt the user for a message and compute its SHA-1 digest
##message = input("Enter a message: ")
##print("The SHA-1 digest is:", SHA1(message))
##

send = "Where are we meeting?.198c4718"
mess = "Where are we meeting?"
            # without ? = Where are we meeting7f0c4fed
            # with ? = Where are we meeting?4be1e96b

secret = "octagon"
send = mess + SHA1(mess+secret)[:8]
print (send)
print(SHA1(send))

print("separate -- starting part 2")

opt1 = "Meet me at the park.7531a2ad"
opt2 = "Meet me at the cafeteria.e53b06c8"
opt3 = "Meet me at the lab.20132b74"
opt4 = "Meet me at the dorm.b15d98c3"

l = [opt1, opt2, opt3, opt4]
y = SHA1(send)


def findot(l):
      idx = 0
      for i in l:
            for char in i:
                  if char == ".":
                        return (idx)
                  idx+=1
for i in l:
      x = findot(i)
      print(x)
      idx = int(input("enter number above"))
      recM = i[:idx]+ ".octagon"
      recM = SHA1(recM)
      print (recM[:8])
      if recM[:8] == i[idx+1:]:
            print ("It's just going to continue but " + i)
      else:
            print ("nope")


      
