#input
    # 0:정보과학관/1:전산관/2:미래관/3:신앙관/4:환경직/5:진리관/6:학생회관/7:형남공학관
DP = [1,0,0,0,0,0,0,0]                          # 시작 시 어느 지점에 존재하는가?


# solve
def nxt(state):                                 # state :
    tmp = [0 for _ in range(8)]                 # tmp : 해당 지점에서 정보과학관까지 도달하는 방법?(어디를 거치게 되는가?)
    tmp[0] = state[1] + state[2]                # 각 시간적 정보를 저장한다. 1분전까지 도착해야 하는 곳
    tmp[1] = state[0] + state[2] + state[3]     # 2분전까지 도착해야 하는 곳...
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    return tmp

# input
for i in range(int(input())):                   # 여기를 한바퀴 돌때마다 1분동안 어디에 갈 수 있는지 알 수 있다.
    DP = nxt(DP)                                # 다 돌고나면 input()한 숫자만큼 지난 후에 해당 위치로 몇번이나 갈 수 있는지 계산된다.

print(DP[0] * 1000000007)