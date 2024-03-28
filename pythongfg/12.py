#Program to create grade calculator in Python

# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }
 
# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }
 
# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }
 
# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }
 
# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }


def avg_marks(marks):
    total_marks=sum(marks)
    total_marks=float(total_marks)
    return total_marks/len(marks)

def final_avg(students):
    assignment=avg_marks(students["assignment"])
    test=avg_marks(students["test"])
    lab=avg_marks(students["lab"])

    # Return the result based
    # on weightage supplied
    # 10 % from assignments
    # 70 % from test
    # 20 % from lab-works

    return (assignment*0.1+test*0.7+lab*0.2)

def grade(score):
    if score>=90 and score<100:
        print("Grade O")
    elif score >=80 and score<90:
        print("Grade E")
    elif score >=70 and score<80:
        print("Grade A")
    elif score >=60 and score<70:
        print("Grade B")
    elif score >=50 and score<60:
        print("Grade C")
    elif score >=40 and score<50:
        print("Grade A")
    else:
        print("Fail,Try again")

students=[jack,james,dylan,jess,tom]

for i in students:
    print(i["name"])
    print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("Average of ",i["name"],"is",final_avg(i))
    print("grade of",i["name"],"is",grade(final_avg(i)))

