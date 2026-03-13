# FILE NAME - grade_converter.py

# NAME: Hoi I Tam
# DATE: March 12, 2026
# BRIEF DESCRIPTION: Converts a numerical grade to a letter grade as follows:
# Below 65	F
# [65, 70)	D
# [70, 80)	C
# [80, 90)	B
# [90, 100]	A
# Above 100	A+
101
########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")

grade = float(input("Enter a numerical grade (1-100): "))

if grade > 100:
    print("A+")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
else:
    print("F")


########### END YER CODE ABOVE THIS LINE ###########

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
We should be careful about the order of the if statements. We should start with the highest grade range to the lowest grade range 
to ensure that the correct letter grade is assigned based on the numerical grade input by the user.



'''
