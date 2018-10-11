package main

import (
	"fmt"
)

type contackInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contackInfo
}

func main() {
	/*
		alex := person{"Alex", "Anderson"}
		// A method to create a person
		// not recommended tho

		bob := person{firstName: "Bobby", lastName: "Dylon"}
		// method 2, better than the one above
	*/

	// var alex person
	/*
		fmt.Println(alex)
		fmt.Printf("%+v", alex)
		// two ways to printout the value
	*/
	// update value
	// alex.firstName = "Alex"
	// alex.lastName = "Anderson"

	jim := person{
		firstName: "Jim",
		lastName:  "Dope",
		contackInfo: contackInfo{
			email:   "Jim@gmail.com",
			zipCode: 48823,
		},
	}
	// jim.print()

	/*
		// '&' gives the memory address of value
		jimPointer := &jim

		// jim.upDateName("Kush")
		jimPointer.upDateName("Kush")

		// from testing we know that this update does Not
		// take effect because pointer doesnt change
		jim.print()

		// fmt.Printf("%+v", jim)
	*/

	// Short cut of the method above
	jim.upDateName("Kush")
	jim.print()

}

func (p person) print() {
	fmt.Printf("%+v", p)

}

// '*' here means we're working with a ptr to a person
// NOTE: `person` here is a type
func (pointerToPerson *person) upDateName(newFirstName string) {
	// '*' here gives the value the memory address is pointing at
	// "pointerToPerson" here is a value of type `person`
	(*pointerToPerson).firstName = newFirstName
}

/*
Note:
Turn address into value with `*address`
Turn value into address with `&value`
*/
