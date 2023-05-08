import os

with open(r'c:\Users\311004\Desktop\1.txt', 'r', encoding='utf8') as f:
    original = f.read()


for line in original.splitlines():
    print(line.split(' '))