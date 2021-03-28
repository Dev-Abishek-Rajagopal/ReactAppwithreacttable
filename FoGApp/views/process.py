'''
Created on 27-MAR-2021

@author: Abishek Rajagopal
'''


from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view
from FoGApp.models import (Green_Business,Green_Owner)
from FoGApp.serializers.serializers import (UserSerializer,Green_OwnerSerializer,Green_OwnerSerializerI,
Green_OwnerSerializerII, Green_OwnerSerializerIII, Green_OwnerSerializerforPUT, Green_BusinessSerializer,
Green_BusinessSerializerI, Green_BusinessSerializerforPut)
from django.contrib.auth.models import User
from rest_framework.response import Response
import smtplib
import logging
from django.conf import settings
from django.core.mail import send_mail
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger("fog.request")


def smtpsender(data, id):
    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = data["email"]
    smtptype = 'html'
    smtpsubject = "Verification Mail From Friends of Green"

    first = data["first_name"]
    last = data["last_name"]
    username = data["username"]
    country = data["country"]
    contact = data["contact"]

    mail_content = "http://127.0.0.1:8000/store/activate_user/?pk=" + str(id) + ""
    url = '<a href="' + mail_content + '">Activate</a>'
    try:
        if smtptype == "text":
            logger.info("Sending Text Email")

        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Friend of Greenner,<br>
     <p>          Please check the following Details and click the link below to activate your Bookstagram Account</p>  
     <h2><b>Friend of Green Owner Information:</b></h2>         
<table>
  <tr>  
    <td>
    <i><b>First Name</b></i>
    </td>
    <td>
    <i>""" + first + """</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Last Name</b></i>
    </td>
    <td>
    <i>""" + last + """</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>User Name</b></i>
    </td>
    <td>
    <i>""" + username + """</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Country</b></i>
    </td>
    <td>
    <i>""" + country + """</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>contact</b></i>
    </td>
    <td>
    <i>""" + contact + """</i>
    </td>
  </tr>

  </table>
  <br><br>
    <h3><b>Activate Friend of Green:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>Activation Link</b></i>
    </td>
    <td>
    <i>""" + url + """</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 

  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Friend of Green.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,
                    emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)


def smtpsenderBiz(data, id):
    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = data["email"]
    smtptype = 'html'
    smtpsubject = "Verification Mail From Friends of Green Business"

    first = data["name"]
    country = data["country"]
    contact = data["contact"]

    mail_content = "http://127.0.0.1:8000/store/activate_user/?pk=" + str(id) + ""
    url = '<a href="' + mail_content + '">Activate</a>'
    try:
        if smtptype == "text":
            logger.info("Sending Text Email")

        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Friend of Greenner,<br>
     <p>          Please check the following Details and click the link below to activate your Bookstagram Account</p>  
     <h2><b>Friend of Green Business Information:</b></h2>         
<table>
  <tr>  
    <td>
    <i><b>Name</b></i>
    </td>
    <td>
    <i>""" + first + """</i>
    </td>
  </tr>

  <tr>  
    <td>
    <i><b>Country</b></i>
    </td>
    <td>
    <i>""" + country + """</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>contact</b></i>
    </td>
    <td>
    <i>""" + contact + """</i>
    </td>
  </tr>

  </table>
  <br><br>
    <h3><b>Activate Friend of Green Business:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>Activation Link</b></i>
    </td>
    <td>
    <i>""" + url + """</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 

  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Friend of Green.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,
                    emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)



class SMTPCON(object):

    def __init__(self, smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, emailtype, subject, content):
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.smtpuser = smtpuser
        self.smtppasswd = smtppasswd
        self.smtpfromaddr = smtpfromaddr
        self.smtptoaddr = smtptoaddr
        self.emailtype = emailtype
        self.subject = subject
        self.content = content
        print(self.smtphost)

    def SendHtmlEmail(self):
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr

        # Attaching the Content of email

        body = MIMEText(self.content, 'html')

        # Attaching the body of email

        msg.attach(body)
        logger.info(msg.attach(body))

        # Connection to SMTP Server
        logger.info("in py")
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        logger.info(con.starttls())
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
        else:
            con.login(self.smtpuser, self.smtppasswd)
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
        con.close()

        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [msg['To'], ]
        # send_mail(msg['Subject'], msg.as_string(), email_from, recipient_list)

