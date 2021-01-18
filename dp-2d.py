def solve(str1,str2,idx1,idx2):
    if idx1>=len(str1) or idx2>=len(str2):
        return 0
    if (str1[idx1]==str2[idx2]):
        return 1+ solve(str1,str2,idx1+1,idx2+1)
    else:
        return max(solve(str1,str2,idx1+1,idx2),solve(str1,str2,idx1,idx2+1))

if __name__ == "__main__":
    print(solve("abced","appseajauuuagfaoayehbghgale",0,0))
dp = [[None for _ in range(100)] for _ in range(100)]
def solve1(str1,str2,idx1,idx2):
    if idx1>=len(str1) or idx2>=len(str2):
        return 0
    if dp[idx1][idx2]!=None:
        return dp[idx1][idx2]
    ans = 0
    if (str1[idx1]==str2[idx2]):
        ans = 1 + solve(str1,str2,idx1+1,idx2+1)
    else:
        ans = max(solve(str1,str2,idx1+1,idx2),solve(str1,str2,idx1,idx2+1))
    dp[idx1][idx2]=ans
    return ans
if __name__ == "__main__":
    print(solve1("abced","appseajauuuagfaoayehbghgale",0,0))


