import numpy as np
import math
import heapq
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


###################################
###################################
###################################
# method for checking value of node BFS
def checkvalueofnodeBFS(node,list):
    for i in list:
        if(node[1]==i[1]):
            return True
    return False

# a method to calculate heuristic value
def calculateh(mystring):
    count=0
    for i in range(len(mystring)):
        if(mystring[i]=='1'):
            count+=1
    return count

def calculateh2(mystring,dimension):
    count=0
    count2=calculateh(mystring)
    sizeofmatrix = len(mystring)
    copy = list(mystring)

    for i in range(len(mystring)):
        if ((i % (dimension) == 0) and (i >= dimension) and (i < (sizeofmatrix - dimension))):
            if((copy[i]=='1') and(copy[i+1]=='0') and(copy[i-dimension]=='0') and(copy [i+dimension]=='0')):
                count+=3
            if (((copy[i] == '1') and (copy[i + 1] == '1') and (copy[i - dimension] == '0') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '0') and (copy[i + dimension] == '1')) ):
                count+=2
            if (((copy[i] == '1') and (copy[i + 1] == '1') and (copy[i - dimension] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '1') and (copy[i + dimension] == '1')) or ((copy[i] == '1') and (copy[i + 1] == '1') and (copy[i - dimension] == '0') and (copy[i + dimension] == '1'))):
                count+=1
        elif(i==0):
            if((copy[i]=='1') and(copy[i+1]=='0') and (copy[i+dimension]=='0')):
                count+=2
            if ((copy[i] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '1')):
                count+=1
            if ((copy[i] == '1') and (copy[i + 1] == '1') and (copy[i + dimension] == '0')):
                count+=1
        elif (i == (sizeofmatrix - dimension)):
            if((copy[i]=='1') and (copy[i+1]=='0') and (copy[i-dimension]=='0')):
                count+=2
            if ((copy[i] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '1')):
                count += 1
            if ((copy[i] == '1') and (copy[i + 1] == '1') and (copy[i - dimension] == '0')):
                count += 1

        elif (((i % dimension) != (dimension - 1)) and ((i % dimension) != 0) and (i >= dimension) and (i < (sizeofmatrix - dimension))):
            if((copy[i]=='1') and (copy[i-1]=='0') and (copy[i+1]=='0') and (copy[i+dimension]=='0') and (copy[i-dimension]=='0')):
                count+=4
            if (((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and (copy[i + dimension] == '0') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and (copy[i + dimension] == '1') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '0') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '0') and (copy[i - dimension] == '0'))):
                count+=3
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '0') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '1') and (copy[i - dimension] == '0')) or ( (copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '1') and (copy[i + dimension] == '0') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '0') and (copy[i - dimension] == '1')) or((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '1') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and (copy[i + dimension] == '1') and (copy[i - dimension] == '1'))):
                count+=2
            if (((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '1') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '1') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '1') and (copy[i + dimension] == '0') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '1') and (copy[i + dimension] == '1') and (copy[i - dimension] == '0'))):
                count+=1

        elif (((i % dimension) != (dimension - 1)) and ((i % dimension) != 0) and (i< dimension)):
            if((copy[i]=='1') and (copy[i-1]=='0') and (copy[i+1]=='0') and(copy[i+dimension]=='0')):
                count+=3
            if(((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and (copy[i + dimension] == '1'))) :
                count+=2
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i + dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i + dimension] == '1'))):
                count+=1

        elif (((i % dimension) != (dimension - 1)) and ((i % dimension) != 0) and (i > (sizeofmatrix-dimension))):
            if((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and (copy[i - dimension] == '0')):
                count+=3
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '0') and ( copy[i - dimension] == '1'))):
                count+=2
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '1') and (copy[i - dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + 1] == '0') and (copy[i - dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + 1] == '1') and (copy[i - dimension] == '1'))):
                count+=1

        elif (((i % dimension) == (dimension - 1)) and (i > dimension) and (i < sizeofmatrix - dimension)):
            if ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i - dimension] == '0') and (copy[i + dimension] == '0')):
                count += 3
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i - dimension] == '0') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i - dimension] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i - dimension] == '0') and (copy[i + dimension] == '1'))):
                count += 2
            if (((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i - dimension] == '1') and (copy[i + dimension] == '0')) or ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i - dimension] == '1') and (copy[i + dimension] == '1')) or ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i - dimension] == '0') and (copy[i + dimension] == '1'))):
                count += 1
        elif ((i == (dimension - 1))):
            if((copy[i]=='1') and (copy[i-1]=='0') and (copy [i+dimension]=='0')):
                count+=2
            if ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i + dimension] == '0')):
                count += 1
            if ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i + dimension] == '1')):
                count += 1

        elif (i == (sizeofmatrix - 1)):
            if((copy[i]=='1') and (copy[i-1]=='0') and (copy[i-dimension]=='0')):
                count+=2
            if ((copy[i] == '1') and (copy[i - 1] == '1') and (copy[i - dimension] == '0')):
                count += 1
            if ((copy[i] == '1') and (copy[i - 1] == '0') and (copy[i - dimension] == '1')):
                count += 1

    count3=count+count2
    return count3



