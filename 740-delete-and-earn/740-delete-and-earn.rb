def delete_and_earn(nums)
  return nums[0] if nums.length == 1

   arr = Array.new(nums.max+1){0}
   nums.each do |num|
       arr[num]+=num
   end
   
   max1=0
   max2=0
   arr.each do |arr|
        max1, max2 = [max2, max1].max, arr+max1
   end
   [max2, max1].max
end