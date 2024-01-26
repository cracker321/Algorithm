# [ 그리디 알고리즘 ]
'''
-

'''


# [ 백준 11047번 ]. p183
# https://www.acmicpc.net/problem/11047
'''
문제
: 준규가 가지고 있는  총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
: 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ 동전은K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

N, K = map(int, input().split())

coins = [] # 현재 가지고 있는 동전의 총 종류 N 가지를 저장하기 위한 리스트 생성, 초기화.

# < 현재 가지고 있는 동전의 총 종류 N가지를 입력받고, 그것을 '리스트 coins'에 저장하기 >
for _ in range(N): # 0 ~ N-1번까지의 인덱스 생성. 아래 실행문을 N번 반복하여, 그 동전의 종류 N가지들을 모두 '리스트 coins'에 저장하는 것임.
    coin = int(input())
    coins.append(coin)
    
    
'''
위에를 저렇게 써도 되고,

for i in range(N):
    coins[i] = int(input())
    
이렇게 써도 되고, 똑같다!
'''


count = 0 # 동전의 가치 합 K를 만들기 위해 필요한 동전 개수의 최솟값을 저장하는 변수 생성, 초기화.


for i in range(N-1, -1, -1): # N-1 ~ 0 까지의 숫자를 -1의 간격으로 거꾸로 출력함. 현재 보유 동전의 총 가짓수는 N가지가 돼야 하기에, N-1부터 시작함. 당연함.
                             # 왜냐하면, 0까지 내려가기 때문이다.
                             # 동전 가치가 큰 순서대로 처리하기 위해 역순으로 반복함.
                             # 저 위에 첫 번째 for문은 일단 그냥 현재 보유 동전 종류들을 '리스트 coins'에 일단 먼저 담기 위함이고,
                             # 여기서의 두 번째 for문은 그 담은 동전들 집합인 '리스트 coins'의 원소들을 '역순으로 재배열'하여 그것을 꺼내 사용하기 위함이다!
    count += K // coins[i] # 예시로, 동전의 가치 합 K=17원, 동전의 종류 개수 N=3, 동전의 종류 리스트 [1, 5, 10] 으로 상정해서 이해하면 됨.
    K %= coins[i] # 


print(count)
    

    
'''
< GPT 해설 답변 >
먼저, 위의 코드는 count 변수를 0으로 초기화하고, for 반복문을 통해 동전 가치를 확인하여 필요한 동전 개수를 계산합니다. 
마지막으로, count를 출력합니다. 아래 예시를 통해 코드가 어떻게 동작하는지 자세히 알아보겠습니다.


입력: N = 3, K = 17, coins = [1, 5, 10]

count = 0: count 변수를 0으로 초기화합니다.

for i in range(N-1, -1, -1):에서 i는 2, 1, 0의 값을 가집니다. 즉, 동전 가치를 10, 5, 1의 순서로 확인하게 됩니다.


1. 첫 번째 반복에서 i = 2인 경우:

count += K // coins[i]를 계산합니다. 현재 K는 17이고, coins[i]는 10입니다. 10원 동전으로 17원을 만들 수 없으므로, 몫은 1입니다. 
count에 1을 더합니다. count는 1이 됩니다.
K %= coins[i]를 계산합니다. K에는 남은 가치인 7이 할당됩니다.


2. 두 번째 반복에서 i = 1인 경우:

count += K // coins[i]를 계산합니다. 현재 K는 7이고, coins[i]는 5입니다. 5원 동전으로 7원을 만들 수 있으므로, 몫은 1입니다. count에 1을 더합니다. 
count는 2가 됩니다.
K %= coins[i]를 계산합니다. K에는 남은 가치인 2가 할당됩니다.


3. 세 번째 반복에서 i = 0인 경우:
count += K // coins[i]를 계산합니다. 현재 K는 2이고, coins[i]는 1입니다. 1원 동전으로 2원을 만들 수 있으므로, 몫은 2입니다. count에 2를 더합니다. 
count는 4가 됩니다.


for 루프가 종료되고, count를 출력합니다. 이 경우 count는 4가 됩니다.

따라서, 동전의 종류가 1원, 5원, 10원이고 K가 17원인 경우에는 17원을 만들기 위해 1원짜리 동전 2개와 10원짜리 동전 1개가 필요합니다.


'''