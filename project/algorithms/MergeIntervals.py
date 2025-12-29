from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newIntervals = []
        intervals.sort()

        i = 0
        while i < len(intervals):
            t = intervals[i].copy()

            j = i+1
            while j < len(intervals) and t[1] >= intervals[j][0]:
                if t[1] < intervals[j][1]:
                    t[1] = intervals[j][1]
                j+=1

            newIntervals.append(t)
            i = j

        return newIntervals