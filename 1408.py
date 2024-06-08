t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [1] * n
    for i in range(n - 2, -1, -1):
        if arr[i] * arr[i + 1] < 0:
            res[i] = res[i + 1] + 1
    print(*res)

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int arr[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
        
        int res[n];
        for (int i = 0; i < n; i++) {
            res[i] = 1; // Initialize the result array with 1s
        }
        
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] * arr[i + 1] < 0) {
                res[i] = res[i + 1] + 1;
            }
        }
        
        for (int i = 0; i < n; i++) {
            printf("%d ", res[i]);
        }
        printf("\n");
    }
    return 0;
}

