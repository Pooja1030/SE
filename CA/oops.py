#Implementation OTP assignment as per OOP design described in classroom
import random
#here we have used random module to generate random otp
import smtplib
#to send e-mail to reciever
import re
#to check if email is in valid format or not here used regular expression library


class oopsotp:
    def __init__(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            #connecting to SMTP server at port 587
            self.server.ehlo()
            self.server.starttls()
            #to start the server process
            self.sender_email = 'poojasawant1030@gmail.com'
            self.sender_pass = 'gwag viyw swrm fhpo'
            self.server.login(self.sender_email, self.sender_pass)
        except:
            print("Unable to connect to the SMTP server")
            exit()

        self.otp = None
        for i in range(3):  # Stop the program if user enters a invalid email several times
            self.eMail = input(" Please enter your Email id: ")
            if self.matching_email(self.eMail):
                break
            else:
                print(" Your email id is invalid !!")
        else:
            print("You've entered an invalid email too many times!!! \n Try again later...")
            exit()


    def matching_email(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        #setting email template: *@*.*
        if re.fullmatch(regex,email): #checking if the entered email matches the template
            return True
        else:
            return False

    # function to return a OTP of length n
    def return_otp(self, n):
        otp=""
        for i in range(n):
            otp+=str(random.randint(0,9))
        return(otp)

    # Function to verify if entered OTP is correct
    def verify_otp(self):
        print("Verify your email id: ")
        OTP = input("Enter the OTP: ")
        if OTP==self.otp:
            print("Email ID successfully verified...")
        else:
            print("Invalid OTP")

    # function to send email
    def send_email(self,n):
        self.server.sendmail(self.sender_email, self.eMail, "Subject:OTP\nYour OTP using OOP is " + self.otp)  # Sending the email
        print("An {} digit OTP has been sent to {}".format(n, self.eMail))



if __name__=='__main__':
    obj=oopsotp()
    n=int(input("Enter the OTP length: "))
    obj.otp=obj.return_otp(4)
    obj.send_email(4)
    obj.verify_otp()
    obj.server.close()