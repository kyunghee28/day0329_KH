import json
str = '{"name":"홍길동","age":"32"}'
print(str)
print(type(str)) #json형태를 띄지만 string

# str은 글자인데 json.loads이라는 객체가
# 딕셔너리로 만들어줌.
r = json.loads(str)
print(r)
print(type(r))
