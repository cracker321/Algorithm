# 입력 받기
N = int(input())
plans = input().split()

# 변수 초기화
x, y = 1, 1

# 이동 계획서 처리
for plan in plans:
    # 이동 후의 좌표를 저장할 변수 초기화
    nx, ny = x, y #  파이썬의 다중할당
                  # 
    
    if plan == 'L': # 왼쪽으로 이동
        nx -= 1
    elif plan == 'R': # 오른쪽으로 이동
        nx += 1
    elif plan == 'D': # 아래로 이동
        ny += 1
    elif plan == 'U': # 위로 이동
        ny -= 1

    # 새로운 좌표가 범위 내인지 확인
    if 1 <= nx <= N and 1 <= ny <= N:
        nx, ny   # 새로운 좌표를 x, y에 할당

# 최종 위치 출력
print(nx, ny)