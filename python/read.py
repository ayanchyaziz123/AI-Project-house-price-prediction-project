import sys
sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    print(A)