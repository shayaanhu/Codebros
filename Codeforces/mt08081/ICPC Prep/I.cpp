/* ---------------- Competitive Programming Template for ICPC and Other Competitions ---------------- */

#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <string>
#include <bitset>
using namespace std;

/* ------------------- FAST I/O ------------------- */
#define fast_io ios::sync_with_stdio(false);cin.tie(nullptr)

/* ------------------- TYPE ALIASES ------------------- */
using ll = long long;
using lld = long double;
using vll = vector<ll>;
using vlld = vector<lld>;
using vb = vector<bool>;
using vvll = vector<vector<ll>>;
using vvlld = vector<vector<lld>>;
using pll = pair<ll, ll>;
using plld = pair<lld, lld>;

/* ------------------- MACROS ------------------- */
#define rep(i,a,b) for(ll i=(a);i<(b);++i)
#define per(i,a,b) for(ll i=(a);i>=(b);--i)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define sz(x) ((ll)(x).size())
#define nl "\n"

/* ------------------- CONSTANTS ------------------- */
const ll MOD = 1e9 + 7;
const ll INF = LLONG_MAX;

/* --------------- GCD and LCM --------------- */
inline ll gcd(ll a,ll b){ return b ? gcd(b,a%b) : a; }
inline ll lcm(ll a,ll b){ return (a/gcd(a,b))*b; }

/* --------------- FASTER INPUT/OUTPUT --------------- */
namespace __input {
    template<class T> void re(T &x){ cin >> x; }
    void re(lld &x){ string t; cin >> t; x=stold(t); }
    template<class T1,class T2> void re(pair<T1,T2> &p){ re(p.first,p.second); }
    template<class T> void re(vector<T> &a){ for(auto &x:a) re(x); }
    template<class T, size_t SZ> void re(array<T,SZ> &a){ for(auto &x:a) re(x); }
    template<class Arg,class...Args> void re(Arg &f,Args &...r){ re(f); re(r...); }
}
using namespace __input;

namespace __output {
    template<class T> void pr(const T &x){ cout<<x; }
    template<class T1,class T2> void pr(const pair<T1,T2> &p){ pr(p.first);pr(" ");pr(p.second); }
    template<class Arg,class...Args> void pr(const Arg &f,const Args &...r){ pr(f);pr(" ");pr(r...); }
    template<class T> void pr(const vector<T> &x){ for(const auto &a:x){ pr(a); pr(" "); } }
    void ps(){ pr("\n"); }
    template<class Arg> void ps(const Arg &f){ pr(f); ps(); }
    template<class Arg,class...Args> void ps(const Arg &f,const Args &...r){ pr(f); pr(" "); ps(r...); }
}
using namespace __output;

/* --------------- CONDITIONAL DEBUG PRIMITIVES --------------- */
#if defined(LOCAL) && LOCAL == SALMAN
    // SALMAN build: enable debug printing
    #define debug_pr(...) pr(__VA_ARGS__)   // print without newline
    #define debug_ps(...) ps(__VA_ARGS__)   // print with newline
#else
    // non-SALMAN build: disable debug printing
    #define debug_pr(...)      /* no-op */
    #define debug_ps(...)      /* no-op */
#endif

/* --------------- RANDOM HELPER --------------- */
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
inline ll random_in_range(ll l,ll r){
    uniform_int_distribution<ll> dist(l,r);
    return dist(rng);
}

/* --------------- SOLVE --------------- */
ll MXE = 20;
vvll adj;
vvll up;
vll depth;

inline void init_binary_lifting(ll n) {
    // MXE = log2(n) + 10;
    adj.assign(n, {});
    depth.assign(n, 0);
    up.assign(n, vll(MXE, -1));
}

inline void dfs_binary(ll curr, ll par) {
    up[curr][0] = par;
    for (ll j = 1; j < MXE; ++j) {
        if (up[curr][j-1] < 0) up[curr][j] = -2;
        else up[curr][j] = up[ up[curr][j-1] ][j-1];
    }
    for (ll to : adj[curr]) {
        if (to == par) continue;
        depth[to] = depth[curr] + 1;
        dfs_binary(to, curr);
    }
}

inline ll lift2(ll v, ll k) {
    for (ll j = 0; j < MXE && v >= 0; ++j) {
        if (k & (1LL << j)) v = up[v][j];
    }
    return v;
}

inline ll lca_binary(ll a, ll b) {
    if (depth[a] < depth[b]) swap(a, b);
    a = lift2(a, depth[a] - depth[b]);
    if (a == b) return a;
    for (ll j = MXE-1; j >= 0; --j) {
        if (up[a][j] != up[b][j]) {
            a = up[a][j];
            b = up[b][j];
        }
    }
    return up[a][0];
}

inline ll dist_binary(ll a, ll b) {
    ll c = lca_binary(a, b);
    return depth[a] + depth[b] - 2*depth[c];
}

void solve(){
    ll N, K, R; re(N, K, R); --R;
    init_binary_lifting(N);
    rep(i, 0, N-1) {
        ll u, v; re(u, v); --u, --v; adj[u].eb(v), adj[v].eb(u);
    }

    dfs_binary(R, -2);

    rep(i, 0, K) {
        ll u, k; re(u, k); --u;
        ps(lift2(u, k) + 1ll);
    }
}

/* --------------- MAIN --------------- */
int main(){
    fast_io;

    #if defined(LOCAL) && LOCAL == SALMAN
    // Record start time
    auto start = std::chrono::high_resolution_clock::now();
    #endif


    // // Precomputations Needed for Your Code
    // precompute_factorials();   // ✅ Required for nCr(n, r)
    // sieve(MAXN);               // ✅ Required for prime-related functions
    // compute_totient();         // ✅ Required for φ(n) calculations
    // compute_mobius();          // ✅ Required for Möbius function calculations

    cout << setprecision(12) << fixed;

    ll T=1;
    cin >> T;
    while(T--) solve();


    #if defined(LOCAL) && LOCAL == SALMAN
    // Record end time
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate duration
    std::chrono::duration<double> duration = end - start;

    // Output duration in seconds
    std::cout << "Execution time: " << duration.count() << " seconds" << std::endl;
    #endif

    return 0;
}
