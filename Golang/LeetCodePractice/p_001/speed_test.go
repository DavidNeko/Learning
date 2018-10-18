package main

import (
	"math/rand"
	"testing"

	"./algorithms"
)

const N = 10000

func BenchmarkTwoSum1(b *testing.B) {
	nums := []int{}
	for i := 0; i < N; i++ {
		nums = append(nums, rand.Int())
	}
	nums = append(nums, 7, 2)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		algorithms.TwoSum1(nums, 9)
	}
}

func BenchmarkTwoSum2(b *testing.B) {
	nums := []int{}
	for i := 0; i < N; i++ {
		nums = append(nums, rand.Int())
	}
	nums = append(nums, 7, 2)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		algorithms.TwoSum2(nums, 9)
	}
}
