#include <stdio.h>
#include <stdlib.h>

void solve(int floor, int ho)
{
    int cnt = 0;
    int info[floor*ho+ho];

    for (int i = 0; i < ho; i++)
    {
        info[i] = i+1;
    }
    for (int i = 1; i <= floor; i++)
    {
        for (int j = 0; j < ho; j++)
        {
            cnt += info[(i-1)*ho+j];
            info[i*ho+j] = cnt;
        }
        cnt = 0;
    }
    printf("%d\n",info[floor*ho+ho-1]);
}

int main(void)
{
    int n;
    scanf("%d",&n);
    int *arr = (int *)malloc(sizeof(int) *(n*2));
    if (arr == 0)
        return 0;
    for (int i = 0; i < n*2; i++)
        scanf("%d", &arr[i]);
    for (int i = 0; i < n; i++)
        solve(arr[i*2], arr[(i*2)+1]);
    free(arr);

    return 0;
}