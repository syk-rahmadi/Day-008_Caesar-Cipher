# Write your code below this line 👇
import math
test_h = int(input("How tall height of the wall? ")) # Height of wall (m)
test_w = int(input("How width of the wall? ")) # Width of wall (m)
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):
    number_of_cans = (height * width)/cover
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

paint_calc()