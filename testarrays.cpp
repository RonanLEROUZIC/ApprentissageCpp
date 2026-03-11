#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "nombre de caractère : ";
    cin >> n;
    int a[n]; // Créé un array de n
    int somme=0;
    
    for (int i = 0; i < n; i++)
    {
        cout << "veuillez entrer un nombre : ";
        cin >> a[i];
        //cout << a[i] << "\n";
        somme+=a[i];
    }
    cout << "Moyenne : " << somme/n;

    return 0;
}