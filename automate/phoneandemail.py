#Finds phone numbers and email addresses on the clipboard.


import pyperclip,re

#phone 正则
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #area code
    (\s|-|\.)?           #seperater
    (\d{3})              #first 3 digits
    (\s|-|\.)            #seperater
    (\d{4})              #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
    )''',re.VERBOSE)
    
#email正则

emaiRegex=re.compile(r'''(
    (/w)+
    #[a-zA-Z0-9._%+-]*      #username
    @
    #[a-zA-Z0-9.-]+         #domain
    #\.
    #([a-zA-Z]{2-4})
    )''',re.VERBOSE)


#正则匹配
text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)
for groups in emaiRegex.findall(text):
    matches.append(groups[0])
    print('1')

#复制到剪贴板

if len(matches)>0:
    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email found')
