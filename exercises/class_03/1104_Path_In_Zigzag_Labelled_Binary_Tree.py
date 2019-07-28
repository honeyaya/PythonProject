class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """

        res = []
        depth = 1
        while True:
            left = pow(2, depth - 1)
            right = pow(2, depth) - 1

            if label >= left and label <= right:
                break
            else:
                depth += 1

        res.append(label)
        if depth % 2 == 0:
            sum = int(pow(2, depth - 1)) + int(pow(2, depth)) - 1
            label = sum - label

        while True:
            depth -= 1
            parent = int(label / 2)
            if parent == 0:
                break
            if depth % 2 == 1:
                res.append(parent)
            else:
                sum = int(pow(2, depth - 1)) + int(pow(2, depth)) - 1
                res.append(sum - parent)
            label = parent

        return reversed(res)

solution = Solution()
#print(solution.pathInZigZagTree(14))

#print(solution.pathInZigZagTree(26))

print(solution.pathInZigZagTree(1))

#print(solution.pathInZigZagTree(2))
#print(solution.pathInZigZagTree(3))

