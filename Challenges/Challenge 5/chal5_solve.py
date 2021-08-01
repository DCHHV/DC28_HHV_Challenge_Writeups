# XOR function
def XOR(inA, inB):
    return (int(inA) ^ int(inB))

# Invert function
def INV(inA):
    return int(not int(inA))

# Simulated 6 in / 6 out inverter
def SN74ALS04N(in1A, in2A, in3A, in4A, in5A, in6A):
    out1 = INV(in1A)
    out2 = INV(in2A)
    out3 = INV(in3A)
    out4 = INV(in4A)
    out5 = INV(in5A)
    out6 = INV(in6A)
    return out1, out2, out3, out4, out5, out6

# Simulated quad XOR
def SN74LS86N(in1A, in1B, in2A, in2B, in3A, in3B, in4A, in4B):
    out1 = XOR(in1A, in1B)
    out2 = XOR(in2A, in2B)
    out3 = XOR(in3A, in3B)
    out4 = XOR(in4A, in4B)
    return out1, out2, out3, out4

# Simulated logic operations for challenge 5 PCB
def decode(data):
    IC11Y, IC12Y, IC13Y, IC14Y, IC15Y, IC16Y = SN74ALS04N(data[0],data[6],data[4],data[8],data[10],data[2])
    IC21Y, IC22Y, IC23Y, IC24Y = SN74LS86N(IC14Y,data[13],IC15Y,data[9],data[12],data[11],data[15],data[14])
    IC31Y, IC32Y, IC33Y, IC34Y = SN74LS86N(IC11Y,data[1],IC16Y,data[3],data[5],IC13Y,data[7],IC12Y)
    IC41Y, IC42Y, IC43Y, IC44Y, IC45Y, IC46Y = SN74ALS04N(data[14],IC24Y,IC22Y,IC23Y,data[12],IC21Y)
    out = [IC31Y,IC16Y,IC15Y,IC13Y,IC33Y,IC41Y,IC42Y,IC45Y,IC43Y,IC44Y,IC46Y,IC14Y,IC32Y,IC34Y,IC12Y,IC11Y]
    return out

# Fix pin order to be ABC...
def fixPinOrder(PCBIn):
    # AMKHUSTGFEDRPCNB
    # 0123456789012345
    outFix = [PCBIn[0],PCBIn[15],PCBIn[13],PCBIn[10],PCBIn[9],PCBIn[8],PCBIn[7],PCBIn[3],PCBIn[2],PCBIn[1],PCBIn[14],PCBIn[12],PCBIn[11],PCBIn[5],PCBIn[6],PCBIn[4]]
    return outFix

def main():
    # Keep running or press Enter to quit
    while(1):
        val = input("value: ")
        if (val):
            if (len(val) != 16):
                print("ERR: incorrect number of characters")
            else:
                # Print decoded output with segment designator above
                decoded = decode(val)
                fixed = fixPinOrder(decoded)
                print('ABCDEFGHKMNPRSTU')
                out = ''
                for val in fixed:
                    out += str(val)
                print(out)
        else:
            print("exiting...")
            exit()

if __name__ == "__main__":
    main()
