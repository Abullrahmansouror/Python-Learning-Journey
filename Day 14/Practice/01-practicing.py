

answer_1 = "19"

while True:
    question_1 = input("How old are Abdo?: ")
    if answer_1 == question_1:
        break
    else:
        print("Wrong answer, Try again!")

answer_2 = "180cm"

while True:
    question_2 = input("How tall are Abdo?: ")
    if answer_2 == question_2:
        break
    else:
        print("Wrong answer, Try again!")

print(f"Your exact answers is Age: {answer_1} hieght: {answer_2}")