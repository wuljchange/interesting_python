import re


text = '/* http new s */'
r = re.compile(r'/\*(.*?)\*/')
print(r.findall(text))
