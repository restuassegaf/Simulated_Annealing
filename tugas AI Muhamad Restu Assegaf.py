import math
import random

T =100
c=0.99999

x1=random.uniform(-10,10)
x2=random.uniform(-10,10)

solusiAwal =-1*(math.fabs(math.sin(x1)*math.cos(x2)*math.exp(math.fabs(1-(math.sqrt(pow(x1,2) + pow(x2,2))/ math.pi)))))

while (T>0.0001) :
        y1=random.uniform(-10,10)
        y2=random.uniform(-10,10)
        solusiBaru=-1*(math.fabs(math.sin(y1)*math.cos(y2)*math.exp(math.fabs(1-(math.sqrt(pow(y1,2)+pow(y2,2))/math.pi)))))
        if(solusiBaru<solusiAwal):
                solusiAwal = solusiBaru
        else:
                selisih = solusiBaru - solusiAwal
                tampung =math.exp((-1*selisih)/T)
                r=random.random()
                if (r< tampung):
                        solusiAwal = solusiBaru
        T=T*c
print(solusiAwal)
