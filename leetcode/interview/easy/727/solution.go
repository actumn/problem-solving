package main

import "fmt"

func main() {
	nums := []int{1, 1, 2}
	fmt.Println(removeDuplicates(nums))
	fmt.Println(nums)
}

func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    
    a := []int{nums[0]}
    curr := nums[0]
    
    for i := 1; i < len(nums); i++ {
        number := nums[i]
        if number != curr {
            a = append(a, number)
            curr = number
        }
    }
    
    nums = nums[:0]
    nums = append(nums, a...)
    
    return len(a)
}