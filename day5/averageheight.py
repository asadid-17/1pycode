# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height+= height
total_lenght = 0
for lenght in student_heights:
  total_lenght +=1
print(round(total_height/total_lenght))


   

    