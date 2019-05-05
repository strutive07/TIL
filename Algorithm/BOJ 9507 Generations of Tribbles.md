# BOJ 9507 Generations of Tribbles

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
ll dp[70];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	dp[0] = dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 67; i++) {
		dp[i] = dp[i - 1] + dp[i-2] + dp[i-3] + dp[i-4];
	}
	int _T = 0;
	cin >> _T;
	while (_T--)
	{
		cin >> n;
		cout << dp[n] << "\n";
	}

	return 0;
}


```

---

# Generations of Tribbles   

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 128 MB      | 3378 | 2335 | 2122      | 71.065%   |

## 문제

꿍은 군대에서 진짜 할짓이 없다. 그래서 꿍만의 피보나치를 만들어보려고 한다. 기존의 피보나치는 너무 단순해서 꿍은 좀더 복잡한 피보나치를 만들어보고자 한다. 그래서 다음과 같은 피보나치를 만들었다. 꿍만의 피보나치 함수가 koong(n)이라고 할 때,

```
n < 2 :                         1
n = 2 :                         2
n = 3 :                         4
n > 3 : koong(n − 1) + koong(n − 2) + koong(n − 3) + koong(n − 4)
```

이다.

여러분도 꿍 피보나치를 구해보아라.

## 입력

입력의 첫 번째 줄을 테스트 케이스의 개수 t (0 < t < 69)가 주어진다. 다음 t줄에는 몇 번째 피보나치를 구해야하는지를 나타내는 n(0 ≤ n ≤ 67)이 주어진다.

## 출력

각 테스트 케이스에 대해, 각 줄에 꿍 피보나치값을 출력하라.



## 예제 입력 1

```
8
0
1
2
3
4
5
30
67
```

## 예제 출력 1

```
1
1
2
4
8
15
201061985
7057305768232953720
```



## 출처

[ACM-ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [North America ](https://www.acmicpc.net/category/8)> [Pacific Northwest Regional ](https://www.acmicpc.net/category/33)> [2013 Pacific Northwest Region Programming Contest](https://www.acmicpc.net/category/detail/1173) G번

- 문제의 오타를 찾은 사람: [mwy3055](https://www.acmicpc.net/user/mwy3055)
- 문제를 번역한 사람: [seok9311](https://www.acmicpc.net/user/seok9311)

## 링크

- [ACM-ICPC Live Archive](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4529)

## 알고리즘 분류

- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)