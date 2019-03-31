# Atcoder apc001 C - Vacant Seat

<https://atcoder.jp/contests/apc001/tasks/apc001_c>

이진 탐색 문제이다.

interactive task 라는 신기한 atcoder 의 채점 방식을 처음 겪어봐서 조금 생소했던 문제다.



원에 홀수 사람들이 둘러 앉아 있고, i 와 i+1 은 인접한 자리이며, 1 과 N-1 은 인접한 자리 이다.

사람은 남성과 여성으로 구분되어진다.

하나의 제약이 있는데, 인접한 자리는 같은 성이 앉을 수 없다 는 것이다. 무조건 남성 여성 남성 여성 --- 으로 앉아야 한다.



홀수 자리이면서 위와 같은 조건이면 무조건 하나 이상 빈 자리가 존재해야 위 제약을 만족시킨다.



따라서 이 `빈자리` 의 위치를 찾아야 한다.



일단 무조건 20회 query 안에 찾아야 하고, N 이 3≤N≤99999 인 홀수 이므로, Log 시간 안에 탐색 해야한다.

따라서 parametric search 를 진행 하면 된다.



맨 처음에는 가장 첫자리인 0번 자리(첫 left)를 query 한다. right 는 N 으로 둔다.

그 후 mid 지점(left + right) /2 에 query 를 한다.

여기서 2가지 조건이 나온다.

1. mid - left 자리 차이가 홀수/짝수
2. query(left) 와 query(mid) 가 같은가?

만약 짝수차이 이면서 같으면, `여 남 여` 또는 `남 여 남` 순서이므로, 빈 자리는 mid 와 right 사이에 존재할것이다.

만약 짝수차이 이면서 다르면, `여 빈자리 남 ` 또는 `남 빈자리 여` 순서이므로, 빈 자리는 무조건 left 와 mid 사이에 존재할것이다.

만약 홀수차이 이면서 같으면, `여 남 빈자리 여` 또는 `남 여 빈자리 남` 순서이므로, 빈 자리는 무조건 left 와 mid 사이에 존재할것이다.

만약 홀수차이 이면서 다르면, `여 남 여 남` 또는 `남 여 남 여` 순서이므로, 빈 자리는 mid 와 right 사이에 존재할것이다.



이 조건을 XOR 로 잘 조합해서 parametric search 의 check 함수로 넣어주면 된다.



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

	int N;
	cin >> N;
	vector<string> vc(N);
	cout << 0 << endl;
	cin >> vc[0];
	int left = 0, right = N;
	int mid = 0;
	while (vc[mid] != "Vacant")
	{
		mid = (left + right) / 2;
		cout << mid << endl;
		cin >> vc[mid];
		if (((mid - left) & 1 ) ^ (vc[left] == vc[mid])) 
			left = mid;
		else 
			right = mid;
	}



	return 0;
}


```





