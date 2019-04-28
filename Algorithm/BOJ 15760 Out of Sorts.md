# BOJ 15760 Out of Sorts

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
#define LIMIT 100005
pair<int, int> A[LIMIT];

int n, m;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i].first;
		A[i].second = i;
	}
	sort(A, A + n);
	int res = 0;
	for (int i = 0; i < n; i++) res = max(res, A[i].second - i);
	
	cout << res+1;
	

	return 0;
}


```



---

# Out of Sorts

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 512 MB      | 163  | 73   | 60        | 46.154%   |

## 문제

Keeping an eye on long term career possibilities beyond the farm, Bessie the cow has started learning algorithms from various on-line coding websites.

Her favorite algorithm thus far is "bubble sort". Here is Bessie's implementation, in cow-code, for sorting an array A of length N.

```
sorted = false
while (not sorted):
   sorted = true
   moo
   for i = 0 to N-2:
      if A[i+1] < A[i]:
         swap A[i], A[i+1]
         sorted = false
```

Apparently, the "moo" command in cow-code does nothing more than print out "moo". Strangely, Bessie seems to insist on including it at various points in her code.

Given an input array, please predict how many times "moo" will be printed by Bessie's code.

## 입력

The first line of input contains N (1≤N≤100,000). The next N lines describe A[0]…A[N−1], each being an integer in the range 0…109. Input elements are not guaranteed to be distinct.

## 출력

Print the number of times "moo" is printed.



## 예제 입력 1

```
5
1
5
3
8
2
```

## 예제 출력 1

```
4
```



## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2017-2018 Season ](https://www.acmicpc.net/category/410)> [USACO 2018 US Open Contest ](https://www.acmicpc.net/category/423)> [Silver](https://www.acmicpc.net/category/detail/1868) 1번