class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        min_bei = a*b*c
        self.ni = n
        self.ai = a
        self.bi = b
        self.ci = c
        self.ab = self.find_minComBeishu(a, b)
        self.ac = self.find_minComBeishu(a, c)
        self.bc = self.find_minComBeishu(b, c)
        self.abc = self.find_minComBeishu(self.ab, c)
        self.maxin = 2*10**9
        ans = self.dichotima(1, self.maxin)

        return ans

    def dichotima(self, left: int, right: int) -> int:
       # print(left, right)
        if left > right:
            return left
        mid = (right + left) // 2
        n_cur = mid // self.ai + mid // self.bi + mid // self.ci - \
            mid // self.ab - mid//self.ac - mid // self.bc + mid // self.abc
        print(mid, n_cur)
        if n_cur < self.ni:
            return self.dichotima(mid+1, right)
        else:
            if (n_cur == self.ni) & ((mid % self.ai == 0) | (mid % self.bi == 0) | (mid % self.ci == 0)):
                return mid
            else:
                return self.dichotima(left, mid)

    def find_minComBeishu(self, x: int, y: int) -> int:
        ai = min(x, y)
        bi = max(x, y)
        ans = bi
        self.maxin = 2*10**9
        while ans % ai != 0:
            ans += bi
            if ans > self.maxin:
                return self.maxin+1
        return ans


kk = Solution()
ans = kk.find_minComBeishu(15, 6)
print(ans)

#ans = kk.nthUglyNumber(1000000000, 2, 217983653, 336916467)
ans = kk.find_minComBeishu(217983653, 336916467)
print(ans)


''' def findii(self, left: int, right: int) -> int:
        mid = (left + right)//2
        num_ii =
'''
