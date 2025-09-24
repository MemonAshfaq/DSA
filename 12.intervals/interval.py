def intervals_overlap(a, b):
    """
    Return True if two closed intervals [a_start, a_end] and [b_start, b_end]
    overlap or touch.
    """
    a_start, a_end = a
    b_start, b_end = b
    return a_start <= b_end and b_start <= a_end

print(intervals_overlap([1, 5], [4, 8]))   # True (overlap 4–5)
print(intervals_overlap([1, 2], [3, 4]))   # False
print(intervals_overlap([1, 4], [4, 6]))   # True (touching counts)

def insert_interval(intervals, interval):
  start,end = interval
  i=0
  new_list = []

  #Add all intervals that end before the new one starts
  while (i < len(intervals) and intervals[i][1] < start):
    new_list.append(intervals[i])
    i+=1

  #Merge all intervals that overlap with [start, end]
  #Look at all meetings that start before this meeting ends
  while (i < len(intervals) and intervals[i][0] <= end):
    start = min(start,intervals[i][0])
    end = max(end,intervals[i][1])
    i+=1

  #Append the merged interval
  new_list.append([start,end])

  #Add everything that comes after
  new_list.extend(intervals[i:])

print(insert_interval([[1,3],[6,9]], [2,5]))
# [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]))
# [[1,2],[3,10],[12,16]]

def merge_intervals(intervals):
  intervals.sort()
  merged = [intervals[0]]
  
  for start, end in intervals[1:]:
    if merged[-1][1] >= start:
      merged[-1][1] = max(merged[-1][1],end)
    else:
      merged.append([start,end])
  return merged
  
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
