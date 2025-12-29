from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        interval = []

        start = 0
        end = len(intervals)-1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if newInterval[0] == intervals[mid][1]:
                interval.append(intervals[mid][0])
                break
            elif newInterval[0] < intervals[mid][1]:
                if newInterval[1] >= intervals[mid][0]:
                    if newInterval[0] >= intervals[mid][0]:
                        interval.append(intervals[mid][0])
                        break
                    else:                    
                        while mid > 0 and newInterval[0] <= intervals[mid-1][1]:
                            mid-=1
                            if newInterval[0] >= intervals[mid][0]:
                                interval.append(intervals[mid][0])
                                break
                        if newInterval[0] < intervals[mid][0]:
                            interval.append(newInterval[0])
                        break
                else:
                    end = mid - 1
            else:
                start = mid + 1
        if start > end:
            i = 0
            while i < len(intervals):
                if newInterval[0] < intervals[i][0]:
                    break
                i+=1

            newIntervals.extend(intervals[:i])
            newIntervals.append(newInterval)
            newIntervals.extend(intervals[i:])

            return newIntervals
        newIntervals.extend(intervals[:mid])

        start = 0
        end = len(intervals)-1
        mid = len(intervals)-1
        while start <= end:
            mid = (start + end) // 2
            if newInterval[1] == intervals[mid][0]:
                interval.append(intervals[mid][1])
                break
            elif newInterval[1] > intervals[mid][0]:
                if newInterval[0] <= intervals[mid][1]:
                    if newInterval[1] <= intervals[mid][1]:
                        interval.append(intervals[mid][1])
                        break
                    else:                    
                        while mid < len(intervals)-1 and newInterval[1] >= intervals[mid+1][0]:
                            mid+=1
                            if newInterval[1] <= intervals[mid][1]:
                                interval.append(intervals[mid][1])
                                break
                        if newInterval[1] > intervals[mid][1]:
                            interval.append(newInterval[1])
                        break
                else:
                    start = mid + 1
            else:
                end = mid - 1
        newIntervals.append(interval)
        newIntervals.extend(intervals[mid+1:])

        return newIntervals