__author__ = 'nvishwakarma'

studDet = {}


def StudentInp():
    no = int(input("Enter number of students::"))
    if no>=2 and no<=10:
        for n in range(0, no):
            name = input("Enter name of students::")
            studDet[name] = int(input("Enter marks of student in Maths::")), int(input("Physics::")), int(input("Chemistry::"))
            for i in range(0,2):
                if (studDet[name][i]<0 or studDet[name][0]>100):
                    print("Marks would be between 0 to 100. Try again!")
                    studDet.clear()
                    StudentInp()
                else:
                    break;

    print(no)
    return studDet


def StudentAvg(name, studDet):
    avg = round((studDet[name][0] + studDet[name][1] + studDet[name][2])/3,2)
    print("Average marks for::", name, "is", avg)


studDet = StudentInp()
print(studDet)
name = input("Enter name of students::")
StudentAvg(name, studDet)

