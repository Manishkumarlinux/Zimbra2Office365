import os

ZIMBRA_HOST = 'mail.example.com'
ZIMBRA_PORT = '143'
PASS = 'zimbra@123'
PASS_OFC = 'manish@123'
OFC365_HOST = 'pod51010.outlook.com'
OFC365_PORT = '993'
EmailID = ['test@example.com', 'test2@example.com', 'test3@example.com']


for EID in EmailID:
        imapcmd = "imapsync --host1 " + ZIMBRA_HOST + " --user1" + ' ' + EID + " --password1" + ' ' + PASS + " --port1" + ' ' + ZIMBRA_PORT + " --host2" + ' ' + OFC365_HOST + " --user2" + ' ' + EID + " --password2" + ' ' + PASS_OFC + " --ssl2" + " --port2" + ' ' + OFC365_PORT + " --noauthmd5"
        os.system(imapcmd)
