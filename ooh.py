import smtplib
import pyinputplus as pyin
from datetime import date




Task1 = "did task? "
Task2 = "brushed teeth thrice, floss and use mouthwash? "
Task3 = "wore flipflops? "
Task4 = "took 1.5hrs off tech? "
Task5 = "locked up? "
Task6 = "meditated? "
Task7 = "neatened up? "

taskAns1 = pyin.inputYesNo(Task1)                     
taskAns2 = pyin.inputYesNo(Task2)                     
taskAns3 = pyin.inputYesNo(Task3)                     
taskAns4 = pyin.inputYesNo(Task4)                     
taskAns5 = pyin.inputYesNo(Task5)                     
taskAns6 = pyin.inputYesNo(Task6)                     
taskAns7 = pyin.inputYesNo(Task7)



emailadd = "demonumberseven@Gmail.com"
passwor = "LB6gSDGeLCYF3D^Ic"
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(emailadd, passwor)

    subject = "my tasks " + str(date.today())
    body =  Task1 + taskAns1+ "\n" + Task2 + taskAns2 +"\n"+ Task3 + taskAns3 +"\n"+ Task4 + taskAns4 + "\n"+Task5 + taskAns5 + "\n"+Task6 + taskAns6 + "\n"+Task7 + taskAns7

    msg = f"subject: {subject} \n\n {body}"

    smtp.sendmail(emailadd, "denise.bdixon@gmail.com", msg)
    smtp.sendmail(emailadd, "leon.dixon@gmail.com", msg)