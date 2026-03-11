using namespace std;
#include <iostream>



int main(){
    int b = 0;
    cin >> b;
    int n;
    while(b!=n){
        if(b>n) cout << "Vous êtes au dessus ";
        else if(b<n) cout << "Vous êtes en dessous ";
        else {cout << "bravo ! "; return 0;}
        cout << "veuillez entrer un nombre : ";
        cin >> b;
    }
}