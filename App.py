import stego
import  stego_decrypt


message=input(f"Please enter secret message you what to hide : ")

stego.generate_key()  # Run once to create key
stego.hide_message("myimg.jpg", message, "encoded.png")

user_input=input("Do you want to decrypt the message  Y or N : ")

if user_input =="Y":
    stego_decrypt.extract_message("encoded.png")

elif user_input =="N":
    print("Exiting  the program ")

else:
    print("Please enter valid input : Y or N ")


