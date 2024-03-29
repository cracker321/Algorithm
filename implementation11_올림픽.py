# [ implementation ]

# [ 올림픽 ]. 백준 8979번. 실버5
# https://www.acmicpc.net/problem/8979

# 'sys.stdin.readline()'는 정확히 'input()'과 동일한 위치에 들어가야 한다!
N, K = map(int, input().strip().split())

board = []

for case in range(N):
    
    num, g, s, b = map(int, input().strip().split())
    board.append([g, s, b])
    
    if num == K: # 입력된 K번 국가가 대상이 될때, 
        chk = [g, s, b] # 그 국가의 금 은 동을 별개의 리스트 chk에 담고
        
board.sort(key = lambda x : (-x[0], -x[1], -x[2]))  # 우선순위 기준을 여러 개 사용(= x를 여러 개 사용)할 때는, 반드시 괄호로 묶어줘야 한다!


print(board.index(chk)+1)


# ===================================================================================================================


# < 정답코드 1 >

'''
import sys

T, N = map(int, sys.stdin.readline().split())

board = [] # 각 국의 메달 정보를 각각에 저장할 각각의 빈 리스트 board를 생성 
for case in range(T):
    num, g, s, b = map(int,sys.stdin.readline().split())
    board.append([g,s,b]) # 각 국가의 메달 정보(금, 은, 동)를 '리스트 board'에 추가함
    if num == N: # '입력받은 국가 번호(=num)'가 문제에서 구하고자 하는 국가 N인 경우,  
        chk = [g,s,b] # 해당 국가의 메달 정보(금, 은, 동)를 변수 chk에 저장함.

board.sort(key = lambda x : (-x[0],-x[1],-x[2])) # 테스트케이스의 개수(=총 국가의 수)에 해당하는 각각의 메달정보(금은동)를 
                                                 # 금-은-동 순서로 내림차순 정렬함.
                                                 # cf) 람다함수에서 적용되는 것은 '리스트 names'가 아닌 '각각 개별의 원소 x'이기 때문에, 
                                                 # 'names[0], names[-1] ..' 이런 것들이 아니라,
                                                 # 'x[0], x[-1] ...' 이 되는 것이다!

print(board.index(chk) + 1) # 정렬된 '리스트 board'에서, index() 함수를 사용하여, 문제에서 구하고자 하는 국가의 메달 정보(chk)의 인덱스를 구한다.
                            # 인덱스는 0부터 시작하기 때문에, 구한 인덱스번호에 1을 더해 등수를 출력한다.

'''


# ===================================================================================================================

'''
문제
올림픽은 참가에 의의가 있기에 공식적으로는 국가간 순위를 정하지 않는다. 
그러나, 많은 사람들이 자신의 국가가 얼마나 잘 하는지에 관심이 많기 때문에 비공식적으로는 국가간 순위를 정하고 있다. 
두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면, 보통 다음 규칙을 따라 어느 나라가 더 잘했는지 결정한다.

금메달 수가 더 많은 나라 
금메달 수가 같으면, 은메달 수가 더 많은 나라
금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 
각 국가는 1부터 N 사이의 정수로 표현된다. 
한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다. 
만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다. 
예를 들어, 1번 국가가 금메달 1개, 은메달 1개를 얻었고, 2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 4번 국가는 메달을 얻지 못하였다면, 
1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 4번 국가가 4등이 된다. 이 경우 3등은 없다. 

각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오. 



입력
입력의 첫 줄은 국가의 수 N(1 ≤ N ≤ 1,000)과 등수를 알고 싶은 국가 K(1 ≤ K ≤ N)가 빈칸을 사이에 두고 주어진다. 
각 국가는 1부터 N 사이의 정수로 표현된다. 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어진다. 전체 메달 수의 총합은 1,000,000 이하이다.



출력
출력은 단 한 줄이며, 입력받은 국가 K의 등수를 하나의 정수로 출력한다. 등수는 반드시 문제에서 정의된 방식을 따라야 한다. 



서브태스크
번호	배점	제한
1	8	


예제 입력, 출력

2	12	
N = 2

3	20	
모든 국가의 은메달 및 동메달 획득 수는 0

4	25	
N ≤ 500

5	35	
추가적인 제약 조건은 없다.

예제 입력 1 
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
예제 출력 1 
2
예제 입력 2 
4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0
예제 출력 2 
2

'''


# ===================================================================================================================


