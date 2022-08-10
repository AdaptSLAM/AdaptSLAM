with open("trans_errorGT.txt") as f:
    word=f.read()

uncertainty=word.split(" ")
un=[]
for words in uncertainty:
   words=words.replace('[',"")
   words=words.replace(']',"")
   if words!="":
       un.append(float(words))

import matplotlib.pyplot as plt
plt.plot(un)
plt.show()
