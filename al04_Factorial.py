# [ 팩토리얼 구현 ]
'''
수학적으로 0!과 1!의 값은 1임.

result *= i 는 result = result * i
result -= i 는 result = result - i
result /= i 는 result = result / i

'''


# < 반복적으로 구현한 n팩토리얼(= n!) >
def factorial_iterative(n):
    result = 1
    
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i # result = result * i 
    return result # result가 누적된 값들을 다 합하는 것이 아니고, 최종단계의 result 값만 반환하는 것이다. 당연!


# < 재귀적으로 구현한 n팩토리얼(= n!) >
def factorial_recursive(n):
    if n<=1: # n이 1이하인 경우, 1을 반환
        return 1
    # n! = n * (n-1)! 을 그대로 코드로 작성한 것
    return n * factorial_recursive(n-1)   
    
    
print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))