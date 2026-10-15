import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('sender_email')
SENDER_PASSKEY = os.getenv('passkey')

def sendEmail(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(host= SMTP_SERVER, port=SMTP_PORT)
        server.starttls() # server start
        server.login(user=SENDER_EMAIL, password=SENDER_PASSKEY)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string()) # send mail
        server.quit() # close server
        return True, "Email send to Registered Mail"
    except Exception as e:
        return False, f"Something wrong in utils.py-sendEmail():{e}"

#generate hash password
def generateHashPassword(password:str):
    hash_password=bcrypt.hashpw(
        password=password.encode('utf-8'),
        salt=bcrypt.gensalt(4)
    )
    return hash_password


#validate hahs password
def validateHashPassword(password:str,hash_password:str):
    status=bcrypt.checkpw(password=password.encode('utf-8'),
                          hashed_password=hash_password.encode('utf-8'))
    return status









class EmailTemplates:
    @staticmethod 
    def registerEmailTemplate(otp:int, username:str="Dear"):
        template = f"""Hello {username},
        Thanks for chosing SNS app to manage your files and Notes
        
        Your OTP: {otp}
            
        If your not registering to this app, simple ignore this email and 
        don't share OTP with any one.
        
        Thank you
        
        Best whises,
        SNS Managment"""
        return template
    @staticmethod
    def forgotPasswordTemplate(url:str,username:str="Dear"):
        template=f"""Hello {username},
        To manage your files and notes, first reset password and login
        with new password.

        Your reset password link : {url}
        If it is not done by you simple ignore this file
          
        Thanks for choosing SNS app.
          
        Reegards 
        SNS Management  """
        return template
