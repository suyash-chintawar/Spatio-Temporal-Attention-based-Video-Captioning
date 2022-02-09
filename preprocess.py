from operator import index
import pandas as pd

ifile = open('data.txt','r')
ofile = open('clean_data.txt','w')

for line in ifile:
    line = line.split()
    temp= line[0]+','+line[1]
    line = line[2:]
    line = [temp] + line
    ofile.write(' '.join(line)+'\n')

df = pd.read_csv('clean_data.txt',delimiter=',')
df.to_csv('data.csv',index=None)