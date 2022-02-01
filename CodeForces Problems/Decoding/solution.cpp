#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h> 
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
#define ln "\n"
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define MAXN 10005
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
#define PRECISION(x) cout << fixed << setprecision(x); 
 
int main()
{
	fast_cin();
	int n;
	cin >> n;
	string s;
	cin >> s;
	deque <char> newS;
	for (int i = 0; i < s.size(); i++)
	{
		if (i % 2 == 0)
			newS.push_back(s[i]);
		else
			newS.push_front(s[i]);
	}

	if (s.size() % 2 == 1)
		for (auto &ch : newS)
			cout << ch;
	else
		for (int i = newS.size() - 1; i >= 0 ; i--)
			cout << newS[i];
	

	return 0;
}