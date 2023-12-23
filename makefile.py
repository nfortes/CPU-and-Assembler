####################################################################
# Lili Fortes and Sean Payba                                       #
# I pledge my honor that I have abided by the Stevens Honor System #
####################################################################

############################################################
# IMPLEMENTING IMAGE FILE CREATION FOR DATA MEMORY SEGMENT #
############################################################

import re

# opening the file
instruction_file = open('instructions.txt', 'r')

# reading the file
instructions = instruction_file.read()

# convert instructions into list
instruction_list = instructions.split('text')[1].split('.data')[0].split('\n')

# creates array of instructions with their inputs
instructionvalues = []

# creates a list of a list of each instruction's operation and instructionvalues
# e.g. [['ADD', 'X0', 'X0', 'X1'], ['SUB', 'X0', 'X1', 'X3']]
for i in instruction_list:
    current = i.split('//', 1)[0]
    current = current.replace(',', ' ').replace('[', '').replace(']', '')
    current = re.split(r'\s+', current)
    while('' in current):
        current.remove('')
    if current != []:
        instructionvalues += [current]

# opcode[0] is 0 if we are adding, 1 if we are subtracting
# opcode[1] is 1 if we are reading from memory (LDR instruction)
# opcode[2] is 1 if we are using an immediate
# opcode[3] is the value of Rd
# opcode[4] is the value of Rd
# opcode[5] is the value of Rn
# opcode[6] is the value of Rn
# opcode[7] is the value of Rm
# opcode[8] is the value of Rm
# opcode[9] is the value of immediate
# opcode[10] is the value of immediate
# opcode[11] is the value of immediate
# opcode[12] is the value of immediate
# opcode[13] is the value of immediate
# opcode[14] is the value of immediate
# opcode[15] is 1 if we are ending the program

opcodes = []

# bit extends
def extend(bin):
    while len(bin)<2:
        bin = '0' + bin
    return bin

# bit extends immediate
def extendimm(bin):
    while len(bin)<6:
        bin = '0' + bin
    return bin

def extendinstr(hex):
    while len(hex)<4:
        hex = '0' + hex
    return hex

# encodes operation in opcode
for i in instructionvalues:
    opcode = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1']
    match i[0].upper():
        case 'LDR':
            opcode[0] = '0' # adding
            opcode[1] = '1' # reading from mem
            rn = bin(int(i[2][1])).split('b')[1]
            rn = extend(rn)
            opcode[5] = rn[0] # Rn
            opcode[6] = rn[1] # Rn
            rd = bin(int(i[1][1])).split('b')[1]
            rd = extend(rd)
            opcode[3] = rd[0] # Rd
            opcode[4] = rd[1] # Rd
            if i[3][0].upper() == 'X': # if register
                opcode[2] = '0' # we are using register
                rm = bin(int(i[3][1])).split('b')[1]
                rm = extend(rm)
                opcode[7] = rm[0] # Rm
                opcode[8] = rm[1] # Rm
            else: # if immediate
                opcode[2] = '1' # we are using imm
                imm = bin(int(i[3])).split('b')[1] # imm
                imm = extendimm(imm)
                opcode[9] = imm[0]
                opcode[10] = imm[1]
                opcode[11] = imm[2]
                opcode[12] = imm[3]
                opcode[13] = imm[4]
                opcode[14] = imm[5]
        case 'ADD':
            opcode[0] = '0' # adding
            rd = bin(int(i[1][1])).split('b')[1]
            rd = extend(rd)
            opcode[3] = rd[0] # Rd
            opcode[4] = rd[1] # Rd
            rn = bin(int(i[2][1])).split('b')[1]
            rn = extend(rn)
            opcode[5] = rn[0] # Rn
            opcode[6] = rn[1] # Rn
            if i[3][0].upper() == 'X': # if register
                opcode[2] = '0' # we are using register
                rm = bin(int(i[3][1])).split('b')[1]
                rm = extend(rm)
                opcode[7] = rm[0] # Rm
                opcode[8] = rm[1] # Rm
            else: # if immediate
                opcode[2] = '1' # we are using imm
                imm = bin(int(i[3])).split('b')[1] # imm
                imm = extendimm(imm)
                opcode[9] = imm[0]
                opcode[10] = imm[1]
                opcode[11] = imm[2]
                opcode[12] = imm[3]
                opcode[13] = imm[4]
                opcode[14] = imm[5]
        case 'SUB':
            opcode[0] = '1' # subtracting
            rd = bin(int(i[1][1])).split('b')[1]
            rd = extend(rd)
            opcode[3] = rd[0] # Rd
            opcode[4] = rd[1] # Rd
            rn = bin(int(i[2][1])).split('b')[1]
            rn = extend(rn)
            opcode[5] = rn[0] # Rn
            opcode[6] = rn[1] # Rn
            if i[3][0].upper() == 'X': # if register
                opcode[2] = '0' # we are using register
                rm = bin(int(i[3][1])).split('b')[1]
                rm = extend(rm)
                opcode[7] = rm[0] # Rm
                opcode[8] = rm[1] # Rm
            else: # if immediate
                opcode[2] = '1' # we are using imm
                imm = bin(int(i[3])).split('b')[1] # imm
                imm = extendimm(imm)
                opcode[9] = imm[0]
                opcode[10] = imm[1]
                opcode[11] = imm[2]
                opcode[12] = imm[3]
                opcode[13] = imm[4]
                opcode[14] = imm[5]
    opcodes += [opcode]

# open file to write to
executable_file = open('imagefile', 'w')


# go through every opcode and create it in image file
added = 0
executable_file.write('v3.0 hex words addressed\n00: ')
for i in opcodes:
    i = ''.join(i)
    print(i)
    i = int(i, 2)
    i = hex(i).split('x')[1]
    i = extendinstr(i)
    for j in i:
        executable_file.write(j)
        added+=1
        if added%4==0:
            executable_file.write(" ")
        if added%64 == 0:
            executable_file.write('\n' + hex(added//4).split('x')[1] + ": ")

############################################################
# IMPLEMENTING IMAGE FILE CREATION FOR DATA MEMORY SEGMENT #
############################################################

# opening the file
instruction_file = open('instructions.txt', 'r')

# reading the file
instructions = instruction_file.read()

if '.data' in instructions:
    # convert instructions into list
    data_list = instructions.split('.data')[1].split('\n')

    # list of all mnemonics and values
    addressmemory = []

    for i in data_list:
        current = i.split('//', 1)[0]
        current = current.replace(',', ' ')
        current = re.split(r'\s+', current)
        while('' in current):
            current.remove('')
        if current != []:
            addressmemory += [current]

    # largest address we are trying to add to
    data_size = int(addressmemory[-1][0][:-1]) + len(addressmemory[-1])

    # list of all the data
    data = []

    for i in range(0,data_size-1):
        data.insert(i, 0)

    for i in addressmemory:
        address = int(i[0][:-1])
        for j in range(1, len(i)):
            data[address] = int(i[j])
            address += 1

    # open file to write to
    executable_file = open('memoryimage', 'w')

    # go through every opcode and create it in image file
    added = 0
    executable_file.write('v3.0 hex words addressed\n00: ')
    for i in data:
        i = hex(i).split('x')[1]
        i = extend(i)
        executable_file.write(i + ' ')
        added+=1
        if added%16 == 0:
            executable_file.write('\n' + hex(added).split('x')[1] + ": ")
