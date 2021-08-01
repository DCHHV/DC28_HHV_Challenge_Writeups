import re # import regex library

flag = [''] * 500 # create a buffer

with open('chal3.csv') as fs:
    lines = fs.readlines()[1:] # first line is titles, so skip it
    for index, line in enumerate(lines[::3]): # every 3 lines is the start of an exchange

        # Parse most sig bit of flag index
        # 0.319003300000000,SPI,MOSI: '0' (0x00);  MISO: '0' (0x00)
        MSBStr = re.findall(r'0x[0-9a-fA-F]+', line)[0] # find all hex values, we want the first
        MSB = int(MSBStr, 16)

        # Parse least sig bit of flag index
        LSBLine = lines[index*3+1] # get next line with LSB value
        LSBStr = re.findall(r'0x[0-9a-fA-F]+', LSBLine)[0] # find all hex values, we want the first
        LSB = int(LSBStr, 16)

        # Combine MSB and LSB for flag index
        flagIndex = MSB << 8 # bring together MSB and LSB for index
        flagIndex |= LSB
        
        # Parse flag character
        flagCharLine = lines[index*3+2] # get line after with flag character
        flagCharStr = re.findall(r'0x[0-9a-fA-F]+', flagCharLine)[1] # find all hex values, we want the second
        flagChar = chr(int(flagCharStr,16))

        # Store character at intended index
        flag[flagIndex] = flagChar

# Profit
print(''.join(flag))
