from collections import Counter
from collections import defaultdict

T = int(input())

score = 1 # 개별 선수들의 점수

for _ in range(T): # 테스트케이스의 개수만큼 반복함
    
    player_numbers = int(input())
    
    teams = list(map(int, input().split()))
    
    teams_counter = Counter.teams # 개별 팀의 선수들의 수를 파악하기 위한 Counter함수 사용
    teams_score = defaultdict(list) # 개별 팀의 각 선수들의 점수들을 담을 defaultdict 객체 생성
    
    
    for i in range(player_numbers): # 모든 팀의 총 참가선수의 수 만큼 반복함
        team = teams[i]
        if teams_counter[i] < 6:
            continue    
        
        teams_socre[i]
