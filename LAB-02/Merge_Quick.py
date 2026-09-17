def compare_merge_quick_tasks(tasks):
    output=["Task Prioritization Report","Merge Sort Result"]
    merge_comparisons=0

    def merge_sort(left,right):
        nonlocal merge_comparisons
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            merge_comparisons+=1
            if left[i][1]>right[j][1] or (left[i][1]==right[j][1] and left[i][0]<right[j][0]):
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result+=left[i:]
        result+=right[j:]
        return result

    def merge(arr):
        if len(arr)<=1:
            return arr
        else:
            l=len(arr)//2
            left=merge(arr[:l])
            right=merge(arr[l:])
            return merge_sort(left,right)

    merge_tasks=merge(tasks[:])

    for task_id,priority in merge_tasks:
        output.append(f"{task_id} {priority}")

    output.append(f"Merge Comparisons: {merge_comparisons}")

    quick_comparisons=0

    def quick_sort(arr,low,high):
        if low<high:
            pi=partition(arr,low,high)
            quick_sort(arr,low,pi-1)
            quick_sort(arr,pi+1,high)

    def partition(arr,low,high):
        nonlocal quick_comparisons
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            quick_comparisons+=1
            if arr[j][1]>pivot[1] or (arr[j][1]==pivot[1] and arr[j][0]<pivot[0]):
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1

    quick_tasks=tasks[:]
    quick_sort(quick_tasks,0,len(quick_tasks)-1)

    output.append("Quick Sort Result")

    for task_id,priority in quick_tasks:
        output.append(f"{task_id} {priority}")

    output.append(f"Quick Comparisons: {quick_comparisons}")

    if merge_comparisons<quick_comparisons:
        output.append("Better Algorithm: Merge Sort")
    elif quick_comparisons<merge_comparisons:
        output.append("Better Algorithm: Quick Sort")
    else:
        output.append("Better Algorithm: Both Equal")

    return output