#include <stdio.h>
#include <stdlib.h>
void constantSpace(int n){
int max = n;
int target = n;
for(int i = 1; i <=max ; i++){
if(i == target){
break;
}
}
printf("O(1) space used: %lu bytes\n", sizeof(max) + sizeof(target) + sizeof(n));
}
void linearSpace(int n){
int max = n;
int *arr = (int *)malloc(n * sizeof(int));
if (arr == NULL) {
printf("Memory allocation failed\n");
return;
}
for (int i = 0; i <= max; i++){
arr[i] = i + 1;
}
printf("O(n) space used: %lu bytes\n", sizeof(max) + sizeof(int) * n + sizeof(n));
free(arr);
}
void quadraticSpace(int n){
int max = n;
int **matrix = (int **)malloc(n * sizeof(int *));
if (matrix == NULL) {
printf("Memory allocation failed\n");
return;
for(int i = 0; i < max; i++){
for(int j = 0; j < max; j++){
matrix[i][j] = j;
}
}
}
printf("O(n^2) space used: %lu bytes\n", sizeof(max) + sizeof(int) * n * n + sizeof(n));
free(matrix);
}
int main(){

int n;
printf("Enter input size: ");
scanf("%d", &n);
constantSpace(n);
linearSpace(n);
quadraticSpace(n);
return 0;
}