def binary_search(mylist,low,high,elem):
   if high >= low:
      mid = (high + low) // 2
      if mylist[mid] == elem:
         return mid
      elif mylist[mid] > elem:
         return binary_search(mylist, low, mid - 1, elem)
      else:
         return binary_search(mylist, mid + 1, high, elem)
   else:
      return -1
     
mylist = list(map(int,input().split()))
elem_to_search=int(input())
print(*mylist)
my_result = binary_search(mylist,0,len(mylist)-1,elem_to_search)
if my_result != -1:
   print("Element found at index ", str(my_result))
else:
   print("Element not found!")
