#include "AwesomeProject/fibonacci.h"

int AwesomeProject::fibonacci(unsigned int n)
{
    int t0 = 0, t1 = 1, t;

    if (n == 0) {
        return t0;
    }
    if (n == 1) {
        return t1;
    }
    for (unsigned i = 2; i <= n; ++i) {
        t = t0 + t1;
        t0 = t1;
        t1 = t;
    }

    return t;
}
