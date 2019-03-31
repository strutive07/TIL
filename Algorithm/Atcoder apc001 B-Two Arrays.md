# Atcoder apc001 B-Two Arrays

<https://atcoder.jp/contests/apc001/tasks/apc001_b>



2 가지 길이가 같은 정수형 배열이 나온다.



우리가 할 수 있는 operation 은 단 한가지 이다.

- A[i] 에 2를 더하면서 B[j] 에 1을 더하기 (i 와 j 는 맘대로 정할 수 있음)

위 operation 을 0회 이상 수행하면서 A array 와 B array 를 같게 만들 수 있는가? 가 문제이다.



일단 조건을 생각해보면, A 와 B 가 무조건 같이 증가 하고, A 의 증가폭이 B 의 2배 이므로, 배열의 전체 합이 A > B 이면 무조건 같은 배열이 될 수 없다.



첫 번째 조건에서 넘어왔다는것은, B 배열의 합이 무조건 크다는것.

- A[i] > B[j] 일때는 A[i] - B[j] 만큼 B 를 늘려야하고
- B[j] > A[i] 일때는 ⌈ (b[i] - a[i])/2 ⌉  만큼 operation 이 필요합니다.



B 배열의 합이 무조건 크므로, 2 번째 조건을 만족하다보면 ⌈⌉ 연산 때문에 무조건 1 조건을 동시에 만족하게 된다.

따라서 2 번째 조건을 몇번 수행해야 하는지 카운트를 해보자.



최종 operation 합이 sum_b - sum_a 보다 작으면 같은 배열을 만들 수 있고

아니면 같은 배열을 만들 수 없다.

합의 차는, 결국 가능한 최대 operation 의 횟수 이기 때문이다.(a 2 증가, b 1증가가 1 operation 이니, 1 operation 당 1 diff 가 발생하므로!)



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
#define LIMIT 10005

int a[LIMIT], b[LIMIT];
ll sum_a, sum_b;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		sum_a += a[i];
	}
	for (int i = 1; i <= n; i++) {
		cin >> b[i];
		sum_b += b[i];
	}
	if (sum_a > sum_b) {
		cout << "No";
		return 0;
	}
	sum_b -= sum_a;
	for (int i = 1; i <= n; i++) {
		sum_b -= max((b[i] - a[i] + 1) / 2, 0);
	}
	if (sum_b >= 0)
		cout << "Yes";
	else
		cout << "No";

	return 0;
}


```

