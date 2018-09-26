package main

import (
	"fmt"
)

type intslice []int

// a slice of int

func main() {
	// a slice of int 0-10
	slice := intslice{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	for _, num := range slice {
		if num%2 == 0 {
			fmt.Println(num, "is even")
		} else {
			fmt.Println(num, "is odd")
		}
	}
}
