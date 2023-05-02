# [ 큐 ]
'''
- 선입선출(FIFO)
  가장 먼저 들어온 데이터가 가장 먼저 나가는 형식의 자료구조
- 입구와 출구가 모두 뚫려 있는 '터널'과 같은 형태로 시각화할 수 있음.
'''

from collections import deque

# < queue에 원소값(데이터)을 추가: put(원소값) >
queue.put('hello')
queue.put('world')

print(queue) # 출력값: 
 