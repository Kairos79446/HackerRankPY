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

if __name__ == "__main__":
    print("Testing the task function:")
    test_numbers = [3, 4, 10, 24]
    for num in test_numbers:
        result = task(num)
        print(f"task({num}) = {result}")
