#Perfect square check (mirrors Q9 — flag pattern)
#Ask for a number n. Loop i from 1 upward, and check if i * i == n for any i. If yes → "perfect square", if the loop ends without finding one → 
# "not a perfect square". Use a flag variable — no for...else this time, I want the flag from memory. Test: 25 (yes), 26 (no), 1 (yes).

print('Enter the value of n:')
n = int(input())

for i in range(1, n+1):
     if i * i == n:
        print('Its a perfect square')
        break
else:
        print('Not a perfect square')