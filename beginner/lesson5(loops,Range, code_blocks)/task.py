fruits=['Apple','Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores=[150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199,78, 65,89]
total_exam_score=sum(student_scores)
print(total_exam_score)

# or use for loop to sum
sum1=0
for score in student_scores:
    sum1+=score
print(sum1)

max1= max(student_scores)
print(max1)
# using for loop to get max
max_score=0
for marks in student_scores:
     if marks > max_score:
         max_score = marks
print(max_score)

# range
for number in range(1,10):
    print(number)

total=0
for num in range(1, 101):
    total+=num
print(total)

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} is FizzBuzz")
    elif n % 3 == 0:
        print(f"{n} is Fizz")
    elif n % 5 == 0:
        print(f"{n} is Buzz")
    else:
        print(f"{n} is not divisible by 3 or 5")

