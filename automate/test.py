#Finds phone numbers and email addresses on the clipboard.


import pyperclip,re

    
#email正则

emaiRegex=re.compile(r'(.*\.[a-z]{2-4})


#正则匹配
text='info@nostarch.com'
matches=[]
for groups in emaiRegex.findall(text):
    matches.append(groups[0])

#复制到剪贴板

if len(matches)>0:
    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email found')