# BOJ 16766 Convention



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
int n, m, c;
int values[LIMIT];

bool check(int waiting_time) {
	int cnt = 1;
	int start_index = 0;
	int start = values[start_index];
	for (int i = 1; i < n; i++) {
		if (
			values[i] - start > waiting_time
			|| i - start_index + 1 > c
			) 
		{
			cnt++;
			start_index = i;
			start = values[start_index];
		}
	}
	return cnt <= m;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	
	cin >> n >> m >> c;
	int maxtime = -1;
	for (int i = 0; i < n; i++) {
		cin >> values[i];
		maxtime = max(maxtime, values[i]);
	}
	sort(values, values + n);


	int left = 0, right = maxtime;

	while (left <= right) {
		int mid = (left + right) / 2;
		if (check(mid)) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	cout << left;

	return 0;
}


```



---

# Convention

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 512 MB      | 93   | 40   | 30        | 41.096%   |

## 문제

Farmer John is hosting a new bovine grass-eating convention at his farm!

Cows from all over the world are arriving at the local airport to attend the convention and eat grass. Specifically, there are N cows arriving at the airport (1≤N≤105) and cow i arrives at time ti (0≤ti≤109). Farmer John has arranged M (1≤M≤105) buses to transport the cows from the airport. Each bus can hold up to C cows in it (1≤C≤N). Farmer John is waiting with the buses at the airport and would like to assign the arriving cows to the buses. A bus can leave at the time when the last cow on it arrives. Farmer John wants to be a good host and so does not want to keep the arriving cows waiting at the airport too long. What is the smallest possible value of the maximum waiting time of any one arriving cow if Farmer John coordinates his buses optimally? A cow’s waiting time is the difference between her arrival time and the departure of her assigned bus.

It is guaranteed that MC≥N.

## 입력

The first line contains three space separated integers N, M, and C. The next line contains Nspace separated integers representing the arrival time of each cow.

## 출력

Please write one line containing the optimal minimum maximum waiting time for any one arriving cow.



## 예제 입력 1

```
6 3 2
1 1 10 14 4 3
```

## 예제 출력 1

```
4
```

## 힌트

If the two cows arriving at time 1 go in one bus, cows arriving at times 3 and 4 in the second, and cows arriving at times 10 and 14 in the third, the longest time a cow has to wait is 4 time units (the cow arriving at time 10 waits from time 10 to time 14).

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2018-2019 Season ](https://www.acmicpc.net/category/442)> [USACO 2018 December Contest ](https://www.acmicpc.net/category/443)> [Silver](https://www.acmicpc.net/category/detail/1987) 1번