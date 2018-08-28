#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RuleEngine.RuleHelper import RuleHelper

class RuleHelperJulia(RuleHelper):

    def __init__(self,title,msg):
        super(RuleHelperJulia, self).__init__(title,msg)
        self.emailMsg = '<html>Hi All,<p>Please check the file for API test report.</p>Thanks<br/>Julia</html>'
        self.email.SetContent(self.emailMsg)
        self.htmlfilename = "API_Test_Report.html"
        self.tabletmpfile = "API_Test_Report.log"
        self.f = open(self.htmlfilename, 'w')
        self.f.truncate()
        self.t = open(self.tabletmpfile, 'w')
        self.t.truncate()

    def ClearEmailTable(self):
        f = open(self.htmlfilename, 'wb')
        f.truncate()
        f.close()

    def ClearTableValue(self):
        f = open(self.tabltmpfile, 'wb')
        f.truncate()
        f.close()

    def EmailMsgTable(self):
        self.tableStart = '<html><head></head><body><table  border="1px" cellspacing="0px" cellpadding="10px" width="800px" height="40px"  ><tbody>' \
                     '<tr align="left"><th>API Name</th><th>API URL</th><th>STATUS</th><th>RESPONSE</th></tr>'
        self.tableEnd = '</tbody></table></body></html>'
        self.f.write(self.tableStart)

    def EmailMsgTableTitle(self,*args):
        self.tableTitle = '<tr> '
        for row in args:
            self.tableTitle += '<th>' + row + '</th>'
        self.tableTitle += '</tr>'

    def EmailMsgTableValue(self,*args):
        print("---- set Table Value start ----")
        self.tableValue = '<tr>'
        for status in args:
            if status==500:
                self.tableValue += '<td><font color="red">' + 'FAILED' + '</font></td>'
            else:
                self.tableValue += '<td><font color="green">' + 'PASS'+ '</font></td>'
        self.tableValue += '</tr>'
        print("---- set Table Value end ----")

    def SaveMsgTableValue(self): # save table value
        fvalue = open(self.tabletmpfile, 'ab')
        if len(self.tableValue) > 0:
            print("---- save Table Value start ----")
            print(self.tableValue)
            fvalue.write(self.tableValue.encode('utf-8'))
            print("---- save Table Value end ----")
        fvalue.close()

    def SaveMsgTablesAll(self): # save all table value
        fall = open(self.htmlfilename, 'ab')
        fvalue = open(self.tabletmpfile, 'rb')
        tmp = fvalue.readlines()
        #print(tmp)
        #print(len(tmp))
        #print(type(tmp))
        if len(tmp)>0:
            if len(tmp[0])>0 :
                print("---- Start to Save Msg Tables All ----")
                fall.write(self.tableStart.encode('utf-8')+ tmp[0]+ self.tableEnd.encode('utf-8'))
        fvalue.close()
        fall.close()

    def sendEmailWithHtml(self): # send email
        html_file = open(self.htmlfilename, 'rb')
        tmp = html_file.readline()
        if len(tmp)>0:
           self.email.attachment = self.htmlfilename
           self.email.SendEmail()
        else:
           print("Attachment HTML file is empty, no need to send email")


if __name__ == "__main__":
   a = RuleHelperJulia("lallla","jjlsd")
   #a.ClearEmailTable()
   #a.ClearTableValue()
   a.EmailMsgTable()
   a.EmailMsgTableTitle('a','b','c')
   a.EmailMsgTableValue(500,200,200)
   a.SaveMsgTableValue()
   a.SaveMsgTablesAll()
   a.sendEmailWithHtml()
