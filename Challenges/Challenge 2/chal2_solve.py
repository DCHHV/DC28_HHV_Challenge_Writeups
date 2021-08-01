import re # import regex library

flag = [''] * 50 # create a buffer to act as our EEPROM

with open('chal2.csv') as fs:
    lines = fs.readlines()[1:] # first line is titles, so skip it
    for index, line in enumerate(lines[::3]): # every 3 lines is the i2c destination

        # Parse i2c destination address
        # 5.795815500000000,I2C,Setup Write to ['8' (0x08)] + ACK
        destStr = re.findall(r'0x[0-9a-fA-F]+', line) # find address with 0x start
        destAddr = int(destStr[0],16)
        if destAddr == 8: # check if this is meant for i2c address 8

            # Parse memory index
            # 5.795946000000000,I2C,'5' (0x05) + ACK
            memIndexLine = lines[index*3+1] # get next line with memory storage location
            memIndexStr = re.findall(r'0x[0-9a-fA-F]+', memIndexLine) # find address with 0x start
            memIndex = int(memIndexStr[0], 16)

            # Parse flag character
            # 5.796052000000000,I2C,f (0x66) + ACK
            memCharLine = lines[index*3+2].split(',') # get line after with character to store
            memChar = memCharLine[2][0] # character is immediately after the 2nd comma

            # Store character at intended memory index order
            flag[memIndex] = memChar

# Profit
print(''.join(flag))