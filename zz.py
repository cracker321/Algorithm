

N = int(input())

# 소의 번호와 위치로 이루어져 있으니 --> 한 쌍 --> 딕셔너리 자료형 사용. '소의 위치와 번호 대한 정보 전체'를 뜻하는 변수명 cows 로 설정
cows = {}

# 소가 길을 건너간 최소 횟수를 출력해야 하나, 그 횟수를 카운팅하는 변수 cnt 생성 및 초기화
cnt = 0


for _ in range(N): # '예제 입력'에서처럼 입력되는 줄의 개수가 N개가 되니, 이렇게 for문 써야 함.
    cnumber, clocation = map(int, input().split()) # 소의 번호와 위치를 입력받고, 그것을 공백 띄워서 나눔.
    
    if cnumber not in cows: # 만약, 새롭게 입력되는 소의 번호가 기존의 딕셔너리에 없다면,
        cows[cnumber] = clocation # 새롭게 입력되는 소의 번호와 위치를 기존의 딕셔너리에 추가하고, : 딕셔너리에 새로운 원소 키, 값 추가하는 방법 참고.
    else: # 만약, 새롭게 입력되는 소의 번호가 기존의 딕셔너리에 있다면,
        cows[cnumber] != clocation # 또한, 새로운 입력으로 들어온 소의 위치('cows[number]')가 기존의 소의 위치('clocation')과 다르다면,
        cnt += 1 # 소가 이동한 것이 되므로, 소의 이동 횟수를 하나 늘려줌
        
        cows[cnumber] = clocation # 기존의 딕셔너리에 새로운 입력으로 들어온 소의 번호와 위치를 입력 및 업데이트 해줌.
        
        
    
        