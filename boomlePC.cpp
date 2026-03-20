#include <iostream>

//Test fuite mémoire

int f()
{
    pid_t fork(void);
    int* a = new int[10];
    while(1)
    {
        a = new int[10];
        pid_t fork(void);
    }
    return 0;
}

int main()
{
    f();
    return 0;
}