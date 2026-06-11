def next_greater(arr);
    n = len(arr)
    
    for i in range(n);
        found = False
        
      for j in range(i + 1, n);
            if arr[j] > arr[i];
                print(arr[j], end=" ")
                found = True
                break
        
        if not found:
            print(-1, end=" ")


