a = 0.1
b = 0.2
c = a + b
print(c)

# 실행결과가 0.3000000004 이런식으로 나오는데
# 컴퓨터가 부동 소수점을 인지하려면 이진수로 입력해야한다.

from decimal import Decimal

a2 = Decimal("0.1")
b2 = Decimal("0.2")
c2 = a2 + b2
print(c2)