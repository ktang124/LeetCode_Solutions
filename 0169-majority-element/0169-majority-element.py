class Solution:
    def majorityElement(self,arr):
        def majElement(arr, l,r):
            #base case
            if l == r:
                return arr[l]

            # recurse on left and right halves of this slice.
            #right bitshift is the same as divide by 2
            mid = (l + ((r-l)>>1)) 
            left = majElement(arr,l, mid)
            right = majElement(arr,mid+1, r)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left
            # pick between the two halves by counting them 
            left_count , right_count =  0, 0
            for i in range(l,r+1):
                if arr[i] == left:
                    left_count += 1
                elif arr[i] == right:
                    right_count += 1

            return left if left_count > right_count else right

        return majElement(arr,0, len(arr)-1)