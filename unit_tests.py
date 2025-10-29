#Implementing a tester
import array
import F32 as f32
import Twos_Complement

class Tester:
    if __name__ == "__main__":
        # Test the encoding and decoding
        number = 12345
        binary_representation = f32.encodeToBinary(number)
        print("Binary Representation:", binary_representation)

        decoded_number = f32.decodeFromBinary(binary_representation)
        print("Decoded Number:", decoded_number)

        # Verify correctness
        assert number == decoded_number, "The functions do not work correctly!"                