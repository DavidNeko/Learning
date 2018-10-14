package main

import (
	"fmt"
)

type shape interface {
	getArea() float64
}

type triangle struct {
	height float64
	base   float64
}
type square struct {
	sideLength float64
}

func main() {
	// init a triangle and print area
	tshape := triangle{
		height: 1.0,
		base:   2.5,
	}

	printArea(tshape)

	// init a square and print area
	sshape := square{
		sideLength: 2.5,
	}
	printArea(sshape)
}

func printArea(sp shape) {
	fmt.Println(sp.getArea())
}

func (t triangle) getArea() float64 {
	Area := 0.5 * t.base * t.height
	return Area
}

func (s square) getArea() float64 {
	Area := s.sideLength * s.sideLength
	return Area
}
