# [ implementation ]

# [ 덩치 ]. 백준 7568번. 실버5
# https://www.acmicpc.net/problem/7568


# 튜플 --> 원소 추가, 삭제, 수정 불가. 즉, 변경이 불가능한 자료구조.
# 리스트 --> 원소 추가, 삭제, 수정 가능.


# ===================================================================================================================

# < 정답코드 1 >

import sys

N = int(sys.stdin.readline().strip()) # 'sys.stdin.readline()' = 'input()' 과 같은 역할임.
                                      # int()와 split()은 절대 map() 또는 list(map(int, ..)) 없이는 같이 올 수 없다!
each_body = [] # 각 사람의 몸무게와 키를 저장할 리스트 body 생성.

for _ in range(N):
    rnk = 0
    
    x, y = map(int, sys.stdin.readline().strip().split())

    each_body.append([x, y])
    
for i in each_body: # 첫 번째 비교의 기준이 되는 i번째 사람의 뭄무게와 키를 꺼냄(=이차원리스트 body의 큰 덩이묶음을 꺼냄)
    rnk = 1 # 등수는 당연히 1부터 시작함. 
    '''
    초기값으로 1을 지정하는 이유는 자기 자신을 포함한 덩치 등수 누적 계산을 고려해야하기 때문입니다. 
    예를 들어 한 사람의 키와 몸무게가 다른 사람보다 크지만 다른 두 사람보다 작은 경우 이 사람의 덩치 등수가 3이어야 합니다. 
    따라서 처음부터 자기 자신의 덩치 등수를 포함시키기 위해값을 1로 설정하는 것입니다.

    각 사람의 덩치를 비교할 때 자기 자신과는 비교할 필요가 없지만, 초기값 1로 지정함으로써 별도의 처리 없이 등수 계산이 가능합니다. 
    이에 for문을 사용하여 다른 사람들과 덩치를 비교하면서 더 작은 경우 등수를 1씩 증가시켜 순위를 매길 것.

    즉, 'rnk = 1' 코드는 각 사람의 덩치 등수를 저장하고 초기값을 자기 자신을 포함한 1로 지정하는 데 사용됩니다. 
    이로 인해 간단히 등수 계산을 할 수 있습니다.
    =========
    따라서 rnk를 0으로 초기화할 경우, 현재 사람의 등수가 0으로 나오게 됩니다. 
    하지만 실제로는 등수는 1부터 시작해야 합니다. 따라서 rnk를 1로 초기화하여 시작하게 됩니다.
    '''
    for j in each_body: # 그리고, 그 사람과 비교할 j번째 사람의 몸무게와 키를 꺼냄(=다른 큰 덩이묶음을 하나씩 꺼냄).

        if i[0] < j[0] and i[1] < j[1]: # [0]은 몸무게, [1]은 키를 뜻함. 
                                        # 첫 번째 비교의 기준이 되는 i번째 사람의 키와 몸무게가 그 비교대상이 된느 j번째 사람의 키와 몸무게보다 작다면
                                        # (즉,몸무게와 키 모두 자신보다 큰 사람이라면)
            rnk += 1 # 첫 번째 비교의 기준이 되는 i번째 사람의 등수는 계속 뒤로 밀려나는 것임(= 등수의 숫자가 커짐)

    print(rnk, end = ' ') # 개별 사람의 등수는 첫 번째 for문이 끝날 때, 즉 비교를 시작하는 첫 번째 사람을 기준으로 시작했기 때문에,
                          # 첫 번째 for문이 끝날 때 계산해야 하는 것이다.
        
        

# ===================================================================================================================

# < 정답코드 2 >

'''

n = int(input())
 
data = [] # 사람들의 키와 몸무게들을 정보를 저장할 리스트 data
ans = [] # 등수정보를 저장할 리스트 ans

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # 몸무게와 키를 묶어서 append 해줌
 
for i in range(n):
    count = 0 # i번째 사람의 덩치보다 덩치가 더 큰 사람의 수를 세기 위한 변수 count를 초기화.
    for j in range(n): # 'for j in range(j+1, n)'이 아닌 이유 :
                       # 만약, j+1로 한다면, '1번 사람은 2, 3, 4, 5번과만 비교', '2번 사람은 3, 4, 5번과만 비교', '3번 사람은 4, 5번과만 비교' ..
                       # 이러면, 모든 사람들이 전체적으로 딱 한 번씩만 서로 비교는 되지만,
                       # 정작 가장 중요한 '각각 개별 사람 기준의 등수'는 놓치게 됨.
                       # 왜냐하면, '개인 등수'는 모든 사람들이 전체적으로 딱 한 번씩만 서로 비교 되는지 여부와 관계 없이
                       # 각각 개별 기준으로 다시 1대 5로 또다시 비교해야 등수를 알아낼 수 있기 때문이다!
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
                                                                # 만약, i번째 사람의 몸무게와 키가 j번재 사람의 몸무게와 키보다 작다면
            count += 1 # i번째 사람보다 덩치가 큰 사람 한 명 추가됨.
    ans.append(count + 1) # 덩치 등수는 자신보다 몸무게 키 모두 큰 사람의 수에다가 + 1을 한 것이므로(당연..! 생각해보면 됨) count + 1을 ans에 append한다.
 
for d in ans:
    print(d,end=" ") # 'end = " "'가 있기 때문에, 일렬로 공백 한 칸 띄워 나열할 수 있는 것임.


'''


# ===================================================================================================================


'''
문제
우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 
어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다. 
두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 
예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈이 된다. 
그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우도 있다. 
예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 
키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

이름	(몸무게, 키)	덩치 등수
A	(55, 185)	2
B	(58, 183)	2
C	(88, 186)	1
D	(60, 175)	2
E	(46, 155)	5
위 표에서 C보다 더 큰 덩치의 사람이 없으므로 C는 1등이 된다. 
그리고 A, B, D 각각의 덩치보다 큰 사람은 C뿐이므로 이들은 모두 2등이 된다. 
그리고 E보다 큰 덩치는 A, B, C, D 이렇게 4명이므로 E의 덩치는 5등이 된다. 
위 경우에 3등과 4등은 존재하지 않는다. 여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.



입력
첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.



출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.



제한
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200



예제 입력 1 
5
55 185
58 183
88 186
60 175
46 155



예제 출력 1 
2 2 1 2 5
'''

