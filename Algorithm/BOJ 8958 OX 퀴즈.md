# BOJ 8958 OX 퀴즈

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

using namespace std;
#define INF 1234567890

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int _T = 0;
	cin >> _T;
	while (_T--)
	{
		int cnt = 0, ans = 0;
		string s;
		cin >> s;
		for (auto c : s) {
			if (c == 'O') cnt++;
			else cnt = 0;
			ans += cnt;
		}
		cout << ans << "\n";
	}

	return 0;
}


```



---

# OX퀴즈

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ----- | ----- | --------- | --------- |
| 1 초      | 128 MB      | 23411 | 12647 | 11210     | 56.545%   |

## 문제

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

## 출력

각 테스트 케이스마다 점수를 출력한다.

## 예제 입력 1

```
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
```

## 예제 출력 1

```
10
9
7
55
30
```



## 출처

[ACM-ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [Asia ](https://www.acmicpc.net/category/42)> [Korea ](https://www.acmicpc.net/category/211)> [Asia Regional - Seoul 2005](https://www.acmicpc.net/category/detail/1067) A번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [jh82582](https://www.acmicpc.net/user/jh82582)

