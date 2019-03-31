# Atcoder codefestival 2016 fianl B - Exactly N points

<https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b>



N 가지 문제가 있는데, 각 문제의 난이도와 Point는 각각 문제 index(1~N) 과 같다

가능한 쉬운 문제들로 정확히 N point 를 얻어야 한다.



일단 N점의 범위를 알아야 한다. 1번 문제부터 하나씩 점수를 더하면서 N point 가 넘는 지점을 찾는다.

이렇게 되면, 최소한 해당 지점이 포함되지 않는다면 N 을 만족하지 못하므로, 해당 지점이 정답 셋에 들어가기 위한 가장 큰 점수의 지점, 즉 Limit 이 된다.



이미 최대 수 가 limit 으로 결정 되었으니, 그 다음 숫자는 목표 점수를 채울 수 있는 숫자 집합 아무거나 찾으면 된다.



이렇게 찾았을때 무조건 1이 `가능한 숫자 집합` 에 포함 되어있으므로 그리디하게 하나씩 숫자를 뽑아주면 끝이다.





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

	int n;
	cin >> n;
	int sum = 0;
	int limit = 0;
	vector<int> res;
	for (int i = 1; i <= n; i++) {
		sum += i;
		if (sum >= n) {
			limit = i;
			break;
		}
	}
	for (int i = limit; i >= 1; i--) {
		if (n < i)
			continue;
			
		res.push_back(i);
		n -= i;
		
	}
	for (int i = res.size() - 1; i >= 0; i--) {
		cout << res[i] << "\n";
	}

	return 0;
}


```



