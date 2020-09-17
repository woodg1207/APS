def solution(prices):
    n = len(prices)
    result = []
    for i in range(n):
        time = 0
        for j in range(i+1, n):
            time += 1
            if prices[i] <= prices[j]:
                pass
            else:
                break
        result.append(time)

    return result
def solution(prices):
    n = len(prices)
    result = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            result[i] += 1
            if prices[i] <= prices[j]:
                pass
            else:
                break

    return result

P = [1, 2, 3, 2, 3]
print(solution(P))