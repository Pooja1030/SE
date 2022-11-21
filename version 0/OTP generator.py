import random
import smtplib
import sender_data

n=(int(input("Enter your range of otp ")))  # Input for the length of the OTP

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

receiver_name=input("Enter receivers name ") 
receiver_email=input("Enter receivers email ")

# Function to send the Email 
def send_email(): 

    login_into_sendersemail()

    # generate_otp function is called
    otp_var=generate_otp(n)
    msg=("Hello "+ receiver_name +"\n"+ str(otp_var)+" is your OTP. ")
    print(msg)
    server.sendmail(Sender_email,receiver_email,msg)
    server.quit() #to quit the server
    print("The email has been sent!!!")

# send_email function is sent
send_email()