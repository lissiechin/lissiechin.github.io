### Lissie Chin
### Homework 1 (#1,2,4,5,6)
### Due February 13, 2019

# Problem 1
5 ** 2  	# I calculated this to be 25, and the computer agreed
9 * 5   	# I calculated this to be 45, and the computer agreed
15 / 12 	# I calculated this to be 1.25,and the computer agreed
12 / 15         # I calculated this to be 0.8, and the computer agreed
15 // 12	# I calculated this to be 1, and the computer agreed
12 // 15	# I calculated this to be 0, and the computer agreed
5 % 2		# I calculated this to be 1, and the computer agreed
9 % 5		# I calculated this to be 4, and the computer agreed
15 % 12		# I calculated this to be 3, and the computer agreed
12 % 15		# I calculated this to be 12, and the computer agreed
6 % 6		# I calculated this to be 0, and the computer agreed
0 % 7		# I calculated this to be 0, and the computer agreed

# Problem 2
print (2 + (3 - 1) * 10 / 5 * (2 + 3))
# 2 + 2 * 10 / 5 * 5
# 2 + 2 * 2 * 5
# 2 + 2 * 10
# 2 + 20
# ==22

#with PEMDAS, I got 2.8 as my answer, not 22 which the computer did get.
#2 + 2 * 10 / 5 * 5
#2 + 20 / 25
# 2 + 0.8
# ==2.8




# Problem 4

Day0 = "Sunday"
Day1 = "Monday"
Day2 = "Tuesday"
Day3 = "Wednesday"
Day4 = "Thursday"
Day5 = "Friday"
Day6 = "Saturday"

Day_left = input("what day did you leave? enter #: 0 being Sunday - 6 being Saturday")
Length_of_stay = input("number of day until you return")

Day_left = int(Day_left)
Length_of_stay = int(Length_of_stay)

Return_day = Day_left + Length_of_stay
Return_day = Return_day % 7 
print ("You will return on day",Return_day)



# Problem 5
A = "all"
W = "work"
B = "and"
N = "no"
P = "play"
C = "makes Jack a dull boy"
	# lazy, just kidding
D = "makes"
E = "Jack"
F = "a"
G = "dull"
H = "boy"
print (A, W, B, N, P, D, E, F, G, H)



# Problem 6
print (6 * 1 - 2)
print (6 * (1-2))











