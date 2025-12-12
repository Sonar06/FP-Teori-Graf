def find_lis_dp(arr):
    if not arr:
        return 0, []

    n = len(arr)
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

    max_len = max(dp)
    end_index = dp.index(max_len)

    lis_sequence = []
    curr = end_index
    while curr != -1:
        lis_sequence.append(arr[curr])
        curr = parent[curr]
    
    lis_sequence.reverse()

    return max_len, lis_sequence

data = [4, 1, 13, 7, 0, 2, 8, 11, 3]

length, sequence = find_lis_dp(data)

print("--- Pendekatan Dynamic Programming ---")
print(f"Input: {data}")
print(f"Panjang Subsequence Terbesar: {length}")
print(f"Isi Subsequence: {sequence}")
