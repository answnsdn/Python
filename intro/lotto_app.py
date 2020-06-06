from lt import lottos

pick = lottos.lotto()
print(pick)

# 1. 만약 4등한 적이 있으면 4등 몇 번 했습니다.
if pick['4th'] >= 1:
    print(f'4등 {pick["4th"]}번 했습니다.')
else :
    print('fail')