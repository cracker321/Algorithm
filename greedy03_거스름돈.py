# [ greedy ]

# [ 거스름돈 ]. 백준 14916번. 브론즈5
# https://www.acmicpc.net/problem/14916


# ===================================================================================================================



# < 정답코드 1 >

n = int(input()) # 거스름돈 n원 입력받음

num = n%5 #'거스름돈을 5원짜리 동전으로 나눴을 때의 나머지 잔액'을 변수 num에 저장함.
          # 거스름돈 구성 중 5원짜리 동전의 개수를 세는 데 필요함.

if n == 1 or n==3: # 거스름돈이 1원 또는 3원인 경우(딱 이 두 경우에만),
    print("-1") # 거스름돈을 정확히 줄 수 없으므로 -1을 출력함.
elif num%2 == 0: # '거스름돈을 5원으로 나눴을 때의 나머지'가 짝수인 경우
    print(n//5+num//2) 
elif num%2 != 0: # '거스름돈을 5원으로 나눴을 때의 나머지'가 홀수인 경우. e.g) 21원, 23원, 26원, 29원, 31원, 33원, 36원, 39원 ...
    print((n//5)-1  +  (num+5)//2) # -'(n//5)-1': 거스름돈에서 5원 동전 한 개를 줄이고
                                   #              (즉, 현재 거스름돈에서 5원은 뺀 것임. 따라서, 이 경우 이제 2원 동전이 더 많이 필요해짐)
                                   # -'(num+5)//2': 거스름돈에서 5원 동전 한 개를 줄인 만큼을 다시 원상복구(=원래 최초 거스름돈 그대로)해서
                                   #                2원으로 나눈 몫
                                    
    
# ===================================================================================================================


# < 정답코드 2 >

n = int(input())

cnt = 0 # 거스름돈울 구성하는 데 필요한 총 돈전의 개수

while n >= 0: # 거스름돈 n원이 0원 이상일 동안에는 계속 True가 되어 반복함. (1.eg: 만약 n이 12원이라면)
    if n % 5 == 0: # 거스름돈이 5의 배수라면 (2.eg: 이 if문에는 들어가지 못하고) (5.eg: 이제 10원이 됐으니 여기 if문으로 들어오게 되고)
        cnt += n//5 # 5원짜리 동전만으로 거스름돈을 구성할 수 있음. (6.eg: '4.eg'에서 이미 1개 필요해진 동전의 개수 cnt가
                    #                                                   여기로 다시 들어와서, 'cnt = 10//5 + 1' 이렇게 되는 것임.
                    #                                                   이래야 진짜 제대로 된 최종 cnt가 되는 것임.)

        print(cnt) # (7.eg: 이제 그 cnt를 출력함.)
        break # (8.eg: while 반복문을 끝내고 탈출함. 즉, 이제 반복문의 제어흐름에서 벗어남.)
    
    # *****중요***** 
    # 위 if문과 아래 'n -= 2 ...' 실행문은 전혀 별개이다.
    # 위 if문은 while로 반복되는 실행문이 아니고,
    # 아래 'n -= 2 ...' 실행문은 while로 반복되는 실행문이다!
    
    
    # < 거스름돈이 5의 배수가 아닌 경우에의 5로 나눈 나머지 돈을 계산하는 로직 > 
        
    n -= 2 # 거스름돈이 5의 배수가 아닌 경우, 거스름돈에서 2원을 빼고 (3.eg: 12원에서 2원이 빠져서 10원이 되고)
           # (이렇게 함으로써, 현재 거스름돈에서 가장 가까운 5의 배수 거스름돈으로 빠르게 변환될 수 있음)
    cnt += 1 # 필요한 거스름돈 동전의 개수 에 1을 더해줌. (4.eg: 빠진 2원 만큼의 동전 1개가 더 필요하기 때문에 동전 개수 하나 더 추가
              #                                                여기 로직은 10원을 계산하는 곳이 아님. 그냥 그 빠진 2원 동전 1개만 추가해줌.)
              # 즉, 2원짜리 동전을 하나 더 사용하는 것이기 때문에, 동전의 개수를 하나 더 추가해주는 것임.
              # 이렇게 함으로써, 거스름돈 구성에 필요한 5원짜리 동전과 2원짜리 동전을 조합하여, 필요한 최소 동전의 개수를 만들어낼 수 있음.
            
    
else: # 파이썬의 반복문(for문, while문)도 for-else 또는 while-else 사용 가능한데,
      # 만약, for-else, while-else를 사용하고, 
      # 1) 반복문 안에 break가 없는 상태에서 while문이 False상태에 도달하거나 하는 등의 이유로 반복문을 빠져나올 경우, 
      #    --> 바로 else의 실행문이 수행된다!
      # 2) 그 반복문 안에 break가 있는 상태에서 break를 만나 반복문이 완전 끝까지 다 실행되지 않고 break 때문에 중간에 종료된 경우, 
      #    --> for-else, while-else의 'else실행문'은 수행되지 않음!
    print(-1)


# ===================================================================================================================

# < 정답코드 3 >

n = int(input())

cnt = 0
i = 0
while True:
    if n % 5 == 0:   # 5의배수이면 or 2로만 거슬러주고 n이 0이된경우 
        cnt += n//5		#5로나눈 몫이 정답 
        break
    else:
        n -= 2   #5의배수가 아니면 2백원씩 뺴면서 5로 나누어떨어지는것이 나오도록
        cnt += 1
    if n < 0:  # 2원씩 뺏더니 음수가 되버린경우 --> 거슬러줄수 없을을 의미함 
        break
if n<0:			# 음수면 거슬러줄수없 
    print(-1)			
else:
    print(cnt)
    
    
    
# ===================================================================================================================


# < 정답코드 4 >
'''
n = int(input())    # 거스름돈 액수 n
 
tmp = n % 5 # 반복해서 나오는 식을 간단하게 변수로 선언해두기
 
if n == 1 or n == 3:    # 거스름돈이 1이나 3이면 거슬러줄 수 없으므로 -1 출력
    print(-1)
 
elif tmp % 2 == 0:  # n이 5로 나누었을 때의 나머지가 짝수이면(2로 나눌 수 있으면)
    print((n // 5) + (tmp // 2))  # 5로 나눴을 때의 몫 + 그 나머지를 2로 나눴을 때의 몫.
 
else:   # n이 5로 나누었을 때의 나머지가 홀수이면(2로 나눌 수 없음)
    print((n // 5) - 1 + (tmp + 5) // 2)  # 5로 나눴을 때의 몫에서 1을 빼준 값 + 그 나머지에 5를 더해준 후 2로 나눴을 때의 몫.
'''

# ===================================================================================================================


'''
문제
춘향이는 편의점 카운터에서 일한다.
손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다.
동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.
예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 
거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.


입력
첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.


출력
거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.


예제 입력 1 
13
예제 출력 1 

5
예제 입력 2 
14
예제 출력 2 
4
'''

