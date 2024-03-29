# [ greedy ]

# [ 로프 ]. 백준 2217번. 브론즈4
# https://www.acmicpc.net/problem/2217

# list(map(int, sys.stdin.readline().split()))

# 변수 1개인 경우: list(map(int, input().split()))
#               = list(map(int, sys.stdin.readline().split()))
#               (단, sys.stdin.readline().split()는 작성하기 전에 먼저 import sys 작성해서 임포트해와야 함)
# 변수 2개인 경우: map(int, input().split()) 또는 list(map(int, input().split()))
#               = map(int, sys.stdin.readline().split()) 또는 list(map(int, sys.stdin.readline().split()))
#               (단, sys.stdin.readline().split()는 작성하기 전에 먼저 import sys 작성해서 임포트해와야 함)

'''    
- 변수 A, 변수 B 이렇게 변수 1개가 아닌 '변수 2개로 할당했을 때'는, 
  map(int, input().split()) 이 결괏값으로 '<map object at 0x0000021741C1A530>'와 같은 문제 없이 작동하는 이유는, 
  반환된 'map' 객체의 값이 자동적으로 언패킹되어 변수 A와 B에 순서대로 할당됨. 각각의 변수에는 정수 값이 저장됨.
'''


N = list(map(int, input().split()))


for _ in range(N):

    # ===================================================================================================================

    # < 정답코드 1 >
    '''
    N = int(input())
    li = []
    for _ in range(N):
        li.append(int(input()))
    li.sort()
    for i in range(N):
        li[i] = li[i]*(N-i)

    print(max(li))
    '''

# ===================================================================================================================

# < 정답코드 2 >

'''


'''


# ===================================================================================================================


'''
문제
N(1 ≤ N ≤ 100,000)개의 로프가 있다. 
이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 
각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.


입력
첫째 줄에 정수 N이 주어진다. 
다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 
이 값은 10,000을 넘지 않는 자연수이다.


출력
첫째 줄에 답을 출력한다.


예제 입력 1 
2
10
15

예제 출력 1 
20
'''


'''
< gpt 해설 답변 >

코드를 더 상세하게 한 줄씩 살펴봅시다.
문제는 N개의 로프를 이용하여 들어올릴 수 있는 물체의 최대 중량을 찾는 것입니다. 
코드를 이해하기 쉽도록 한 줄씩 숫자로 표시하겠습니다.

N = int(input())
li = []
for _ in range(N):
li.append(int(input()))
li.sort()
for i in range(N):
li[i] = li[i]*(N-i)
print(max(li))

(1) 여기서는 로프 개수인 N을 입력받습니다.
(2) 로프들의 정보를 저장할 빈 리스트 li를 생성합니다.
(3-4) N번 반복하여 각 로프가 견딜 수 있는 최대 중량을 입력받아 리스트 li에 추가합니다.
비유: 이 과정은 마치 로프가 사람이고 각 사람은 서로 다른 양의 짐을 들 수 있다고 생각하면 이해하기 쉽습니다. 
여기서 N명의 사람이 각자 들 수 있는 짐의 양을 입력 받습니다.
(5) 여기서는 입력받은 로프에 대한 정보를 견딜 수 있는 중량에 따라 오름차순 정렬합니다.
(6-7) N번 반복하면서 각 로프에서 들 수 있는 물체의 중량을 나눠서 부담시키고, 각 경우에서 들어올릴 수 있는 
최대 중량을 계산하여 리스트 li에 저장합니다. for문 안에서 i는 반복 횟수입니다. 
예를 들어, 첫번째 로프를 사용했을 때 아래와 같은 과정을 거칩니다:
- li[0] = li[0] * (N - 0) 즉, 첫 번째 로프가 들 수 있는 중량(10) 곱하기 로프의 개수 N(이 경우에는 2)을 합니다. 
  그러면 li[0] = 20이 됩니다.
- 다음으로 두 번째 로프를 사용했을 때:
- li[1] = li[1] * (N - 1): 두 번째 로프가 견딜 수 있는 중량(15)에 로프의 개수에서 1을 뺀 값(2-1=1)을 곱합니다. 
  여기서, li[1] = 15가 됩니다. 합니다.
(8) 모든 로프의 경우를 계산한 후, 리스트 li의 최대 값을 출력합니다. 이 값은 각 로프를 사용해서 들어올릴 수 있는 물체의 
최대 중량이 됩니다. 예시를 사용하여 단계별로 이해해봅시다. 

예제 입력:

2
10
15

코드의 실행 결과:
N = 2 (로프의 개수)
리스트 생성: li = []
입력받기 시작
첫 번째 로프 중량 입력: li = [10]
두 번째 로프 중량 입력: li = [10, 15]
정렬하기: li = [10, 15] 6-7. 각 로프에서 들 수 있는 최대 중량 계산
첫 번째 로프: li = [20, 15] - 중량 10 * 로프 개수 2 = 20
두 번째 로프: li = [20, 15] - 중량 15 * (로프 개수 2 - 1) = 15
결과 출력: 20
도움이 되는 표시본 간략한 표는 다음과 같습니다.
로프 번호	중량 입력	정렬 후	견딜 수 있는 최대 중량	최대 중량
1	10	10	20	20
2	15	15	15	
이제 각 줄의 코드가 하는 일, 작동 방식, 그리고 예시를 통해 어떻게 동작하는지에 대한 이해를 돕기 위한 비유 및 명확한 예시를 
기반으로 코드를 설명하였습니다. 이 모든 내용을 토대로 이러한 유형의 문제를 해결하는 데 도움이 될 것입니다.
'''
