def find_pairs(num_string):
  pairs = set()
  lst_num = num_string.split(" ") 
  new_lst = []                    
  for num in lst_num:
    new_lst.append(int(num))


  for i in range(len(new_lst)):
    for j in range(i + 1, len(new_lst)):      
      if new_lst[i] < new_lst[j]:
        pairs.add((new_lst[i], new_lst[j]))
      else:
        pairs.add((new_lst[j], new_lst[i]))  

  return pairs


find_pairs("7 3 99")
# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")
