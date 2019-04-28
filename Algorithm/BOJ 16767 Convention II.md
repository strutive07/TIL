# BOJ 16767 Convention II

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
#define LIMIT 1
int n, m;

typedef pair<ll, ll> pl;

vector<pair<ll, pl>> vc;
priority_queue<pl, vector<pl>, greater<pl>> waiting_queue;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, t;
		cin >> a >> t;
		vc.push_back({a, {i, t}});
	}
	sort(vc.begin(), vc.end());

	ll res = 0;
	ll before_cow_finish_time = vc[0].first + vc[0].second.second;
	ll cur_cow_index = 1;
	
	while (cur_cow_index < n || waiting_queue.size() > 0) {
		
		// waiting 조건
		while (
				cur_cow_index < n 
				&& vc[cur_cow_index].first <= before_cow_finish_time
			) 
		{
			waiting_queue.push({vc[cur_cow_index].second.first, cur_cow_index });
			cur_cow_index++;
		}
		if (waiting_queue.size() == 0 && cur_cow_index < n) {
			before_cow_finish_time= vc[cur_cow_index].first + vc[cur_cow_index].second.second;
			cur_cow_index++;
		}
		else {
			pl head = waiting_queue.top();
			waiting_queue.pop();
			//cout << res << "\n";
			//cout << head.first << " " << head.second << " " << ll(before_cow_finish_time - vc[head.second].first) << " " << "\n";
			res = max(res, before_cow_finish_time - vc[head.second].first);
			before_cow_finish_time = before_cow_finish_time + vc[head.second].second.second;
		}
	}
	cout << res;


	return 0;
}


```



---





# Convention II

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 512 MB      | 50   | 27   | 20        | 50.000%   |

## 문제

Despite long delays in airport pickups, Farmer John's convention for cows interested in eating grass has been going well so far. It has attracted cows from all over the world.

The main event of the conference, however, is looking like it might cause Farmer John some further scheduling woes. A very small pasture on his farm features a rare form of grass that is supposed to be the tastiest in the world, according to discerning cows. As a result, all of the Ncows at the conference (1≤N≤105) want to sample this grass. This will likely cause long lines to form, since the pasture is so small it can only accommodate one cow at a time.

Farmer John knows the time ai that each cow i plans to arrive at the special pasture, as well as the amount of time ti she plans to spend sampling the special grass, once it becomes her turn. Once cow i starts eating the grass, she spends her full time of ti before leaving, during which other arriving cows need to wait. If multiple cows are waiting when the pasture becomes available again, the cow with the highest seniority is the next to be allowed to sample the grass. For this purpose, a cow who arrives right as another cow is finishing is considered "waiting". Similarly, if a number of cows all arrive at exactly the same time while no cow is currently eating, then the one with highest seniority is the next to eat.

Please help FJ compute the maximum amount of time any cow might possibly have to wait in line (between time ai and the time the cow begins eating).

## 입력

The first line of input contains N. Each of the next N lines specify the details of the N cows in order of seniority (the most senior cow being first). Each line contains ai and ti for one cow. The ti's are positive integers each at most 104, and the ai's are positive integers at most 109.

## 출력

Please print the longest potential waiting time over all the cows.



## 예제 입력 1

```
5
25 3
105 30
20 50
10 17
100 10
```

## 예제 출력 1

```
10
```

## 힌트

In this example, we have 5 cows (numbered 1..5 according to their order in the input). Cow 4 is the first to arrive (at time 10), and before she can finish eating (at time 27) cows 1 and 3 both arrive. Since cow 1 has higher seniority, she gets to eat next, having waited 2 units of time beyond her arrival time. She finishes at time 30, and then cow 3 starts eating, having waited for 10 units of time beyond her starting time. After a gap where no cow eats, cow 5 arrives and then while she is eating cow 2 arrives, eating 5 units of time later. The cow who is delayed the most relative to her arrival time is cow 3.

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2018-2019 Season ](https://www.acmicpc.net/category/442)> [USACO 2018 December Contest ](https://www.acmicpc.net/category/443)> [Silver](https://www.acmicpc.net/category/detail/1987) 2번