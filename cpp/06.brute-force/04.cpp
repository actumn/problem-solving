#include <ios>
#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

int n;
bool areFriends[10][10];
int countPairings(bool taken[10]) {
    int firstFree = -1;
    for (int i = 0; i < n; ++i) {
        if (!taken[i]) {
            firstFree = i;
            break;
        }
    }

    if (firstFree == -1) return 1;

    int ret = 0;
    for (int pairWith = firstFree + 1; pairWith < n; ++pairWith) {
        if (!taken[pairWith] && areFriends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairings(taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    }
    return ret;
}


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int C = 0;
    cin >> C;
    
    for (int i = 0; i < C; i++) {
        int m;
        cin >> n >> m;
        for (int j = 0; j < m; j++) {
            int left, right;
            cin >> left >> right;
            areFriends[left][right] = true;
        }

        bool taken[10];
        memset(&taken, false, sizeof(taken));

        cout << countPairings(taken) << '\n';
    }
}
