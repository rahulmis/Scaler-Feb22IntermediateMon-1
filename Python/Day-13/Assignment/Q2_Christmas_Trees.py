
# Rahul Mishra
def solve1_optimized(A, B):
        ans = float('inf')
        for j in range(1, len(A)):
            temp_sum = B[j]
            val_i = float('inf')
            val_k = float('inf')
            for i in range(j-1, -1, -1):
                if A[i] < A[j] and B[i] < val_i:
                    val_i = B[i]
            for k in range(j+1, len(A)):
                if A[k] > A[j] and B[k] < val_k:
                    val_k = B[k]
            if val_i != float('inf') and val_k != float('inf'):
                temp_sum += val_i + val_k
                ans = min(temp_sum, ans)
        if ans != float('inf'):
            return ans
        else:
            return -1

# Rahul Mishra
def solve1_brute_force_approach(A, B):
        minimum_ = float('inf')
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    if B[i]+B[j]+B[k] < minimum_ and A[i] < A[j] < A[k]:
                        minimum_ = B[i]+B[j]+B[k]
        return minimum_ if minimum_ != float('inf') else -1