#include <ios>
#include <iostream>
using namespace std;

int sum(int n) {
	int ret = 0;
	for (int i = 1; i <= n; ++i)
		ret += i;

    return ret;
}

int recursiveSum(int n) {
    if (n == 1) return 1;

    return n + recursiveSum(n-1);
}



int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n = 0;
    cin >> n;

    cout << sum(n) << '\n';
    cout << recursiveSum(n) << '\n';

	return 0;	
}
