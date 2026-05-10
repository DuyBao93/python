# Quy hoạch động mẫu
# n, S = map(int, input().split())
# w = list(map(int, input().split()))

# print (w)
# dp = [[0 for _ in range(n)] for _ in range(S + 1)]
# for i in range(n):
#     dp[0][i] = 1

# print (dp)

# for i in range(1, S + 1):
#     for j in range(n):
#         x = dp[i - w[j]][j] if i - w[j] >= 0 else 0
#         y = dp[i][j - 1] if j >= 1 else 0
#         dp[i][j] = x + y


# print(dp)

#Bài toán fibonanci

#Dệ quy chia để trị
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# # Dùng quy hoạch động
# def dpFib(n):
#     dp = [0 for col in range(0, n + 1)]
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i-2] + dp[i-1]
#     return dp

# def main():
#     n = 5
#     print ("Dung de quy chia de tri : ")
#     print (fib(n))
#     print ("Dung quy hoach dong : ")
#     print (dpFib(n))

def main():
    list = [1, 2, 3]
    print (len(list))
if __name__ == "__main__":
    main()


