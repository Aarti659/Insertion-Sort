// Insertion sort in C++

#include <iostream.h>

using namespace std;


void priArr(int ar[], int size) {
  for (int i = 0; i < size; i++) {
    cout << ar[i] << " ";
  }
  cout << endl;
}

void inserSort(int ar[], int size) {
  for (int step = 1; step < size; step++) {
    int key = ar[step];
    int j = step - 1;

    
    while (key < ar[j] && j >= 0) {
      ar[j + 1] = ar[j];
      --j;
    }
    ar[j + 1] = key;
  }
}


int main() {
  int item[] = {7, 5, 2, 1, 9};
  int size = sizeof(item) / sizeof(item[0]);
  inserSort(item, size);
  cout << "Sorted array in ascending order:\n";
  priArr(item, size);
  return 0;
}




