import random
a=chr(random.randint(97,122))
b=chr(random.randint(97,122))
c=chr(random.randint(65,90))
d=chr(random.randint(65,90))
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))
char1=chr(random.randint(33,47))
char2=chr(random.randint(33,47))
string = a+b+c+d+num1+num2+char1+char2
char_list=list(string)
random.shuffle(char_list)
password=''.join(char_list)
print(password)