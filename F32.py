#Implementing bit-level encode
import array

class F32:
    def encodeToBinary(num):
        to_proc = num
        #limit 0-65535
        if(to_proc < 0 or to_proc > 65535):
            raise ValueError("Can only accept values between 0 and 65535")

        output_bits = array.array('h',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) #how to make emtpy 16-bit array most efficiently (if it gives you problems, replace 'h' with 'i')
        for i in range (0, 16):
            current_power = 15 - i
            if(to_proc % (2**current_power) != 0):
                output_bits[i] = 1
        return output_bits
                
    def decodeFromBinary(bits):
        if(len(bits) != 16):
            raise ValueError("Input must be an array of length 16")
        
        output = 0
        for i in range (0,len(bits)):
            output += bits[15-i] * (2**i)

        return output


    def addBinary(ax, bx):
        pass
