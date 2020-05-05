'''
nums:       current permutation
index:      the next index to add digit
visited:    whether a number has been visited
sum:        sum of last 3 digits
'''
def getPermutations(nums, index, visited, sum):
    if index == 6:          #
        if sum == 6:        # sum of last 3 digit is 6
            ouput = [str(n) for n in nums]
            print("".join(ouput))
        return
    for i in range(6):      # try all nums between 0 and 5
        if visited[i]:      # is digit already in result continue
            continue
        if index == 0 and i == 0:   # 0 不能在最高位
            continue
        if len(nums) > 0:
            if (nums[-1] == 3 and i == 4) or \
                    (nums[-1] == 4 and i == 3):    # 3和4不能挨着
                continue
        if index >= 3:      # 最后三位相加
            sum += i
        if sum > 6:         # 如果最后三提前结束
            break
        visited[i] = True   # 设定已经用过这个数字
        nums.append(i)      # 把当前数字加入列表
        getPermutations(nums, index + 1, visited, sum) #递归调用
        nums.pop()          # 把当前数字列表
        visited[i] = False  # 设定位没有用过这个数字
        if index >= 3:      # 最后三位需要减去
            sum -= i


if __name__ == "__main__":
    visited = [False] * 6
    getPermutations([], 0, visited, 0)
