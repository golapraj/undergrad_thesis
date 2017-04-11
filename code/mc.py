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
        n = 3
        error_position.append(int(n))
    return error_position,num

def BinarytoDecimal(chromosome):
    decimal = 0
    for digit in chromosome:
        decimal = decimal*2 + int(digit)
    return decimal

def sec_ded(data):
    C0=data[0]^data[1]^data[3]^data[4]^data[6]
    C1=data[0]^data[2]^data[3]^data[5]^data[6]
    C2=data[1]^data[2]^data[3]^data[7]
    C3=data[4]^data[5]^data[6]^data[7]
    C4=data[0]^data[1]^data[2]^data[3]^data[4]^data[5]^data[6]^data[7]
    return [C0,C1,C2,C3,C4]
def xor(data):
    P=0
    for i in data:
        P=P^i
    return [P]

def generate_parity(data):
    R0=sec_ded(data[0:8])
    R1=sec_ded(data[8:16])
    R2=sec_ded(data[16:24])
    R3=sec_ded(data[24:32])
    P0=xor([data[0],data[8],data[16],data[24]])
    P1=xor([data[1],data[9],data[17],data[25]])
    P2=xor([data[2],data[10],data[18],data[26]])
    P3=xor([data[3],data[11],data[19],data[27]])
    P4=xor([data[4],data[12],data[20],data[28]])
    P5=xor([data[5],data[13],data[21],data[29]])
    P6=xor([data[6],data[14],data[22],data[30]])
    P7=xor([data[7],data[15],data[23],data[31]])
    return R0+R1+R2+R3,P0+P1+P2+P3+P4+P5+P6+P7
def error_detection(r1,c1,r2,c2):
    a1=r1[0:]
    a2=r2[0:]
    sc=[]
    for i in range(20):
        if a1[i]==a2[i]:
            sc.append(0)
        else:
            sc.append(1)  

    b1=c1[0:]
    b2=c2[0:]
    sp=[]
    for i in range(8):
        if b1[i]==b2[i]:
            sp.append(0)
        else:
            sp.append(1)

    return sc,sp
    
Data = generate_data(DATA_LENGTH)
Data=[1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0]
row1,col1= generate_parity(Data)

int_list,number=generate_error()
Error_Data=Data[:]
for i in int_list:
    if Error_Data[i]==1:
        Error_Data[i]=0
    else:
        Error_Data[i]=1

row2,col2= generate_parity(Error_Data)

sc,sp=error_detection(row1,col1,row2,col2)

print Data
print Error_Data
#print row1,col1
#print row2,col2
#print sc
#print sp

print time.clock() - start_time, "seconds"




