result = [0 for _ in range(26)]
for alphabet in input().strip(): result[ord(alphabet) - 97] += 1
print(*result)