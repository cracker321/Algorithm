# [ DFS(Depth-First Search) 깊이우선탐색 ]

'''
파이썬의 리스트 = 자바의 배열

- DFS는 한 번 방문한 노드를 다시 방문하면 안 되므로, 노드 방문 여부를 체크할 방문 리스트 필요하며, 그래프는 인접 리스트로 표현함. 
- DFS의 탐색 방식은 후입선출 특성을 가지므로 스택을 사용하여 설명함.
- 다만, DFS 구현은 스택보다는 스택 성질을 갖는 재귀 함수로 많이 구현함. 


2. 스택에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 스택에 삽입하기
  - pop을 수행하여 이제 막 방문한 노드를 스택으로부터 꺼낸 후, 그 노드 근처에 방문해야 할 인접노드가 뭐가 있는지 확인하는 단계
  - 이제 그 인접노드를 스택에 삽입하는 것 

3. 스택 자료구조에 값이 없을 때까지 반복하기
  - 앞의 과정을 스택 자료구조에 값이 없을 때까지 반복함. 이 때, 다녀간 노드는 방문배열 바탕으로 재삽입하지 않는 것이 핵심임!

'''

# < 문제 23: 방향 없는 그래프가 주어졌을 대 연결 요소(connected components)의 개수를 구하는 프로그램을 작성하시오 >
'''
방향 없는 그래프가 주어졌을 때 연결 요소의 개수를 구하는 프로그램을 작성하시오. 
입력: 1번째 줄에 노드의 개수 N(1<=N<=1000)과 에지의 개수 M(0<=M<=N*(N-1)/2), 2번째 줄부터 M개의 줄에 에지의 양끝 점 u와 v가 주어진다(1<=u, v<=N, u와 v는 같지 않다). 
같은 에지는 한 번만 주어진다.
'''
# 해설: 
# https://www.youtube.com/watch?v=Y2kHlj7xqfU&list=PLFgS-xIWwNVU_qgeg7wz_aMCk22YppiC6&index=13&ab_channel=%ED%95%98%EB%A3%A8%EC%BD%94%EB%94%A9  또는 교재 p139
# https://www.youtube.com/watch?v=yvWmjljjYJY&ab_channel=%EC%BD%94%EB%8D%B0%ED%92%80 

'''
# 수도코드 작성. 교재 p 139~

==============================================================================================
n(노드 개수) m(에지 개수)
A(그래프의 데이터를 저장해주는 인접리스트) 초기화
visited(방문기록 리스트) 초기화

# DFS 구현

DFS:
    visited 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS를 실행('재귀함수' 형태)
    
for m의 개수 만큼 반복:
    '인접 리스트 A'에 그래프 데이터 저장
    
for n의 개수 만큼 반복:
    if 방문하지 않은 노드가 있으면:
        연결요소 개수의 값 1 증가
        DFS 실행
        
연결 요소의 개수 값 출력    
==============================================================================================

# 해설:
- '연결 요소'란, '에지로 연결된 노드들의 집합'임.
- 모든 노드를 탐색하는 데 실행한 DFS의 실행 횟수 = 연결 요소의 개수
  즉, '한 번의 DFS가 끝날 때까지 탐색한 모든 노드들의 집합 하나'를 '하나의 연결 요소'로 판단할 수 있음.
  따라서, 만약에 그래프가 모두 연결되어 있었다면(노드들이 모두 연결되어 있었다면), DFS는 딱 1번만 실행되었을 것임.

- 1 --> 2 --> 5 : DFS 1회차. 이게 하나의 연결요소 집합
  이후, 이제 방문하지 않았던 3번 노드로 가는 것임.
- 3 --> 4 --> 6 : DFS 2회차. 이게 하나의 연결요소 집합

- 연결된 노드 중 방문하지 않은 노드가 여러 개라면, 그 중 아무 노드나 갈 수 있음.

'''




