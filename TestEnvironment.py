def task(n):
  ans = ""
  if n%2 != 0:
      ans= "Weird"
  elif n in range (2,5):
      ans= "Not Weird"
  elif n in range (6,20):
      ans= "Weird"
  elif n > 20:
      ans= "Not Weird"
  return ans
#print(task(24))
