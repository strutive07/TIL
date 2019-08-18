# BOJ 9663 N-Queen

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
#include <functional>

typedef long long int ll;
using namespace std;
#define INF 1234567890
#define N 200000

const int LIMIT = 1e+9;
int n, m;

bool a[30], b[30], c[30];

void solve(int here) {
	if (here == n) {
		m++;
		return;
	}
	for (int i = 0; i < n; i++) {
		if (a[i] || b[i + here] || c[here - i + n - 1]) continue;
		a[i] = b[i + here] = c[here - i + n - 1] = true;
		solve(here + 1);
		a[i] = b[i + here] = c[here - i + n - 1] = false;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	solve(0);
	cout << m;


	return 0;
}


```

---

# N-Queen

| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ----- | ---- | --------- | --------- |
| 10 초     | 128 MB      | 13869 | 8032 | 5203      | 57.600%   |

## 문제

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.



## 예제 입력 1

```
8
```

## 예제 출력 1

```
92
```



## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)