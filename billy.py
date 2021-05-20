# Hi Alexis!
#Hi Stephen.
#If you run all, you'll get an error at line 22, but if you just copy
#and paste the remaining code I swear it works. You do have to pass
#the printed first word through the function yourself to get the sentence.

with open('billyjoel.txt') as f:
    billy = f.read()
billy=billy.split()
b=[w.lower() for w in billy]

def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string

b = [remove_punc(i) for i in b]

x=0
b_dict={}
for word in b:
    b_dict.setdefault(b[x],[]).append(b[x+1])
    x+=1

freqs={w:len(b_dict[w]) for w in b_dict}
import numpy as np
print(np.random.choice(list(freqs.keys()),p=np.array(list(freqs.values()))/np.array(list(freqs.values())).sum(),size=1))

def billy_sentence(word):
    billy_sent=[]
    billy_sent.append(word)
    current=word
    for i in range(15):
        current=np.random.choice(b_dict[current])
        billy_sent.append(current)
    print(" ".join(billy_sent))
