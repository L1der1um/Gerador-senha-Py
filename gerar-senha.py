import random

lower = "abcdefehijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPORSTUVWXYZ"
numbers = "0123456789"
symbols ="*;/.-"
all = lower + upper + numbers +symbols
length = 16
password = "".join(random.sample(all,length))

print (password)