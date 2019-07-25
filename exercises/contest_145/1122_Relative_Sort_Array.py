class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []

        if len(arr1) == 0:
            return res

        s = {}
        for idx in range(len(arr1)):
            if arr1[idx] not in s:
                s[arr1[idx]] = 0

            s[arr1[idx]] += 1;

        for idx in range(len(arr2)):
            for i in range(s[arr2[idx]]):
                res.append(arr2[idx])
        # print(res)

        keys = sorted(s.keys())

        for key in keys:
            if key not in res:
                for i in range(s[key]):
                    res.append(key)

        # print(res)
        return res


