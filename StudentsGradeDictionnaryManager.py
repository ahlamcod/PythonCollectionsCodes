#Students Grades Manager----------------------------------------
print("----------------Welcome to student grade manager--------------------------")
while True:
    try:
        num_students=int(input("inter students number of this class: "))
        break   #exit the loop once input is valid
    except ValueError:
        print("Value Error detected, inter an integer students number: ")

print("----------------Dictionnary creation--------------------------")
StudentDictionary={}
for i in range(num_students):
    Student=input("Insert student full name: ")
    while True:
        try:
            Grade=float(input("Insert the student grade: "))
            break #exit the loop once input is valid
        except ValueError:
            print("Value Error detected, inter a real number for the student grade: ")
    StudentDictionary[Student] = Grade
avg_grade=0
for j in StudentDictionary.values():
    avg_grade=avg_grade+j
avg_grade=avg_grade/num_students
print("The dictionnary is: ", StudentDictionary)
print("The class mean grade is: ", avg_grade)
