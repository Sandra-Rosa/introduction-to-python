#print i as long as i is less than 6:
i = 1
while i<6:
    print(i)
    i += 1
#exit the loop when i is 3
i = 1
while i<6:
    print(i)
    if i ==3:
      break
i += 1
#continue to the next iteration if i is 3
i = 0
while i<6:
    i += 1
    if i == 3:
        continue
    print(i)
