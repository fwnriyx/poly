#Please ensure that you are using python 3.10 such that you can use the match case statement

from misc import boxbox
from misc import menu

menu()

# while case != 8:
#     input("Press enter key, to continue....\n")
#     choice = input(f"""Please select your choice: (1,2,3,4,5,6,7,8)
#     \t1. Encrypt/Decrypt Message
#     \t2. Encrypt/Decrypt File
#     \t3. Analysze letter frequency distribution
#     \t4. Infer caesar cipher key from file
#     \t5. Analyze, and sort encrypted files
#     \t6. Extra Option One
#     \t7. Extra Option Two
#     \t8. Exit
# Enter choice: """)

#     match int(choice):
#         case 1:
#             eord = input(f'Enter "E" for encryption, "D" for decryption: ')
#             if eord == "E":
#                 codedText = input(f"Please type text that you want to encrypt: \n")
#                 shift = int(input(f"Enter the cipher key: \n"))
#                 print(f"Plaintext: {codedText}\n Encrypted text: {textEncDec(codedText, shift)}")
            
#             elif eord == "D":
#                 print(f'Please type text that you want to decrypt: \n')
#                 codedText = input(f"Please type text that you want to decrypt: \n")
#                 shift = int(input(f"Enter the cipher key: \n"))
#                 print(f"Encrypted text:\t {codedText}\nPlaintext:\t {textEncDec(codedText, shift)}")
#             else:
#                 print(f'Invalid input')
#         case 2:
#             eord = input(f'Enter "E" for encryption, "D" for decryption: ')
#             chosenFile = input(f"Please enter the file you want to encrypt: ")
#             shift = int(input(f"Enter the cipher key: \n"))
#         case 8:
#             print(f'\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer')
#             exit();
