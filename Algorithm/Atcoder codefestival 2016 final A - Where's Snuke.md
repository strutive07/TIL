# Atcoder codefestival 2016 final A - Where's Snuke?

<https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_a>



간단하게 완전탐색을 하면 된다.

시간도 최대 크기가 26*26인데 2초나 줘서 노상관. 100점짜리 문제는 역시는 역시다.



---



```c++
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
typedef long long int ll;
using namespace std;
#define INF 1234567890
#define LIMIT 1

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int _T = 0;
	int h, w;
	cin >> h >> w;
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			string s;
			cin >> s;
			if (s == "snuke") {
				cout << (char)(j + 'A' - 1) << i;
				return 0;
			}
		}
	}

	return 0;
}



```

