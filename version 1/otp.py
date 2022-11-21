import random
import smtplib
import sender_data


#function to generate otp 
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))      # OTP will append any random digits[index] 
    return (OTP)


# Creating Gmail's server

server =smtplib.SMTP('smtp.gmail.com',587)

# Importing the sender's email from other file
Sender_email = sender_data.email
Sender_password= sender_data.password

# Function to login and add this to the server
def login_into_sendersemail():
    server.starttls()              # Transfered layer Security
    server.login(Sender_email,password=Sender_password)         # Login in the senders mail



# Function to send the Email 
def send_email(): 
    receiver_name=input("Enter receiver's name: ") 
    receiver_email=input("Enter receiver's email: ")
    login_into_sendersemail()
    n=(int(input("Enter your range of otp: ")))  # Input for the length of the OTP

    # generate_otp function is called
    otp_var=generate_otp(n)
    msg=("Hello "+ receiver_name +","+"\n"+ str(otp_var)+" is your OTP. ")
    print(msg)
    server.sendmail(Sender_email,receiver_email,msg)
    server.quit() #to quit the server
    print("The email has been successfully sent!!!")

# send_email function is sent
# send_email()