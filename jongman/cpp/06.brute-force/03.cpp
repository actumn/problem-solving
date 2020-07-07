#include <ios>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int dx[8] = { -1, -1, -1,  1,  1,  1,  0,  0 };
const int dy[8] = { -1,  0,  1, -1,  0,  1, -1,  1 };

char board[][5] = {
    {'U', 'R', 'L', 'P', 'M'},
    {'X', 'P', 'R', 'E', 'T'},
    {'G', 'I', 'A', 'E', 'T'},
    {'X', 'T', 'N', 'Z', 'Y'},
    {'X', 'O', 'Q', 'R', 'S'},
};

bool inRange(int y, int x) {
    return 0 <= x && x < 5 && 0 <= y && y < 5;
}

bool hasWord(int y, int x, const string& word) {
    if (!inRange(y, x)) return false;

    if (board[y][x] != word[0]) return false;

    if (word.size() == 1) return true;

    for (int direction = 0; direction < 8; ++direction) {
        int nextY = y + dy[direction], nextX = x + dx[direction];

        if (hasWord(nextY, nextX, word.substr(1)))
            return true;
    }

    return false;
}

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(NULL);
    // cout.tie(NULL);
    cout << hasWord(1, 1, "PRETTY") << '\n';

    return 0;
}
