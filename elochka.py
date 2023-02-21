class Solution:
    def tree(self,n,c="*"):
        for i in range(n):
            print(
                (c*(1+2*i))
                .rjust(n+i)
                )


pine = Solution()
pine.tree(19)