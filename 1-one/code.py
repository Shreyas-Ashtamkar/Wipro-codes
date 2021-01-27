N      = input().strip()
M1, P1 = input().strip().split()
M2, P2 = input().strip().split()

N, M1, P1, M2, P2 = map(int,(N, M1, P1, M2, P2))

ceil = lambda x, y: -1

prices = []

M1_c = 0
M2_c = 0

for boxesA in range(ceil(N/M1)):
    apples_remaining = N - (boxesA*M1)
    boxesB = ceil(apples_remaining/M2)

    prices.append(boxesA*P1 + boxesB*P2)

print(min(prices))
