#include <stdio.h>
#include <stdlib.h>

void printArray(int *a, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
}

#define MAX_LINE_SIZE 10000   // maximum size of a line of input

int scanArray(int *a) {
    // scan line of text
    char line[MAX_LINE_SIZE];
    scanf("%[^\n]", line);    // legge i caratteri fino all'a capo escluso
    getchar();

    // convert text into array
    int size = 0, offset = 0, numFilled, n;
    do {
        numFilled = sscanf(line + offset, "%d%n", &(a[size]), &n);   // sscanf legge da stringa e non da standard input, %n indica il numero di caratteri consumati
        if (numFilled > 0) {
            size++;
            offset += n;
        }
    } while (numFilled > 0);

    return size;
}

int ricerca_dicotomica(int *a, int n, int key) {
   int i = 0;
   int j = n;
   while (i < j) {
      int m = (i + j) / 2;
      if (key == a[m]) {
         return m;
      } else if (key < a[m]) {
         j = m;
      } else {
         i = m + 1;
      }
   }
   return -1;
}


int main() {
   printf("Inserire array: ");
   int a[10000];
   int n = scanArray(a);

   printf("Inserire chaive: ");
   int key;
   scanf("%d", &key);

   printf("%d", ricerca_dicotomica(a, n, key));
}