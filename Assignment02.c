#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Enter value of n: ");
    scanf("%d", &n);

    /* -------------------- O(1) Space Complexity -------------------- */
    printf("\n1. Constant Space Complexity O(1)\n");
    int a = 10, b = 20, sum;
    sum = a + b;
    printf("Sum = %d\n", sum);

    /* -------------------- O(n) Space Complexity -------------------- */
    printf("\n2. Linear Space Complexity O(n)\n");
    int *arr = (int *)malloc(n * sizeof(int));

    for(int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    printf("Array Elements: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    free(arr);

    /* -------------------- O(n^2) Space Complexity -------------------- */
    printf("\n3. Quadratic Space Complexity O(n^2)\n");
    int **matrix = (int **)malloc(n * sizeof(int *));
    for(int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            matrix[i][j] = i + j;
        }
    }

    printf("Matrix:\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}