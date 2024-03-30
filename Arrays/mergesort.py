#merge sort is better in term of time compelxity compare to bubble, insertion and selection sort.


# This is Divide and Merge type algo.
#first algo divides the array hypothetically left-part and right part.
# keep dividing untill you left with single number. stop there 
# now merge it in sorted manner. 
# this problem contains the subproblem of merging of two sorted arrays. using two pointer technique.

# some careful obeservations when merging two sorted lists
# we can specifically can not tell PRIOR that how much iterations will require when merging the lists so while loop will be the choice of iteration
# we are also sure that at when we done merging lists whether they are of similar lengths or different any one list 
# will exaust first FOR SURE. Now the problem here is to find which one ?
# one you found that then simply append the remaining list to the merged array if elements present in second list.
  
def mergeTwoSortedArrays(arr1,arr2):
    #taking care of the some of the edge cases
    if len(arr1)==0 and len(arr2) ==0:
        print("Both lists are empty Merging not possible")
        return []
    if len(arr1)==0:
        return arr2
    if len(arr2)==0:
        return arr1
    #at this point we are sure that we have alteast one element in the BOTH of the lists
    new_arr = []
    left_arr_pointer = 0
    right_arr_pointer=0
    
    while True:
        #usual comparison to decide which one to put first
        if(arr1[left_arr_pointer] <= arr2[right_arr_pointer]):
            new_arr.append(arr1[left_arr_pointer])
            left_arr_pointer+=1
        else:
            new_arr.append(arr2[right_arr_pointer])
            right_arr_pointer+=1
        
        #finding out which list got exhausted IF ANY
        if left_arr_pointer == len(arr1): #arr1 is exhausted
            new_arr.extend(arr2[right_arr_pointer:])
            break
        elif right_arr_pointer == len(arr2):
            new_arr.extend(arr1[left_arr_pointer:])
            break
        
    return new_arr
        

def mergeSort(given_arr):
    if(len(given_arr)==1):
        return given_arr
    #first part recursively split the array until one element left.
    left=0
    right=len(given_arr)-1
    mid = (left+right)//2
    # also we need to make a new object of list as python passes the reference of the list in subsequent 
    # call by default which we do not want because it actually modifies the existing data structure here list
    new_arr = list(given_arr[left:mid+1]) #here we are considering from left to mid including
    left_sorted_arr=mergeSort(new_arr)
    new_arr2 = list(given_arr[mid+1:right+1]) #here mid excluding to right including
    right_sorted_arr=mergeSort(new_arr2)
    
    # merge the two sorted arrays and return it to the former recursive calls if present or last call as a final result
    return mergeTwoSortedArrays(left_sorted_arr,right_sorted_arr)
 
# print(mergeTwoSortedArrays([-1,1,1],[1,5]))

# print(mergeSort([5,1,1,2,0,0]))

