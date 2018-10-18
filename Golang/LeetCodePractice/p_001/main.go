package main

import (
	"fmt"

	"./algorithms"
)

func main() {
	r1 := algorithms.TwoSum1([]int{2, 7, 11, 15}, 9)
	fmt.Println(r1)
	r2 := algorithms.TwoSum2([]int{2, 7, 11, 15}, 9)
	fmt.Println(r2)
}
