import numpy as np

maximize = False

in_file = open("input.txt")
lines_to_read = [0,2]
run = True
output = open("log.txt", "w")
solution = open("solution.txt", "w")
lines = in_file.readlines()
constraintLine = int(lines[5])
slackStart = int(lines[7])
varLine = int(lines[5]) + int(lines[7])
rowLength = varLine + 1 + constraintLine

if "maximum" in lines[3]:
    maximize = True
if run == True:
    
    #add number of artificial variables equal to number of equations
    baseTableau = np.zeros(shape=(constraintLine + 1, (rowLength)))
    #no. of constraint +2 (for obj rows)
    #varline + 2 for slack + x's + solution + z +constraintline again for artificial vars
    print("tableau base")

    output.write("Tableau dimesions: ")
    output.write(str(constraintLine + 1))
    output.write("x")
    output.write(str(rowLength))
    output.write("\n")
    np.savetxt(output, baseTableau, fmt='%1.2f')
    output.write("\n")
    print(baseTableau)
    slackCount = 0
    for i in range(9, 9+(constraintLine)):
        needArtificial = False
        removeSlack = False
        baseRow = np.zeros(rowLength)
        slackValue = 1 #decide if + or - slack
        lSplit = lines[i].split(" ")
        lSplit[-1] = lSplit[-1].strip() #remove /n
        #take lSplit[-1] add to array
        baseRow[-1] = lSplit[-1]
        q = lSplit[0].split("+")
        for s in range(len(q)):
            #decide on slack var
            if ">=" in str(q):
                q[s] = q[s].replace(">=", "")
                removeSlack = True
                slackValue = -1
                needArtificial = True
                
            if "<=" in str(q):
                q[s] = q[s].replace("<=", "")
                removeSlack = True
                slackValue = 1
                
            if "==" in str(q):
                q[s] = q[s].replace("==", "")
                removeSlack = True
                slackValue = 0
                needArtificial = True
                print(str(q))
            if "x1" in str(q): #need str(q) else wont recognize if number infront of x1
                q[s] = q[s].replace("x1", "")
            
                #check if list is empty
                if not q[s]: #replace empty list element with 1
                    q[s] = 1   
                baseRow[0] = q[s]
                
            elif 'x2' in str(q):
                q[s] = q[s].replace("x2", "")
            
                #check if list is empty
                if not q[s]: #replace empty list element with 1
                    q[s] = 1   
                baseRow[1] = q[s]    
            elif 'x3' in str(q):
                q[s] = q[s].replace("x3", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
            elif 'x4' in str(q):
                q[s] = q[s].replace("x4", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
            elif 'x5' in str(q):
                q[s] = q[s].replace("x5", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
            elif 'x6' in str(q):
                q[s] = q[s].replace("x6", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
            elif 'x7' in str(q):
                q[s] = q[s].replace("x7", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
            elif 'x8' in str(q):
                q[s] = q[s].replace("x8", "")

                if not q[s]:
                    q[s] = 1   
                baseRow[2] = q[s]
        if removeSlack == True:
            baseRow[slackStart + slackCount] = slackValue
        if(all(i <= 0 for i in baseRow)):
            baseRow = baseRow * -1
            print(baseRow)
            needArtificial = not needArtificial

        #artificial variables
        if needArtificial == True:
            baseRow[(varLine) + slackCount] = 1
        if needArtificial == False:
            baseRow[(varLine) + slackCount] = 0

        baseTableau[slackCount] = baseRow

        slackCount += 1
        #now for objective function
    objFunc = lines[1]
    objList = objFunc.split("=")
    objList[-1] = objList[-1].strip()
    objRow = np.zeros(rowLength)
    for i in range(len(objList)):
        if "z" in str(objList[i]):
            objList[i] = objList[i].replace("z", "")
            if not objList[i]: #replace empty list element with 1
                    objList[i] = 1
            objRow[varLine+constraintLine] = objList[i]
        else:
            #equation side of list
        
            eqn = objList[i].split("+")
            for s in range(len(eqn)):
                if "x1" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x1", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[0] = int(eqn[s]) * -1 #change side of = 
                if "x2" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x2", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[1] = int(eqn[s]) * -1
                if "x3" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x3", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[2] = int(eqn[s]) * -1
                if "x4" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x4", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[1] = int(eqn[s]) * -1
                if "x5" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x5", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[2] = int(eqn[s]) * -1
                if "x6" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x6", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[1] = int(eqn[s]) * -1
                if "x7" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x7", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[2] = int(eqn[s]) * -1
                if "x8" in str(eqn[s]): 
                    eqn[s] = eqn[s].replace("x8", "")
                    if not eqn[s]: 
                        eqn[s] = 1   
                    objRow[2] = int(eqn[s]) * -1

    mostMagnitude = -1
    #adjustable factor of artificial variable
    M = 100
    baseTableau[constraintLine] = objRow
    #for i in range((2*constraintLine - 1), 3*constraintLine -1):
        #find a that corresponds to that row, multiply it b m

        
        #baseTableau[-1,i] = (abs(aFactor))*sum + baseTableau[-2,i]

    for i in range(constraintLine):#row of constraints in tableau
         for s in range((2*constraintLine), (3*constraintLine)): #columns of artificial vars
             if baseTableau[i,s] == 1: #if there is a artificial var present
                 print(i,s)
                 for p in range(-1,2*constraintLine):
                     
                     if maximize == True:
                        baseTableau[-1,p] = baseTableau[-1,p] - M * baseTableau[i,p]
                     if maximize == False:
                        baseTableau[-1,p] = baseTableau[-1,p] + M * baseTableau[i,p]

    #baseTableau = np.delete(baseTableau, (-2), axis=0)
    print("New base Tableau")
    print(baseTableau)
    output.write("Tableau before pivot: \n")
    np.savetxt(output, baseTableau, fmt='%1.2f')
    output.write("\n")


def pivot(A,count):
    #initialize values
    columnToPivot = 0
    rowToPivot = 0
    count += 1
    #do the pivot
    if maximize == True:
        #step 1 determine which column has the most negative entry in it
        leastValue = 0 #initialize least value
        for i in range(len(objRow)-1):
            if A[-1,i] < leastValue:
                leastValue = A[-1,i]
                columnToPivot = i
                print("LV IS: ", leastValue)
        #step 2 Find pivot row
    elif maximize == False:
        #step 1 determine which column has the most positive entry in it
        leastValue = 0 #initialize least value
        for i in range(len(A)):
            if A[-1,i] > leastValue:
                leastValue = A[-1,i]
                columnToPivot = i
                
        #step 2 Find pivot row
    
    resultLeastValue = 0
    for i in range(len(A) - 1):
            if A[i, columnToPivot] != 0:
                if((A[i, -1] /A[i, columnToPivot]) >= 0):
                     resultLeastValue = (A[i, -1] /A[i, columnToPivot])
                     rowToPivot = i
        
    for i in range(constraintLine):
        divider = float(A[i, columnToPivot])
        if divider != 0:
            if (A[i,-1] / divider) < resultLeastValue and (A[i,-1] / divider) >= 0:
                if(divider < 0 and A[i,-1] == 0):
                    print("cannot")
                else:
                    resultLeastValue = A[i,-1] / divider
                    rowToPivot = i

            if (A[i,-1] / divider) == resultLeastValue and (A[i,-1] / divider) >= 0:#if ratio is the same
                if(A[i,-1] < A[rowToPivot,-1]):
                    resultLeastValue = A[i,-1] / divider
                    rowToPivot = i

    

    print("pivot point is: ", rowToPivot, columnToPivot)
    print(A[rowToPivot, columnToPivot])
    #divide row by the element in the row to make sure it is 1
    A[rowToPivot] = A[rowToPivot] / A[rowToPivot, columnToPivot]
    #step 3 make column a unit vector
    for i in range(len(A)):
        #perform row operations on every row except for pivot row
        if i != rowToPivot:
            if A[i,columnToPivot] != 0:
                A[i] = A[i] - ((A[i,columnToPivot] / A[rowToPivot, columnToPivot]) * A[rowToPivot])
    np.set_printoptions(suppress=True) #dont want scientific notations
    
    print("pivot", count, ":")

    output.write("pivot ")
    output.write(str(count))
    output.write(": \n")
    
    np.savetxt(output, A, fmt='%1.2f')
    output.write("\n")

    print(np.around(A,2))
    
    #if more negative elements in obj row, repeat process
    if maximize == True:
        for i in range((len(objRow)-1)):
            if A[-1,i] < 0:
                pivot(A,count) #recursion
    if maximize == False: 
        for i in range((len(objRow)-1)):
            if A[-1,i] > 0:
                pivot(A,count) #recursion 
       
    
def getResults(A):
    #check for unit vector
    print(A[-1,-1])
    for i in range(len(objRow)):
        noResult = False
        arr = []
        arr = A[:,i]
        sortedArr = np.sort(arr)
        
        for q in range(len(sortedArr)-1):
            #make sure unit column
            if(sortedArr[q] != 0):
                noResult = True

        if(noResult==False):
            for p in range(len(arr)):
                if arr[p] == 1 and A[p,-1] != 0:
                    if 0 <= i <= (slackStart - 1):
                        print("x",i+1, "is equal to", A[p,-1])
                        solution.write("x")
                        solution.write(str(i+1))
                        solution.write(" is equal to: ")
                        solution.write(str(A[p,-1]))
                        solution.write("\n")
                    if slackStart <= i <= (slackStart + constraintLine-1):
                        print("s", i-slackStart+1, "is equal to", A[p,-1]) #could have error not sure about slackstart+1
                        solution.write("s")
                        solution.write(str(i-slackStart+1))
                        solution.write(" is equal to: ")
                        solution.write(str(A[p,-1]))
                        solution.write("\n")

                    if slackStart + constraintLine <= i <= (slackStart + (constraintLine*2)-1):
                        print("a", (i - (slackStart+constraintLine)), "is equal to", A[p,-1])
                        solution.write("a")
                        solution.write(str(i - (slackStart+constraintLine)))
                        solution.write(" is equal to: ")
                        solution.write(str(A[p,-1]))
                        solution.write("\n")
    solution.write("The rest of the variables are equal to: 0 \n")
    solution.write("Solution (z) is equal to: ")
    solution.write(str(A[-1,-1]))
    solution.write("\n")

def IndentifyOptima(A):
    #get tableau
    #check if function in obj row is 0 for x's, s's and a's

    multipleOptima = False
    #do the simplex method for that column
    #check if function in obj row is 0 for x's, s's and a's
    for i in range(len(A)-1):
        columnToPivot=-1
        if A[-1,i] == 0:
            #check if var is non-basic (not unit vector)
            column = A[:,i]
            sortedColumn = np.sort(column)
            for q in range(len(sortedColumn)-1):
                #make sure unit column
                if(sortedColumn[q] != 0 and sortedColumn[len(sortedColumn)-1] != 1):
                    #solution is not unique

                    multipleOptima = True

    if multipleOptima ==  True:
        print("Solution not unique")
        solution.write("Solution is not unique (multiple optima present) \n")
    else:
        solution.write("Solution is unique \n")

            
            
pivot(baseTableau,0)

np.set_printoptions(suppress=True)
print("final tableau:")
print(np.around(baseTableau,3)) #rounding

IndentifyOptima(baseTableau)

getResults(baseTableau)

output.close()
solution.close()






