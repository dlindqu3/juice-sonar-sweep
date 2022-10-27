def count_over_avgs(arr): 
  sums = []
  for idx in range(0, len(arr)): 
    if idx == 0: 
      sums.append(arr[idx])
    elif idx != 0: 
      new_sum = sums[-1] + arr[idx]
      sums.append(new_sum)
  avgs = []
  for idx in range(0, len(arr)): 
    if idx == 0: 
      avgs.append(arr[idx])
    else: 
      new_avg = sums[idx] / (idx + 1)
      avgs.append(new_avg)
  count = 0
  for idx in range(1, len(arr)): 
    if arr[idx] > avgs[idx -1]: 
      count += 1
  return count 
      

print(count_over_avgs([1, 3, 5]))
print(count_over_avgs([1, 0, -1, 20, -30, 0, 5]))