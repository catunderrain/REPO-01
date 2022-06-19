#include <stdio.h>
int main()
{
    int n;
    printf("\nNhap n = ");
    scanf("%d", &n);
    while (n >= 100 || n <= 0)
    {
        printf("\nn khong phu hop, nhap lai n (0<n<100): ");
        scanf("%d", &n);
    }
    int i = 0;
    int A[n];
    for (i; i < 3; i++)
    {

        printf("\nNhap A%d = ", (i + 1));
        scanf("%d", &n);
        A[i] = n;
    }
    printf("Gia tri n = %d", n);
    printf("%d",A);
}
