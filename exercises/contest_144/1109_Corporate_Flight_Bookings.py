class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        ans = []

        change = [0 for idx in range(0, n + 2)]
        print(change)

        for booking in bookings:
            change[booking[0]] += booking[2]
            change[booking[1] + 1] -= booking[2]

        res = 0
        for idx in range(1, n + 1):
            res += change[idx]
            ans.append(res)

        return ans[0:n]
