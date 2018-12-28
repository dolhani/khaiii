#/bin/env python3.6
from _kakao import Kakao
kakao = Kakao()

f = open('ab.txt')
lines = f.readlines()
f.close()
line = ''.join(lines)
#print(line)
#print(kakao.nouns('안녕, 세상'))
result = kakao.nouns(line)

for word in result:
    print(word)
