# [ implementation ]

# [ 집합 ]. 백준 11723번. 브론즈
# https://www.acmicpc.net/problem/11723
# https://mong9data.tistory.com/91


# 커서를 문장 맨 앞으로 이동: home 버튼
# 커서를 문장 맨 끝으로 이동: end 버튼
# 커서를 해당 단어블록 끝으로 이동: ctrl + <- 또는 ->
# 커서를 블록단위로 빠르게이동: ctrl + shift + <- 또는 ->
# 블록지정하여 커서를 오른쪽으로 이동: shift + <- 또는 ->


import sys

M = int(sys.stdin.readline().strip()) # 여기서 split()을 사용할 수 없는 이유는(사용하면 TypeError 발생), split()은 '입력된 문자열'을 '리스트'로 반환하는데,
                                      # int함수는 '리스트'를 '정수형'으로 바꿔줄 수가 없기 때문이다.
                                      # 따라서, 그냥 애초에 split()을 사용하지 않고, 입력된 문자열을 바로 그냥 정수형 int로 변환시키는 거다!
                                      # https://ccamppak.tistory.com/38 참조.
S = set()



for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set({i for i in range (1, 21)}) # 이거는 set([]) 이렇게 하나, set({}) 이렇게 하나 상관 없는 듯..?
        elif temp[0] == 'empty':
            S = set()
    
    else:
        temp[1] = int(temp[1])
        if temp[0] == 'add':
            S.add(temp[1])
        elif temp[0] == 'remove':
            S.discard(temp[1])
        elif temp[0] == 'check':
            print(1 if temp[1] in S else 0)
        elif temp[0] == 'toggle':
            if temp[1] in S:
                S.discard(temp[1])
            else:
                S.add(temp[1])    
        
    

# =============================================================================================


'''
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 


입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.


출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1


예제 출력 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0

'''


# =============================================================================================


# < 정답코드 1 >
import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split() # 입력되는 여러 개의 개별 문자열(=개별 단어)이 'split()에 의해 나눠지고 리스트의 원소로 변환'됨.
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)


# =============================================================================================





# =============================================================================================


# < 내 오답코드 >
'''
import sys

M = int(input())
S = set()

def set_add(x):
    if x not in S:
        S.add(x)
        
def set_remove(x):
    if x in S:
        S.remove(x)

def set_check(x):
    if x in S:
        print(x)
    else:
        print(0)
        
def set_toggle(x):
    if x in S:
        S.remove(x)
    elif x not in S:
        S.add(x)
        
def set_all():
    for i in range(1, 21):
        element = set(i)
        S.append(element)
        
def set_empty():
    S.clear()
    


for _ in range(M):
    A, B = map(str, sys.stdin.readline().split()) # 반복문으로 여러 줄을 입력받는 상황에서 반드시 sys.stdin.readline()을 사용해야 시간초과 발생하지 않는다!
    
    if A == 'add':
        set_add(B)
    
    if A == 'remove':
        set_remove(B)
        
    if A == 'check':
        print(set_check(B))
        
    if A == 'toggle':
        set_toggle(B)
        
    if A == 'all':
        set_all()
    
    if A == 'empty':
        set_empty()
 '''   
    

# =============================================================================================




# =============================================================================================

'''
    
< 정답코드 1 >



'''

# =============================================================================================

'''
< 정답코드 2 >


    
'''

# =============================================================================================



