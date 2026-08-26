class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(len(temp)):
                arr[low + i] = temp[i]


        def mergeSort(low , high):
            if low >= high:
                return
            mid = low + (high - low) // 2
            mergeSort(low , mid)
            mergeSort(mid+1 , high)
            merge(nums , low , mid ,high)
        mergeSort(0,len(nums)-1)
        return nums
