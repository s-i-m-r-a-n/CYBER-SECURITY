#include <stdio.h>
#include <stdlib.h>

int smallestElement(int A[], int n){
   int temp = A[0];
   for(int i=0; i<n; i++) {
      if(temp>A[i]) {
         temp=A[i];
      }
   }
   return temp;
}

int main(int argc, char *argv[])
{
  int a[100],b;
  int i, n=0;
  
  if(argc<2)
  {
    printf("Please use \"file_name value1 value2 ... \"\n");
    return -1;
  }
  
  for(int i=1; i<argc; i++){
      a[i-1]= atoi(argv[i]);
      n++;
     }
     int smallest = smallestElement(a, n);
     printf("Smallest Element is: %d\n ",smallest);
  
  return 0;
}
