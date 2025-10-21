def enter(collection, value, counter, length = 8):
    if not isinstance(value, str):
        if isinstance(value, int):
            value = bin(value)[2:]
        else:
            raise ValueError("Cannot convert to binary")
    
    while(len(value) < length):
        value = f'0{value}'

    value = f'{value[0:4]} {value[4:]}'
    value = value.strip()

    collection.append(f'{value} ({counter})')

def enter_RAM(REG, code, counter):
    value = read(REG)
    value = f'{value[0:4]} {value[4:]}'
    index = int(code,2)
    RAM[index] = value
    spaces = '  ' + ' '*len(str(index))
    RAM_OUT[index] = f'{RAM_OUT[index]}\n{spaces}{value} ({counter})'  

def read(collection,index=-1):
    last_item = str(collection[len(collection)-1 if index == -1 else index])
    return last_item[0:last_item.index("(") if "(" in last_item else len(last_item)].replace(" ","")

RAM = ["0001 1011",
"0010 1101",
"0111 0110",
"0010 1110",
"0101 0110",
"0110 0001",
"0011 1100",
"1111 0000",
"0000 0000",
"0000 0000",
"0000 0000",
"0000 1101",
"0000 0000",
"0000 0111",
"0000 0010",
"0000 0000"]
RAM_OUT = RAM.copy()
IR = []
IAR = []
REG_A = []
REG_B = []
REG_C = []
REG_D = []
FLAG_Z = []
FLAG_P = []
FLAG_N = []
FLAG_O = []

counter = 0
halt = False

while not halt:
    fetch = read(RAM, counter)
    optcode = fetch[0:4]
    code = fetch[4:8]
    print(f"{optcode} {code}")
    reg_a = None
    reg_b = None

    if optcode in ["0101", "0110", "0111", "1000", "1001", "1010"]:
        first = code[0:2]
        second = code[2:]
        reg_a = REG_A if first == "00" else REG_B if first == "01" else REG_C if first == "10" else REG_D if first == "11" else None
        reg_b = REG_A if second == "00" else REG_B if second == "01" else REG_C if second == "10" else REG_D if second == "11" else None  
    
    match optcode:
        case "0000":
            pass
        case "0001":
            enter(REG_A, read(RAM, int(code,2)), counter)
        case "0010":
            enter(REG_B, read(RAM, int(code,2)), counter)
        case "0011":
            enter_RAM(REG_A, code, counter)
        case "0100":
            enter_RAM(REG_B, code, counter)
        case "0101":
            enter(reg_a, int(int(read(reg_a),2)+int(read(reg_b),2)), counter)
        case "0110":
            enter(reg_a, int(int(read(reg_a),2)-int(read(reg_b),2)), counter)
        case "0111":
            enter(reg_b, read(reg_a), counter)
        case "1000":
            enter(reg_a, int(read(reg_a),2)+1, counter)
        case "1001":
            enter(reg_a, int(read(reg_a),2)-1, counter)
        case "1010":
            result = int(read(reg_a),2) - int(read(reg_b),2)
            if result == 0:
                enter(FLAG_Z, "1", counter, 1)
                enter(FLAG_N, "0", counter, 1)
                enter(FLAG_P, "0", counter, 1)
            elif result < 0:
                enter(FLAG_Z, "0", counter, 1)
                enter(FLAG_N, "1", counter, 1)
                enter(FLAG_P, "0", counter, 1)
            elif result > 0:
                enter(FLAG_Z, "0", counter, 1)
                enter(FLAG_N, "0", counter, 1)
                enter(FLAG_P, "1", counter, 1)
        case "1011":
            if(read(FLAG_P)=="1"):
                counter = int(code,2)-1
        case "1100":
            if(read(FLAG_N)=="1"):
                counter = int(code,2)-1
        case "1101":
            if(read(FLAG_Z)=="1"):
                counter = int(code,2)-1
        case "1110":
            counter = int(code,2)-1
        case "1111":
            halt = True

    counter += 1

print("\nRAM:")
for idx, x in enumerate(RAM_OUT):
    print(f'{idx}: {x}')
print("\nRegister A:")
for entry in REG_A:
    print(entry)
print("\nRegister B:")
for entry in REG_B:
    print(entry)
print("\nRegister C:")
for entry in REG_C:
    print(entry)
print("\nRegister D:")
for entry in REG_D:
    print(entry)
print("\nFlags:")
print("  Z\t  P\t  N")
for i in range(len(FLAG_Z)):
    print(f'{FLAG_Z[i]}\t{FLAG_P[i]}\t{FLAG_N[i]}')


