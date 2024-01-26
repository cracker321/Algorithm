# [ Time Complexity 시간 복잡도 ]
'''
- 데이터의 크기가 가장 클 때를 가정하는(=시간복잡도가 최악일 때를 가정하는) '빅오 표기법'을 사용한다!
- 시간 복잡도는, '가장 많이 중첩된 반복문을 기준으로 도출'하기 때문에, 'n번 중첩된 반복문(for문, while문 등)'을 어떻게 개선할 수 있는지 여부가
  가장 핵심이다!
  이 부분을 연산에 효율적인 구조로 수정하는 작업이
- 동일한 for문 을 N번 사용하는 것인, 이중 for문(=N의 제곱) 사용하는 것보다 훨~~씬 시간 복잡도가 낮고 효율적이다.
  동일한 for문을 N번 사용하는 것은 연산에서 사실 for문을 1번 사용하는 것과 시간복잡도에서 별 차이가 없기 때문이다!

'''


#=====================================================================================


# < 예제 1 >. 교재 p17

# import random
# findNumber = random.randrange(1, 101) # 1~100 사이의 랜덤값 생성

# for i in range(1, 101):
#     if i == findNumber:
#         print(i)
#         break
    
    
#=====================================================================================


# [ 백준 2750번: 수 정렬하기 ]
''' (전체 블록 주석처리 방법 1: 이렇게 '블록 따옴표 주석처리는 shift + alt + a' 이고, '블록 샵 # 주석처리는 ctrl + /' 임)
문제
: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
  이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# 1.< 입력될 수의 개수 N개 코드 >
N = int(input()) 



# 2.< N개의 숫자들을 생성하여 저장할 빈 리스트 생성(초기화) >
numbers = [] 



# 3.< N개의 숫자들을 입력받고, 그 숫자들 '리스트 numbers'에 저장하기 >
for _ in range(N): # 아래 실행문을 N번 반복하여, 그 N개의 숫자들을 모두 '리스트 numbers'에 저장하는 것임.
  num = int(input()) # N개의 숫자들을 입력하도록 함.
  numbers.append(num) # 그리고 그 입력된 숫자들을 '리스트 numbers'에 저장하기

  
  
# 4.< 그 숫자들을 오름차순으로 정렬하기 >
numbers.sort()



# 5.< 위에서 정렬된 결과를 출력하기 >
for num in numbers:
  print(num) # 출력값: 한 줄에 한 개의 숫자씩, 총 5줄에 총 5개의 숫자가 오름차순으로 출력됨.
# cf) 'print(numbers)' 입력하게 되면, 이것은 한 줄로 늘어진 '리스트 numbers'를 출력하는 것이다.
#     즉, 이렇게 하면 출력값이 '[숫자, 숫자, 숫자, 숫자, 숫자]'의 형식으로 나온다.
  
  
  
  