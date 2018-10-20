package main

import (
	"fmt"
)

// HANDS ON 3
// create an interface type that both person and secretAgent implement
// declare a func with a parameter of the interface’s type
// call that func in main and pass in a value of type person
// call that func in main and pass in a value of type secretAgent

type person struct {
	fname string
	lname string
	age   int
}

type secretAgent struct {
	person
	ltk bool
}

func (p person) speak() string {
	return fmt.Sprintln("Ayyyyyyy Imma person")
}

func (sa secretAgent) speak() string {
	return fmt.Sprintln("shaken, not stirred")
}

type humanoid interface {
	speak() string
}

func vomit(h humanoid) {
	fmt.Printf("%T\n", h)
	fmt.Println(h)

	switch v := h.(type) {
	case person:
		fmt.Println(v.fname)
	case secretAgent:
		fmt.Println(v.fname)
	default:
		fmt.Println("unknown")
	}
}

func main() {
	p1 := person{"Dav", "Wang", 22}
	sa1 := secretAgent{person{"Chai", "P", 23}, false}
	vomit(p1)
	vomit(sa1)
}
