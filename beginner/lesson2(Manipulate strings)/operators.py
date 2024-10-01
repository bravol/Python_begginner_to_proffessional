# ROUND OFF OPERATOR
bmi=84/1.65**2
print(bmi)
print(int(bmi)) #chopping off the end
print(round(bmi))  #rounding off to whole number
print(round(bmi,2)) # rounding to 2 decimal places

# 2
score=0
height=1.8
is_winning=True
# user scores a point
score+=1
print(score)


print("Your score is: "+str(score))
# f strings
print(f"Your score is {score}, Your height id {height}, Your winning is {is_winning}")