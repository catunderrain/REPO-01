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
    int k;
    for (i; i < n; i++)
    {

        printf("\nNhap A%d = ", (i + 1));
        scanf("%d", &k);
        A[i] = k;
    }
    printf("Mang A: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
}
