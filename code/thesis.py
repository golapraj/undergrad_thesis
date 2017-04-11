from random import randint

DATA_LENGTH = 64
error_position = list()

def generate_data(length):
    return [randint(0,1) for x in xrange(length)]

def generate_parity(data):
    length = len(data)
    parity = []
    sucp = 0
    for i in range(length):
        sucp = data[i]^sucp
        parity.append(sucp)
    return parity

def generate_CB_parity(parity):
    P=[]
    for i in range(8):
        A=parity[i]^parity[i+8]^parity[i+16]^parity[i+24]^parity[i+32]^parity[i+40]^parity[i+48]^parity[i+56]
        P.append(A)
    return P
        
def generate_error():
    num = raw_input("Enter how many error you want:")
    for i in range(int(num)):
        n = raw_input("Error position :")
        error_position.append(int(n))
    print error_position

def detect_error(received_codeword):
    data = received_codeword[:DATA_LENGTH]
    original_parity = received_codeword[DATA_LENGTH:]
    calculated_parity = generate_parity(data)
    error_position = []
    display("After Error Data, D~~",data)
    display("After Error Parity, B",calculated_parity),"\n"

    for i in range(0,DATA_LENGTH):
        if original_parity[i] != calculated_parity[i]:
            error_position.append(i)
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0
        else:
            None
        calculated_parity = generate_parity(data)
        #print "At step",i+1,"D :",dis(data),"B :",dis(calculated_parity)
    return error_position

def display(message,array,separator = 0):
    if separator == 0:
        string = ''.join(str(i) for i in array)
        print message,":",string
    else:
        string = ','.join(str(i) for i in array)
        print message,":",string


def dis(array):
    string = ''.join(str(i) for i in array)
    return string
def evaluation():
    Data = generate_data(DATA_LENGTH)      
    Parity = generate_parity(Data)
    P = generate_CB_parity(Parity)
    #print "CHECK", Parity[0],Parity[8],Parity[16],Parity[24],Parity[32],Parity[40],Parity[48],Parity[56]
    #print "CB PARITY:",P
    Code_Word = Data + Parity

    display("Original Data, D~~~~~",Data)
    display("Original Parity, A~~~",Parity)
    display("Original Code Word, C",Code_Word)

    print "Enter Choice\n 1. Random\n 2. Manual\n"
    Choice = input("Enter a Choice: ")

    if Choice==1:
        Error_Data = generate_data(DATA_LENGTH)
    elif Choice==2:
        generate_error()
        Error_Data=Data
        for i in error_position:
            if Error_Data[i]==1:
                Error_Data[i]=0
            else:
                Error_Data[i]=1
                
    Error_Code_Word = Error_Data + Parity
    display("Error Code Word~~~~~~",Error_Code_Word)
    
    Error_Position = detect_error(Error_Code_Word)
    display("\nError Bit Position",Error_Position,separator=1)

def evaluation_file():

    with open("new.txt") as f:
        for line in f:
            int_list = [int(i) for i in line.split()]
            print int_list
            Data = generate_data(DATA_LENGTH)      
            Parity = generate_parity(Data)
            Code_Word = Data + Parity

            display("Original Data, D~~~~~",Data)
            display("Original Parity, A~~~",Parity)
            display("Original Code Word, C",Code_Word)

            Error_Data=Data
            for i in int_list:
                #print i
                if Error_Data[i]==1:
                    Error_Data[i]=0
                else:
                    Error_Data[i]=1
                        
            Error_Code_Word = Error_Data + Parity
            display("Error Code Word~~~~~~",Error_Code_Word)
            Error_Position = detect_error(Error_Code_Word)
            display("\nError Bit Position",Error_Position,separator=1)


print "Enter Error Injection Source\n 1. Keyboard\n 2. txt File\n"
Source = input("Enter a Choice: ")
if Source==1:
    n = input("How many evaluation: ")
    for i in range(n):
        evaluation()
elif Source==2:
    evaluation_file()
else:
    print "Wrong Choice!"
