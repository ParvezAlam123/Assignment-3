# for generating bernoulli sample I have used binomial  where  n=1
import numpy as np
s=np.random.binomial(1,3/4,10000)
c=0
for i in range(10000):
    if s[i]==1:
        c=c+1
X3=c/10000
c=0
s=np.random.binomial(1,1/4,10000)
for i in range(10000):
    if s[i]==1:
        c=c+1
X1X2=c/10000
X1X2_given_X3=X1X2/X3
print("simulated probability:",X1X2_given_X3)