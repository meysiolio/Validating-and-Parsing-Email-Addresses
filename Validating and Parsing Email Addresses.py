import email.utils
import re

result = []
for _ in range(int(input())):
    address = email.utils.parseaddr(input())
    try:
        username , domain = address[1].split('@')
    except ValueError:
        continue
    try:
        domain_name, extention = domain.split('.')
    except ValueError:
        continue
    #print(username,domain, domain_name,extention)
    if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9-._]+',username) and re.fullmatch(r'[a-zA-Z]+',domain_name) and re.fullmatch(r'[a-zA-Z]{1,3}',extention):
        result.append(email.utils.formataddr(address))

for i in result:
    print(i)
