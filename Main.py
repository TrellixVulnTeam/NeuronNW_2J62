from Node import Node
import math
import random
from test import *

# initialize neural nw

# end initialize neural nw

def activationFunc(v):
    # print("V = ",v)
    y=1/(1+math.e**-v)

    return y

def dActivationfuction(y):
    x=y*(1-y)
    return x

def add_input(o1,o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_input(o2[j])
    return

def add_output(o1,o2):
    for i in range(o1.__len__()):
        for j in range(o2.__len__()):
            o1[i].add_output(o2[j])
    return

def feedfoward(arr):
    # start feed forward
    for i in range(arr.__len__()):
        arr[i].x=[]
        for j in range(arr[0].input.__len__()):
            arr[i].x.append(arr[i].input[j].y)
        # print("Input ",i," :",end=" ")
        # print(arr[i].x)

    # why append array in one object can affect to the others ??

    for i in range(arr.__len__()):
        sum=0
        # print("Input for v : ",arr[i].x)

        for j in range(arr[i].x.__len__()):
            sum+=arr[i].x[j]*arr[i].w[j]

        arr[i].v=sum+arr[i].bias
        arr[i].y=activationFunc(arr[i].v)

        # produce y form node

    # print("produce y form node\n",)
    return

def setWnew(node,i):

    for j in range(node[i].w.__len__()):
        # print(node[i].w[j],end="  ")
        node[i].w[j] += (node[i].gradient*node[i].x[j]*lr)
        # print("W'",j," from node",i,":",node[i].w[j])

    # print(node[i].bias,end="  ")
    node[i].bias += (node[i].gradient*1*lr)
    # print("Bias'"," from node",i,":",node[i].bias)
    return

def outputBPG(d,err):

    for i in range(outputNode.__len__()):
        # print("ERR =",d[i],"-",outputNode[i].y,"=",end=" ")
        err.append(d[i]-outputNode[i].y)
        # print(err[i])
        # find delta w from each output node
        outputNode[i].wo=outputNode[i].w
        outputNode[i].gradient=(-err[i]*dActivationfuction(outputNode[i].y))
        # save gradient and w old for hidden BPG
        setWnew(outputNode,i)

    # outputBPG done
    return

def hiddenBPG(hiddenNode):
    for i in range(hiddenNode.__len__()):
        # find delta w from each hidden node
        hiddenNode[i].wo=hiddenNode[i].w
        sum=0
        for j in hiddenNode[i].output:
            sum+=(j.gradient*j.wo[i])
        hiddenNode[i].gradient = (dActivationfuction(hiddenNode[i].y)*sum)
        # save w old for hiddenBPG
        setWnew(hiddenNode,i)
    # hiddenBPG done
    return

def train(data,ans):
    # start train
    for i in range(ans.__len__()):
        # print("\n\n\n*******Row ",i,"Start*****\n\n\n")
        for j in range(data[i].__len__()):
            inputNode[j].y=data[i][j]
        # start feed forward

        feedfoward(hiddenNode)
        feedfoward(outputNode)
        # stop feed forward

        # start back propagation # find error from each output node
        err=[]
        d=[]
        for j in range(outputNode.__len__()):
            d.append(ans[i])
        outputBPG(d,err)
        # print("\noutputBPG done\n")
        hiddenBPG(hiddenNode)

    # train done
    return

def test(data,ans):
    # start test
    correct=0
    for i in range(ans.__len__()):
        # print("\n\n\n*******Row ",i,"Start Test*****\n\n\n")
        for j in range(data[i].__len__()):
            inputNode[j].y=inputNode[j].x=data[i][j]
        # start feed forward
        feedfoward(hiddenNode)
        feedfoward(outputNode)
        # stop feed forward

        tmp=0
        for j in outputNode:
            tmp+=(j.y-ans[i])**2

        if(tmp**1/2 < ((0.5**2)*outputNode.__len__())**1/2):
            correct+=1

    # test done
    return correct

inputNode=[]
hiddenNode=[]
outputNode=[]

lr=0.1

data=readExel('Data.xls')
data=preprocess(data)

min = list(map(min, zip(*data)))
max = list(map(max, zip(*data)))

print(max)
print(min)

datatrain=data[0:int(data.__len__()*90/100)]
datatest=data[int(data.__len__()*90/100):]

ans=[]
for i in data :
    ans.append(int(i.pop(i.__len__()-1)))

anstest=ans[int(data.__len__()*90/100):]
ans=ans[0:int(data.__len__()*90/100)]

for i in range(data[0].__len__()):
    inputNode.append(Node(1,data[0][i]))
    inputNode[i].setW()
    inputNode[i].y=inputNode[i].x

print()

for i in range(3):
    hiddenNode.append(Node(random.uniform(0.5,1)))
    outputNode.append(Node(random.uniform(0.5,1)))

add_input(hiddenNode,inputNode)
add_output(inputNode,hiddenNode)

add_input(outputNode,hiddenNode)
add_output(hiddenNode,outputNode)

for i in range(3):
    hiddenNode[i].setW()
    outputNode[i].setW()

n=0
e=0

print(anstest.__len__())
while(n<10):
    train(datatrain,ans)
    c=test(datatest,anstest)
    n+=1
    print(n,c)
# save W' and Bias' of all node
#
with open("Output.txt", "w") as text_file:
    for i in range(hiddenNode.__len__()):
        print(f"Hidden Node ",i,",W' :",hiddenNode[i].w, file=text_file)
        print(f"Hidden Node ",i,",Bias' :",hiddenNode[i].bias, file=text_file)
        print(f"Output Node ",i,",W' :",outputNode[i].w, file=text_file)
        print(f"Output Node ",i,",Bias' :",outputNode[i].bias, file=text_file)
    print(n, file=text_file)



