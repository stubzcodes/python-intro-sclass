Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
color = "red"
print (color)
red
"dev" + "ices"
'devices'
print("Hello!)
      
SyntaxError: unterminated string literal (detected at line 1)
print("Hello world")
      
Hello world
\
print("Hello" + color)
      
Hellored
print("Hello " + color)
      
Hello red
print(Hello world)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print ("Hello, " + color)
      
Hello, red
J = 50
      
print(J)
      
50
print(j)
      
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(j)
NameError: name 'j' is not defined. Did you mean: 'J'?
print("J")
      
J
1+1
      
2
J-5
      
45
5*4
      
20
J/5
      
10.0
name = "Yesi"
      
print(name.lower())
      
yesi
print(name.upper())
      
YESI
feeling = "sleepy"
      
print(name + " feels " + feeling)
      
Yesi feels sleepy
choices = ["Rock", "Paper", "Scissors"]
      
print(choices[2])
      
Scissors
25 > 10
      
True
25 < 10
      
False
25 <= 10
      
False
25 >= 10
      
True
25 == 10
      
False
10 <= 10
      
True
10 < 10
      
False
A == 10
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    A == 10
NameError: name 'A' is not defined
A = 10
      
A == 10
      
True
"name" == "Name"
      
False
False
      
False
if J > 25:
      print('J is the winner!')

      
J is the winner!
if J < 25:
      print('J is the winner!')

      
feeling = "needs a snack."
      
print(name + " " + feeling)
      
Yesi needs a snack.
if J > 60:
      print("J is the winner")
else:
    print("J is the loser.")

    
J is the loser.
if J > 50:
    print("J is the winner!")
elif J == 50:
    print("It's a tie!")
else:
    print("J is the loser.")

    
It's a tie!
It's a tie!
SyntaxError: unterminated string literal (detected at line 1)

player = input("Rock, Paper, or Sciessors?: ")
Rock, Paper, or Sciessors?: "Rock"
print(player)
"Rock"
for x in range(5):
    print(x)

    
0
1
2
3
4
count = 0
while count < 10:
...     print(count)
...     count = count + 1
... 
...     
0
1
2
3
4
5
6
7
8
9
>>> count = 25
>>> while count < 101
SyntaxError: expected ':'
>>> count = 25
>>> while count < 101:
...     print (count)
...     count = count + 5
... 
...     
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
