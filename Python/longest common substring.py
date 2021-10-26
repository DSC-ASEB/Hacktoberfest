def longest_common_substring(a,b):
    #we have to build a 2D matrix to make use of DP approach
    # so that I require a 2D matrix of (n+1)(m+1) size
    dp = []
    maxi = 0
    for i in range(len(b)+1):
        dp.append([0]*(len(a)+1))
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if b[i-1] == a[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                if maxi<dp[i][j]:
                    idx = [i,j]
                maxi = max(maxi,dp[i][j])

            else:
                dp[i][j] = 0
    sub_string = ""
    i = idx[0]
    j = idx[1]
    while dp[i][j]>0:
        sub_string+=a[j-1]
        i-=1
        j-=1
    return maxi, sub_string

if __name__ == "__main__":
    a = input("Enter the string1: ")
    b = input("Enter the string2: ")
    lcs_length, lcs = longest_common_substring(a,b)
    print("Longest Matched substring length is ",lcs_length)
    print("Longest Matched substring is")
    print('"',lcs[::-1],'"')
