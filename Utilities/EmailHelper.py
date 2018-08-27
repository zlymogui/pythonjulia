import sys
import os
import os.path

class EmailHelper:
    def __init__(self):
        self.cmd = "sendEmail.exe"
        self.toEmail = "821064526@qq.com"
        self.subject = "API Test Report"
        self.content = "Please check below for API test report"
        self.accountUser = ""
        self.accountPassword = ""
        self.fromEmail = "821064526@qq.com"
        self.smtp = "smtp.qq.com"
        self.attachment = "dummy.txt"

    def SetToEmail(self,emailList):
        self.toEmail = emailList

    def SetSubject(self,emailSub):
        self.subject = emailSub

    def SetContent(self,emailContent):
        self.content = emailContent

    def SetAttachment(self,attached):
        self.attachment = attached

    def SetAccountUser(self,emailAccountUser):
        self.accountUser = emailAccountUser

    def SetAccountPassword(self,emailAccountPwd):
        self.accountPassword = emailAccountPwd

    def SetFromEmail(self,emailFrom):
        self.fromEmail = emailFrom

    def SetSmtp(self,smtpUrl):
        self.smtp = smtpUrl

    def SendEmail(self):
        emailParam = self.cmd + """ -f %s -t %s -xu %s -xp %s -u "%s" -m "%s" -s %s""" % (self.fromEmail,self.toEmail,self.accountUser,self.accountPassword,self.subject,self.content,self.smtp)
        if os.path.exists(self.attachment):
            emailParam = emailParam + " -a " + self.attachment
            
        print(emailParam)
        os.system(emailParam)
