# BOJ 6166 Meteor Shower

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
int n, m;
vector<vector<int>> boomtime(505, vector<int>(505, INF));
vector<vector<int>> bfstime(505, vector<int>(505, INF));


queue<pair<int, int>> que;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};


void do_bfs(int x, int y, int cur_time) {
	if (
		x >= 0 &&
		y >= 0 &&
		cur_time < boomtime[x][y] &&
		cur_time < bfstime[x][y]
		) {
		if (boomtime[x][y] == INF) {
			cout << cur_time;
			exit(0);
		}
		bfstime[x][y] = cur_time;
		que.push({ x,y });
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int x, y, time;
		cin >> x >> y >> time;
		boomtime[x][y] = min(boomtime[x][y], time);
		for (int i = 0; i < 4; i++) {
			int cx = x + dx[i];
			int cy = y + dy[i];
			if (cx >= 0 && cy >= 0) {
				boomtime[cx][cy] = min(boomtime[cx][cy], time);
			}
				
		}
	}
	do_bfs(0, 0, 0);
	while (!que.empty()) {
		int x = que.front().first;
		int y = que.front().second;
		que.pop();
		for (int i = 0; i < 4; i++) {
			int cx = x + dx[i];
			int cy = y + dy[i];
			do_bfs(cx,cy,bfstime[x][y]+1);
		}
	}
	cout << -1;
	return 0;
}


```



# Meteor Shower

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 1 초      | 128 MB      | 44   | 11   | 11        | 26.190%   |

## 문제

Bessie hears that an extraordinary meteor shower is coming; reports say that these meteors will crash into earth and destroy anything they hit. Anxious for her safety, she vows to find her way to a safe location (one that is never destroyed by a meteor) . She is currently grazing at the origin in the coordinate plane and wants to move to a new, safer location while avoiding being destroyed by meteors along her way.

The reports say that M meteors (1 <= M <= 50,000) will strike, with meteor i will striking point (X_i, Y_i) (0 <= X_i <= 300; 0 <= Y_i <= 300) at time T_i (0 <= T_i <= 1,000). Each meteor destroys the point that it strikes and also the four rectilinearly adjacent lattice points.

Bessie leaves the origin at time 0 and can travel in the first quadrant and parallel to the axes at the rate of one distance unit per second to any of the (often 4) adjacent rectilinear points that are not yet destroyed by a meteor.  She cannot be located on a point at any time greater than or equal to the time it is destroyed).

Determine the minimum time it takes Bessie to get to a safe place.

## 입력

- Line 1: A single integer: M
- Lines 2..M+1: Line i+1 contains three space-separated integers: X_i, Y_i, and T_i

 

## 출력

- Line 1: The minimum time it takes Bessie to get to a safe place or -1 if it is impossible.

 



## 예제 입력 1

```
4
0 0 2
2 1 2
1 1 2
0 3 5
```

## 예제 출력 1

```
5
```

## 힌트

There are four meteors, which strike points (0, 0); (2, 1); (1, 1); and (0, 3) at times 2, 2, 2, and 5, respectively.

```
    t = 0                t = 2              t = 5
5|. . . . . . .     5|. . . . . . .     5|. . . . . . .    
4|. . . . . . .     4|. . . . . . .     4|# . . . . . .   * = meteor impact
3|. . . . . . .     3|. . . . . . .     3|* # . . . . .  
2|. . . . . . .     2|. # # . . . .     2|# # # . . . .   # = destroyed pasture
1|. . . . . . .     1|# * * # . . .     1|# # # # . . .   
0|B . . . . . .     0|* # # . . . .     0|# # # . . . .   
  --------------      --------------      -------------- 
  0 1 2 3 4 5 6       0 1 2 3 4 5 6       0 1 2 3 4 5 6 
```


Examining the plot above at t=5, the closest safe point is (3, 0) -- but Bessie's path to that point is too quickly blocked off by the second meteor. The next closest point is (4,0) -- also blocked too soon.  Next closest after that are lattice points on the (0,5)-(5,0) diagonal. Of those, any one of (0,5), (1,4), and (2,3) is reachable in 5 timeunits.

```
       5|. . . . . . .   
       4|. . . . . . .   
       3|3 4 5 . . . .    Bessie's locations over time
       2|2 . . . . . .    for one solution
       1|1 . . . . . .   
       0|0 . . . . . .   
         -------------- 
         0 1 2 3 4 5 6  
```

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2007-2008 Season ](https://www.acmicpc.net/category/146)> [USACO February 2008 Contest ](https://www.acmicpc.net/category/152)> [Silver](https://www.acmicpc.net/category/detail/685) 2번

## 링크

- [PKU Judge Online](http://poj.org/problem?id=3669)