from random import randint
import time
start_time = time.clock()

DATA_LENGTH = 32
error_position = list()
def generate_data(length):
    return [randint(0,1) for x in xrange(length)]

def generate_error():
    #num = raw_input("Enter how many error you want:")
    num = 1
    for i in range(int(num)):
        #n = raw_input("Error position :")
        n=4
        error_position.append(int(n))
    return error_position,num

def BinarytoDecimal(chromosome):
    decimal = 0
    for digit in chromosome:
        decimal = decimal*2 + int(digit)
    return decimal


def binary_addition(Op1,Op2):
    op1 = BinarytoDecimal(Op1)
    op2 = BinarytoDecimal(Op2)
    result = op1+op2
    #print result
    binary =[int(x) for x in bin(result)[2:]]
    if(len(binary)<5):
        binary=[0]+binary[0:]
    return binary[0:5]

def generate_decimal_parity(data):
    p1=binary_addition(data[0:4],data[8:12])
    p2=binary_addition(data[4:8],data[12:16])
    p3=binary_addition(data[16:20],data[24:28])
    p4=binary_addition(data[20:24],data[28:])
    
    a1=data[0:16]
    a2=data[16:32]
    p5=[]
    for i in range(16):
        if a1[i]==a2[i]:
            p5.append(0)
        else:
            p5.append(1)
    return p1+p2+p3+p4,p5

def generate_parity(data):
    a1=data[0:4]
    a2=data[4:8]
    parity1=[]
    for i in range(4):
        if a1[i]==a2[i]:
            parity1.append(0)
        else:
            parity1.append(1)


    a1=data[8:12]
    a2=data[12:16]
    parity2=[]
    for i in range(4):
        if a1[i]==a2[i]:
            parity2.append(0)
        else:
            parity2.append(1)

    a1=data[16:20]
    a2=data[20:24]
    parity3=[]
    for i in range(4):
        if a1[i]==a2[i]:
            parity3.append(0)
        else:
            parity3.append(1)
            
    a1=data[24:28]
    a2=data[28:32]
    parity4=[]
    for i in range(4):
        if a1[i]==a2[i]:
            parity4.append(0)
        else:
            parity4.append(1)

    a1=data[0:16]
    a2=data[16:32]
    parity5=[]
    for i in range(16):
        if a1[i]==a2[i]:
            parity5.append(0)
        else:
            parity5.append(1)

    return parity1+parity2+parity3+parity4,parity5

def correction(r1,c1,r2,c2,Error_Data):
    a1=r1[0:]
    a2=r2[0:]
    sr=[]
    for i in range(20):
        if a1[i] == a2[i]:
            sr.append(0)
        else:
            sr.append(1)

    b1=c1[0:]
    b2=c2[0:]
    sc=[]
    for i in range(16):
        if b1[i]==b2[i]:
            sc.append(0)
        else:
            sc.append(1)    
    Data=Error_Data[0:]
    if(BinarytoDecimal(sr[0:5])!=0):
        correct=[Error_Data[0]^sc[0],Error_Data[1]^sc[1],Error_Data[2]^sc[2],Error_Data[3]^sc[3]]
        Data=correct[0:4]+Data[4:]
        
        correct=[Error_Data[8]^sc[8],Error_Data[9]^sc[9],Error_Data[10]^sc[10],Error_Data[11]^sc[11]]
        Data=Data[0:8]+correct[0:]+Data[12:]

    if(BinarytoDecimal(sr[5:10])!=0):
        correct=[Error_Data[4]^sc[4],Error_Data[5]^sc[5],Error_Data[6]^sc[6],Error_Data[7]^sc[7]]
        Data=Data[0:4]+correct[0:]+Data[8:]

        correct=[Error_Data[12]^sc[12],Error_Data[13]^sc[13],Error_Data[14]^sc[14],Error_Data[15]^sc[15]]
        Data=Data[0:12]+correct[0:]

    if(BinarytoDecimal(sr[10:15])!=0):
        correct=[Error_Data[16]^sc[0],Error_Data[17]^sc[1],Error_Data[18]^sc[2],Error_Data[19]^sc[3]]
        Data=Data[0:16]+correct[0:4]+Data[20:]
        
        correct=[Error_Data[24]^sc[8],Error_Data[25]^sc[9],Error_Data[26]^sc[10],Error_Data[27]^sc[11]]
        Data=Data[0:24]+correct[0:]+Data[28:]

    if(BinarytoDecimal(sr[15:20])!=0):
        correct=[Error_Data[20]^sc[4],Error_Data[21]^sc[5],Error_Data[22]^sc[6],Error_Data[23]^sc[7]]
        Data=Data[0:20]+correct[0:]+Data[24:]

        correct=[Error_Data[28]^sc[12],Error_Data[29]^sc[13],Error_Data[30]^sc[14],Error_Data[31]^sc[15]]
        Data=Data[0:28]+correct[0:]

    return Data
    
Data = generate_data(DATA_LENGTH)
Data=[1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1]
row1,col1=generate_decimal_parity(Data)
int_list,number=generate_error()
Error_Data=Data[:]
for i in int_list:
    #print i
    if Error_Data[i]==1:
        Error_Data[i]=0
    else:
        Error_Data[i]=1
        
row2,col2= generate_decimal_parity(Error_Data)  
Data1=correction(row1,col1,row2,col2,Error_Data)

#print row1,col1
#print row2,col2

print Data
print Error_Data
print Data1

print time.clock() - start_time, "seconds"




