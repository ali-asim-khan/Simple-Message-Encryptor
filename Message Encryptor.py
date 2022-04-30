import random
print("\n<<< Message Encryption >>>")
option = int(input("1: Encrypt, 2: Decrypt: "))
message = input("Type message here: ")
if option == 1:
    message = message.replace("e", "1")
    message = message.replace("a", "2")
    message = message.replace("i", "3")
    message = message.replace("o", "4")
    message = message.replace("u", "5")
    reversed = ''.join(reversed(message))
    reversed = reversed.upper()
    print("Encrypted message: " + reversed)
elif option == 2:
    message = message.replace("1", "e")
    message = message.replace("2", "a")
    message = message.replace("3", "i")
    message = message.replace("4", "o")
    message = message.replace("5", "u")
    reversed = ''.join(reversed(message))
    reversed = reversed.lower()
    print("Decrypted message: " + reversed)
else:
    print("Invalid option")