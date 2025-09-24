def intervals_overlap(a,b):
  a_start, a_end = a
  b_start, b_end = b

  return not((a_end < b_start) or (b_end < a_start))
