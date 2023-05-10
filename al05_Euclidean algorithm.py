# [ 최대공약수 계산(유클리드 호제법) 예제 ]

'''
두 개의 자연수에 대한 최대공약수를 구하는 알고리즘.
- 두 자연수 A, B 에 대하여(A > B) A를 B로 나눈 나머지를 R이라고 합시다.
  이 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같음.
- 유클리드 호제법의 아이디어를 그대로 재귀함수로 작성할 수 있음. 
- 최대공약수: GCD(=Greatest Common Divisor)
- 최소공배수: LCM(=Least(Lowest) Common Multiple)
'''

# < GCD(192, 162)의 경우 >
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
print(gcd(192, 162)) # 호출할 때는 인자값을 매개변수의 순서 a, b(a>b) 이렇게 a가 b보다 꼭 크게 넣지 않아도 됨
                     # 즉, 'gcd(192, 162)'로 하든지 'gcd(162, 192)' 하든지 동일하다!