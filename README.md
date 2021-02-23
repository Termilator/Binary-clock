![Header image] (/screenshot.jpg)

# Binary clock

This clock shows the current time (24 hours: 59 minutes) using six digits,
that have a total possible value of 64. Naturally, in a clock we only need
to count to 59.

The point of this program is, in addition to being a great programming exercise
for me, to play with binaries. They don't come up too often in everyday life,
but reading them is good exercise for the brain, and for some people, even fun.

## About

I wrote the program in **Microsoft Visual Studio** IDE in **Python.** 
It uses the datetime library to fetch current time, and tkinter library for
the graphic window.

## How do I read it?

In binary, we have digits (also known as bits) that have two possible states, 
ON or OFF. In this case we use 0 and 1 to represent these states. 
When a digit is 0, it's OFF and we don't count its value. 
When its 1, it's ON and it is counted.

The value of a digit is based on the number two. We read the digits from right
to left. Each digit is 2 to the power of N, with N refering to the digit.
So the first digit (starting from right) gets the value of 2^0 = 1,
the second digit gets the value of 2^1 = 2, the third 2^2 = 4 and so on.

When we use multiple digits, we count the sum of all the ON digits.

Here's the count from 0 to 5 using a six digit binary:

Value  32  16  8   4   2   1   | decimal

       0   0   0   0   0   0   |    0
       0   0   0   0   0   1   |    1
       0   0   0   0   1   0   |    2
       0   0   0   0   1   1   |    3
       0   0   0   1   0   0   |    4
       0   0   0   1   0   1   |    5
