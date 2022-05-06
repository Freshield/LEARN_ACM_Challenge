/**
 @Author: Freshield
 @Contact: yangyufresh@163.com
 @File: a1_bisearch.py
 @Time: 2022-04-08 11:09
 @Last_update: 2022-04-08 11:09
 @Desc: None
 @==============================================@
 @      _____             _   _     _   _       @
 @     |   __|___ ___ ___| |_|_|___| |_| |      @
 @     |   __|  _| -_|_ -|   | | -_| | . |      @
 @     |__|  |_| |___|___|_|_|_|___|_|___|      @
 @                                    Freshield @
 @==============================================@
 */
var search = function (nums, target) {
    var left = 0
    var right = nums.length
    // 这里是左闭右闭的区间
    while (left <= right) {
        // 这里是左右范围的中间
        const mid = Math.floor((right - left) / 2) + left
        const mid_value = nums[mid]
        // 如果相等
        if (mid_value === target) {
            return mid
        } else if (mid_value < target) {
            // 如果小于目标值，则缩小为右半边
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return -1
}


let res = search([-1,0,3,5,9,12], 9)
console.log(res)