import random
import sender_data
import smtplib


def generateOTP(size):
    OTP = ""
    for i in range(size):
        OTP += str(random.randint(0, 9))
    return OTP


def verifyOTP(otp, otp_1):
    if otp_1 == otp:
        return True
    else:
        return False

def sendOTP(Sender_data, receiver_email, OTP):
    # Connect to server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #Get sender's details
    sender_email=Sender_data.email
    sender_password=Sender_data.password


    # Login to gmail account of sender
    server.login(sender_email, sender_password)

    # Generate message to be sent
    msg = str(OTP)+" is your OTP"

    # Send email
    server.sendmail(Sender_data.email, receiver_email, msg)

    # Disconnect server
    server.quit()


if __name__ == '__main__':
    # Get receiver's email
    receiver_email = 'poojasawant@dbatu.ac.in'  # input("Enter your email: ")

    # Generate OPT
    size = int(input("Enter length of OTP: "))
    OTP = generateOTP(size)

    # Send OTP
    sendOTP(sender_data, receiver_email, OTP)
    print("OTP sent!")

    # Verify OTP
    otp_1 = input("Enter your OTP >> ")

    if verifyOTP(OTP, otp_1):
        print("Verified!")
    else:
        print("Incorrect OTP!")
