studentNo = int(input("Enter number of students = "))
weightInLB =[]
for x in range(studentNo):
    weightInLB.append(int(input("Enter weight for student :")))
print(weightInLB);
weightInKG = []
i=0
while i < weightInLB.__len__():
    wt = int(weightInLB[i]/2.205)
    wt =  "{: .2f}".format(wt)
    print(wt)
    weightInKG.append(wt)
    i += 1
print(weightInKG)