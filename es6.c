#include <stdio.h>
#include <stdlib.h>

void printArray(int *a, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
}

#define MAX_LINE_SIZE 10000  // maximum size of a line of input

int scanArray(int *a) { 
    // scan line of text
    char line[MAX_LINE_SIZE];
    scanf("%[^\n]", line); //tutti caratteri escluso a capo
    getchar(); //consuma a capo

    // convert text into array
    int size = 0, offset = 0, numFilled, n;
    do {
        numFilled = sscanf(line + offset, "%d%n", &(a[size]), &n); //scanf consuma da input e converte, sscanf -> stringa
        if (numFilled > 0) { //line + offset, line puntatore, offeset intero. numFilled
            size++;
            offset += n; //n numero di caratteri che ho appena consumato %[n]
        }
    } while (numFilled > 0);

    return size;
}

int ricerca_dicotomica(int *a, int n, int key) {
    int i = 0;
    int j = n;
    while (i < j) {
        int m = (i + j) / 2;
        if (key == a[m]){
            return m;
        } else if (key < a[m]){
        j = m;
        }else{ 
        i = m +1;
        }
        
    }
    return -1;
}

int main() {
    int a[10000];
    int n =scanArray(a);

    int key;
    scanf("%d",&key);

    printf("%d",ricerca_dicotomica(a, n, key));
    return 0;
}

