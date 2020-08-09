#include<iostream>
#include<string.h>
using namespace std;
int main() {
   cout<<"Enter the message:\n";
   char message[100], ch;
   cin.getline(message,100);
   int i, j, length, choice, key = 5;
   length = strlen(message);
   cout<<"Enter your choice \n1. Encryption \n2. Decryption \n";
   cin>>choice;
   if (choice==1) {
      for(int i = 0; message[i] != '\0'; ++i) {
        ch = message[i];
       
        if (ch >= 'a' && ch <= 'z'){		//lowercase
            ch = ch + key;
            if (ch > 'z') {
               ch = ch - 'z' + 'a' - 1;
            }  
            message[i] = ch;
        }
        
        else if (ch >= 'A' && ch <= 'Z'){			//uppercase
        	ch = ch + key;
            if (ch > 'Z'){
               ch = ch - 'Z' + 'A' - 1;
            }
            message[i] = ch;
         }
      }
      printf("Encrypted message: %s", message);
   }
   
   else if (choice == 2) { 
      char ch;
      for(int i = 0; message[i] != '\0'; ++i) {
         ch = message[i];
    
         if(ch >= 'a' && ch <= 'z') {			//lowercase
            ch = ch - key;
            if(ch < 'a'){
               ch = ch + 'z' - 'a' + 1;
            }
            message[i] = ch;
         }
         										
         else if(ch >= 'A' && ch <= 'Z') {		//uppercase 
            ch = ch - key;
            if(ch < 'A') {
               ch = ch + 'Z' - 'A' + 1;
            }
            message[i] = ch;
         }
      }
      cout << "Decrypted message: " << message;
   }
   return 0;
}
