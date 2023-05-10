# [ 스택 ]
'''
- 선입후출
  가장 먼저 들어온 데이터가 가장 나중에 나가는 형식.입구와 출구가 동일함. 


'''
stack = []

stack.append(73)
stack.append(14)
stack.append(26)
stack.append(3)
stack.append(7)
stack.append(14)
stack.append(21)

# < 리스트의 맨 마지막에 있는 원소를 반환하고, 그 원소는 삭제함: pop() >
stack.pop() # 맨 마지막에 들어간 21 삭제
print(stack) # 남아있는 73, 14, 26, 3, 7, 14 출력


# < 리스트의 원소들을 순서대로 정렬해줌: sort() >
stack.sort() 
print(stack) # 출력값: 3, 7, 14, 14, 26, 73


# < 리스트에 새로운 원소 삽입: insert(인덱스 a번째 위치, 삽입하고자 하는 원소값) >
stack.insert(3, 150)
print(stack) # 출력값: 3, 7, 14, 150, 14, 26, 73


# < 리스트의 일부 원소 제거: remove(삭제하고자 하는 원소값(인덱스번호가 아니다!)) >
stack.remove(150)
print(stack) # 출력값: 3, 7, 14, 14, 26, 73


# < 삭제하고자 하는 특정 원소값이 이미 리스트에 여러 번 있는 상태라면, 첫 번째 그 특정 원소값만 삭제된다 >
stack.remove(14)
print(stack) # 출력값: 3, 7, 14, 26, 73


# < 리스트에 있는 특정 원소의 개수 세기(그 특정 원소가 몇 개나 리스트에 포함되어 있는지): count(특정 원소값) >
print(stack.count(26)) # 출력값: 1. 원소 26은 리스트에 딱 1개 있기 때문.
 

# < 특정 원소의 인덱스번호 반환: index(특정 원소값) >
print(stack.index(73)) # 출력값: 4. 원소 73의 인덱스번호는 4임.


# < 현재 리스트에 다른 리스트 붙이기(=리스트 확장): extend([다른 리스트]) >
stack2 = [5, 4, 3, 2, 1]
stack.extend(stack2)
# 또는, 'stack.extend([5, 4, 3, 2, 1])' 로 작성해도 동일하다!
print(stack) # 출력값: 3, 7, 14, 26, 73, 5, 4, 3, 2, 1


# < 리스트 뒤집기: reverse() >
stack.reverse()
print(stack) # 출력값: 1, 2, 3, 4, 5, 73, 27, 14, 7, 3


# < 스택의 최상단(맨 마지막에 삽입된) 원소'부터' 전체 원소를 위에서부터 아래로 출력: print(stack[::-1]) >
print(stack[::-1]) # 출력값: 


# < 스택의 최하단(맨 처음에 삽입된) 원소'부터' 전체 원소를 아래에서 위로 출력: print(stack[::])
print(stack)