# a method to generate children of a node and put them in the list
def generatechildrenBFS(parent,grandparent,depth,h):
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
            heuristic=int(calculateh(''.join(copy)))
            myflipchar=chr(j//dimension+65)+str(1+j%dimension)
            if(''.join(copy)!=(grandparent)):
                children.append([heuristic,''.join(copy),parent,depth+1,myflipchar])
    children.sort(reverse=True)
    return children

def checkkeyBFS(key,list):
    mynode=[]
    for i in list:
        if (i[1]==key):
            mynode=i
            return mynode
    return False

def BFS(root,limit,goalstate):
    open=[root]
    close=[]
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate != node[1]) and (len(close)<limit)):
        node = open.pop()
        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)
            if(len(close)<=limit):
                children=generatechildrenBFS(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        open.append(child)
            open.sort(reverse=True)
    return close


def generatesolutionpathBFS(close):
    solutionpath=[]
    mynode=close[len(close)-1]
    while(mynode[2]!=''):
        solutionpath.append([mynode[1],mynode[4]])
        mynode=checkkeyBFS(mynode[2],close)
    solutionpath.append([mynode[1],mynode[4]])
    solutionpath.reverse()
    return solutionpath

def checkifsolutionBFS(mypath,goalstate):
    solutionfound=False
    for i in range(len(mypath)):
        if(goalstate==mypath[i][0]):
            solutionfound=True
    return solutionfound

def writesolutionBFS(mypath,goalstate,name):
    f1= open(name,"w+")
    if(checkifsolutionBFS(mypath,goalstate)):
        for i in range(len(mypath)):
             f1.write(mypath[i][1]+" "+mypath[i][0]+"\n")
    else:
        f1.write("no solution")
    f1.close()

def writesearchpathBFS(mylist,name):
    f2= open(name,"w+")
    for i in range(len(mylist)):
         f2.write(str(mylist[i][0])+" "+'0'+" "+str(mylist[i][0])+" "+mylist[i][1]+"\n")
    f2.close()

def IndonesianDotPuzzleBFS(testfile):
    # list containing of test cases
    testcases = []
    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)
    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):

        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()


    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialh=int(calculateh(testcases[i][3]))
        root = [initialh,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=BFS(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_bfs_solution(h1).txt"
        searchname1=str(i)+"_bfs_search(h1).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathBFS(mycloselist,searchname1)
        f.close()


########################################
########################################
########################################





def generatechildrenAstar(parent,grandparent,depth,f):
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
            heuristic=int(calculateh(''.join(copy)))
            function=int(heuristic+depth+1)
            myflipchar=chr(j//dimension+65)+str(1+j%dimension)
            if(''.join(copy)!=(grandparent)):
                children.append([function,''.join(copy),parent,depth+1,myflipchar])
    children.sort(reverse=True)
    return children


def Astar(root,limit,goalstate):
    open=[root]
    close=[]
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate!=node[1]) and (len(close)<limit)):
        node=open.pop()

        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)

            if(len(close)<=limit):
                children=generatechildrenAstar(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        open.append(child)
            open.sort(reverse=True)

    return close

def writesearchpathAstar(mylist,name):
    f2= open(name,"w+")
    for i in range(len(mylist)):
         f2.write(str(mylist[i][0])+" "+str(mylist[i][3])+" "+str(int(mylist[i][0])-int(mylist[i][3]))+" "+mylist[i][1]+"\n")
    f2.close()



def IndonesianDotPuzzleAstar(testfile):
    # list containing of test cases
    testcases = []

    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)

    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):
        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()

    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialf=1+int(calculateh(testcases[i][3]))
        root = [initialf,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=Astar(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_astar_solution(h1).txt"
        searchname1=str(i)+"_astar_search(h1).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathAstar(mycloselist,searchname1)
        f.close()


#######################################
#######################################



def generatechildrenBFS2(parent,grandparent,depth,h):
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
            heuristic=int(calculateh2(''.join(copy),dimension))
            myflipchar=chr(j//dimension+65)+str(1+j%dimension)
            if(''.join(copy)!=(grandparent)):
                children.append([heuristic,''.join(copy),parent,depth+1,myflipchar])
    children.sort(reverse=True)
    return children

def BFS2(root,limit,goalstate):
    open=[root]
    close=[]
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate != node[1]) and (len(close)<limit)):
        node = open.pop()
        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)
            if(len(close)<=limit):
                children=generatechildrenBFS2(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        open.append(child)
            open.sort(reverse=True)
    return close

def IndonesianDotPuzzleBFS2(testfile):
    # list containing of test cases
    testcases = []
    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)
    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):

        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()


    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialh=int(calculateh2(testcases[i][3],dimension))
        root = [initialh,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=BFS2(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_bfs_solution(h2).txt"
        searchname1=str(i)+"_bfs_search(h2).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathBFS(mycloselist,searchname1)
        f.close()

########################################
########################################
########################################

def generatechildrenAstar2(parent,grandparent,depth,f):
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
            heuristic=int(calculateh2(''.join(copy),dimension))
            function=int(heuristic+depth+1)
            myflipchar=chr(j//dimension+65)+str(1+j%dimension)
            if(''.join(copy)!=(grandparent)):
                children.append([function,''.join(copy),parent,depth+1,myflipchar])
    children.sort(reverse=True)
    return children

def Astar2(root,limit,goalstate):
    open=[root]
    close=[]
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate!=node[1]) and (len(close)<limit)):
        node=open.pop()

        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)

            if(len(close)<=limit):
                children=generatechildrenAstar2(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        open.append(child)
            open.sort(reverse=True)

    return close

def IndonesianDotPuzzleAstar2(testfile):
    # list containing of test cases
    testcases = []

    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)

    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):
        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()

    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialf=1+int(calculateh2(testcases[i][3],dimension))
        root = [initialf,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=Astar2(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_astar_solution(h2).txt"
        searchname1=str(i)+"_astar_search(h2).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathAstar(mycloselist,searchname1)
        f.close()
###############
###############
#################
def Astar3(root,limit,goalstate):
    open=[root]
    heapq.heapify(open)
    close=[]
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate!=node[1]) and (len(close)<limit)):
        node=heapq.heappop(open)

        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)

            if(len(close)<=limit):
                children=generatechildrenAstar2(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        heapq.heappush(open,child)


    return close



#########################
######################
def IndonesianDotPuzzleAstar3(testfile):
    # list containing of test cases
    testcases = []

    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)

    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):
        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()

    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialf=1+int(calculateh2(testcases[i][3],dimension))
        root = [initialf,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=Astar3(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_astar_solution(h3).txt"
        searchname1=str(i)+"_astar_search(h3).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathAstar(mycloselist,searchname1)
        f.close()

def BFS3(root,limit,goalstate):
    open=[root]
    close=[]
    heapq.heapify(open)
    node=root
    if (node[1] == goalstate):
        close.append(node)
    while (len(open)>0 and (goalstate != node[1]) and (len(close)<limit)):
        node = heapq.heappop(open)
        if( not checkvalueofnodeBFS(node,close)):
            close.append(node)
            if(len(close)<=limit):
                children=generatechildrenBFS2(node[1],node[2],node[3],node[0])
                for child in children:
                    if( not checkvalueofnodeBFS(child,open)):
                        heapq.heappush(open,child)

    return close




def IndonesianDotPuzzleBFS3(testfile):
    # list containing of test cases
    testcases = []
    # reading the test file and store them line by line test cases
    with open(testfile) as f:
        for line in f:
            testcases.append(line)
    # processing line by line in suitable format, get rid of the '\n' at the end of each line, and split the contents by white space
    for i in range(len(testcases)):

        if (i < (len(testcases) - 1)):
            testcases[i] = testcases[i][:-1]
        testcases[i] = testcases[i].split()


    for i in range(len(testcases)):
        dimension=int(testcases[i][0])
        initialh=int(calculateh2(testcases[i][3],dimension))
        root = [initialh,testcases[i][3],'',1,'0']
        goalstate = generategoalstate(dimension)
        limit=int(testcases[i][2])
        mycloselist=BFS3(root,limit,goalstate)
        mysolutionpath=generatesolutionpathBFS(mycloselist)
        solutionname1=str(i)+"_bfs_solution(h3).txt"
        searchname1=str(i)+"_bfs_search(h3).txt"
        writesolutionBFS(mysolutionpath,goalstate,solutionname1)
        writesearchpathBFS(mycloselist,searchname1)
        f.close()


def project1(mytest):
    IndonesianDotPuzzleDFS(mytest)
    IndonesianDotPuzzleBFS(mytest)
    IndonesianDotPuzzleBFS2(mytest)
    IndonesianDotPuzzleAstar(mytest)
    IndonesianDotPuzzleAstar2(mytest)
    '''IndonesianDotPuzzleBFS3(mytest)
    IndonesianDotPuzzleAstar3(mytest)'''

project1("test.txt")

#####################
##############
