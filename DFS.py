import numpy as np
import math
# a function that generate goals state for size of matrix(al 0s)
def generategoalstate(dimension):
    mygoalstate = ''
    for i in range(dimension ** 2):
        mygoalstate += '0'
    return mygoalstate

# method to reverse bits, 0 to 1 and 1 to 0
def reversevalue(bit):
    if(bit=='1'):
        bit='0'
    elif (bit=='0'):
         bit='1'
    return bit

# a method to generate children of a node and put them in the list for DFS
def generatechildren(parent,grandparent,depth):
    myparent=list(parent)
    children=[]
    sizeofmatrix=len(parent)
    dimension=int(math.sqrt(sizeofmatrix))
    for j in range(len(parent)):
            copy=list(myparent)
            # flipping the left most column except the fir and last row
            if((j% (dimension)== 0) and (j>=dimension) and (j<(sizeofmatrix-dimension))):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            #flipping the first element
            elif((j==0)):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
            #flipping the left most element of the last row
            elif(j==(sizeofmatrix-dimension)):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            #filliping inner elements
            elif (((j%dimension)!= (dimension-1)) and((j%dimension)!=0) and (j>=dimension) and (j<(sizeofmatrix-dimension))):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j-1]=reversevalue(myparent[j - 1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            #first row
            elif(((j%dimension)!= (dimension-1)) and((j%dimension) !=0) and (j<dimension)):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j-1]=reversevalue(myparent[j - 1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
            elif(((j%dimension)!= (dimension-1)) and((j%dimension) !=0) and (j> (sizeofmatrix-dimension))):
                copy[j]=reversevalue(myparent[j])
                copy[j+1]=reversevalue(myparent[j + 1])
                copy[j-1]=reversevalue(myparent[j - 1])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            #flipping the last column
            elif(((j%dimension)==(dimension-1)) and (j>dimension) and (j<sizeofmatrix-dimension)):
                copy[j]=reversevalue(myparent[j])
                copy[j-1]=reversevalue(myparent[j-1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            elif((j==(dimension -1))):
                copy[j]=reversevalue(myparent[j])
                copy[j-1]=reversevalue(myparent[j - 1])
                copy[j+dimension]=reversevalue(myparent[j + dimension])
            elif(j==(sizeofmatrix-1)):
                copy[j]=reversevalue(myparent[j])
                copy[j-1]=reversevalue(myparent[j - 1])
                copy[j-dimension]=reversevalue(myparent[j - dimension])
            myflipchar=chr(j//dimension+65)+str(1+j%dimension)
            if(''.join(copy)!=(grandparent)):
                children.append([''.join(copy),parent,depth+1,myflipchar])
    children.sort(reverse=True)
    return children


# method to check value of a node
def checkvalueofnode(node,list):
    for i in list:
        if(node[0]==i[0]):
            return True
    return False

#depth first search method
def DFS(root,limit,goalstate):
    open=[root]
    close=[]
    node=root
    if(node[0]==goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate!=node[0])):
        node=open.pop()
        if( not checkvalueofnode(node,close)):
            close.append(node)
            if(node[2]<limit):
                children=generatechildren(node[0],node[1],node[2])
                for child in children:
                    if( not checkvalueofnode(child,open)):
                        open.append(child)
    return close

#method used for finding parent of nodes in solution path
def checkkey(key,list):
    mynode=[]
    for i in list:
        if (i[0]==key):
            mynode=i
            return mynode
    return False
# method that generates solution path
def generatesolutionpath(close):
    solutionpath=[]
    mynode=close[len(close)-1]
    while(mynode[1]!='' and mynode!=False):
        solutionpath.append([mynode[0],mynode[3]])
        mynode=checkkey(mynode[1],close)
    solutionpath.append([mynode[0],mynode[3]])
    solutionpath.reverse()
    return solutionpath

# method that checks if the solution exists
def checkifsolution(mypath,goalstate):
    solutionfound=False
    if(goalstate==mypath[len(mypath)-1][0]):
        solutionfound=True
    return solutionfound

#writing solution path on a text file
def writesolutionDFS(mypath,goalstate,name):
    f1= open(name,"w+")
    if(checkifsolution(mypath,goalstate)):
        for i in range(len(mypath)):
             f1.write(mypath[i][1]+" "+mypath[i][0]+"\n")
    else:
        f1.write("no solution")
    f1.close()

# method that writes the search path on text file
def writesearchpathDFS(mylist, name):
    f2 = open(name, "w+")
    for i in range(len(mylist)):
        f2.write('0' + " " + '0' + " " + '0' + " " + mylist[i][0] + "\n")
    f2.close()

# main method that read input file and run the code
def IndonesianDotPuzzleDFS(testfile):
    # list containing of test cases
    testcases = []

    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
             testcases.append(line)

            # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):
        
        if(i<(len(testcases)-1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()

    for i in range(len(testcases)):
        dimension = int(testcases[i][0])
        root = [testcases[i][3], '', 1, '0']
        goalstate = generategoalstate(dimension)
        limit = int(testcases[i][1])
        mycloselist = DFS(root, limit, goalstate)
        mysolutionpath = generatesolutionpath(mycloselist)
        solutionname = str(i) + "_dfs_solution.txt"
        searchname = str(i) + "_dfs_search.txt"
        writesolutionDFS(mysolutionpath, goalstate, solutionname)
        writesearchpathDFS(mycloselist, searchname)
        f.close()

IndonesianDotPuzzleDFS('test.txt')