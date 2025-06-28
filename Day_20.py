""" coin = [2, 3, 4, 5]
amt = 12
if amt > sum(coin):
    print("Not possible")
dp = [[0] * (amt + 1) for _ in range(len(coin))]

# Base case: sum 0 is always possible

for i in range(len(coin)):
    dp[i][0] = 1

# First coin case

if coin[0] <= amt:
    dp[0][coin[0]] = 1

# Fill the dp table

for i in range(1, len(coin)):
    for j in range(1, amt + 1):
        if j < coin[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - coin[i]]

# Print the dp table

for row in dp:
    print(row)

# Final result

if dp[-1][amt]:
    print("Possible to form", amt)
else:
    print("Not possible") """

# # User input
# nums = list(map(int, input("Enter numbers separated by space: ").split()))

# # Frequency count using dictionary
# d = {}
# for num in nums:
#     if num in d:
#         d[num] += 1
#     else:
#         d[num] = 1

# # Sort by frequency ascending, then value descending
# nums.sort(key=lambda x: [d[x],-x])

# # Output result
# print("Sorted by frequency:", nums)

