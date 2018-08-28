from Utilities import EmailHelper
from Utilities import EmailInfo

class RuleHelper(object):
    def __init__(self,title,msg):
        self.rulName = 'testRule'
        self.emailTitle = title
        self.emailMsg = msg
        self.email = EmailHelper.EmailHelper()
        self.email.SetToEmail(EmailInfo.EMAIL['To'])
        self.email.SetAccountUser(EmailInfo.EMAIL['User'])
        self.email.SetAccountPassword(EmailInfo.EMAIL['Password'])
        self.email.SetFromEmail(EmailInfo.EMAIL['From'])
        self.email.SetSubject(title)
        self.email.SetContent(msg)


