def newClass(listCLASS, currentNumClass):
    currentNumClass += 1
    s = "CLASS" + str(currentNumClass)
    listCLASS += [s]
    return currentNumClass
def makeClassOf(numOfStudents):
    for i in range(numOfStudents):
        studentID = input("Enter Student ID: ")
        studentName = input("Enter Student Name: ")
        studentDOB = input("Enter Student DOB: ")

def main():
    #init
    CLASS = []
    numOfClass = 0

    #test
    numOfClass = newClass(CLASS, numOfClass)
    numOfClass = newClass(CLASS, numOfClass)
    print(*CLASS)

if __name__ == "__main__":
    main()