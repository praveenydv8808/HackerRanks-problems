import array
def sort(arr):
    while True:
        corrected=False
        for i in range(0,len(arr)-1):
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                corrected=True
            if not corrected:
                return arr
            
print(sort([1,6,9,4,3,5]))
