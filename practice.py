class Solution:
    def transpose(self, matrix):
        m=[[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m[j][i]=matrix[i][j]
        return m
s=Solution()