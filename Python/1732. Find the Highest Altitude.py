class Solution(object):
    def highestalti(self, gain):

        gain.insert(0,0)
        for i in range(len(gain)-1):
            gain[i+1] = gain[i]+gain[i+1]
        return max(gain)


if __name__ == "__main__":
    #gain = [-5, 1, 5, 0, -7]
    gain = [-4,-3,-2,-1,4,3,2]
    a = Solution()
    k = a.highestalti(gain)
    print(k)
