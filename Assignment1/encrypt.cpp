#include <bits/stdc++.h> 
using namespace std; 
  
void encrypt(char input[100]) 
{ 
    char even = '$', odd = '#'; 
    int repeat, ascii; 
  
    for (int i = 0; i <= strlen(input); i++)  
    { 
        ascii = input[i]; 
        repeat = ascii >= 97 ? ascii - 96 : ascii - 64; 
        for (int j = 0; j < repeat; j++) 
        {   
            if (i % 2 == 0) 
                cout << odd;      
            else
                cout << even; 			
        } 
    } 
} 
  
  
int main() 
{ 
    char input[100]; 
    cout<<"Enter the input: ";
    cin.getline(input,100);
    encrypt(input); 
    
    return 0; 
}
