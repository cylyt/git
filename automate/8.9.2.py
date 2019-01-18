text='The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

import re
groups=[]
groups=text.split()
for i in range(len(groups)):
    if groups[i]=='ADJECTIVE':
        new_word=input('enter an ADJECTIVE')
        groups[i]=new_word
    elif groups[i]=='ADJECTIVE.':
        new_word=input('enter an ADJECTIVE')
        groups[i]=new_word+'.'    
    elif groups[i]=='VERB':
        new_word=input('enter an VERB')
        groups[i]=new_word 
    elif groups[i]=='VERB.':
        new_word=input('enter an VERB')
        groups[i]=new_word+'.'
    elif groups[i]=='NOUN':
        new_word=input('enter an NOUN')
        groups[i]=new_word
    elif groups[i]=='NOUN.':
        new_word=input('enter an NOUN')
        groups[i]=new_word+'.'     
newText=' '.join(groups)    
print(newText)
    