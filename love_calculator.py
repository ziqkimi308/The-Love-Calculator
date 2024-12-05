"""
********************************************************************************
* Project Name:  The Love Calculator
* Description:   It calculates the "love score" between two people based on the number of occurrences of specific letters in their names
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

name1 = input("Enter first name: ").lower()
name2 = input("Enter second name: ").lower()

# Combine name
combined_name = name1 + name2

# Count letter TRUE
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

# Total for TRUE
true = t + r + u + e

# Count letter LOVE
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

# Total for LOVE
love = l + o + v + e

# Love Score
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Score: {love_score} | You go together like coke and mentos")
elif 40 <= love_score <= 50:
    print(f"Score: {love_score} | You are alright together")
else:
    print(f"Score: {love_score}")