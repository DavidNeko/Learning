package main

import (
	"fmt"
)

// HANDS ON 2
// create a struct that holds person fields
// create a struct that holds secret agent fields and embeds person type
// attach a method to person: pSpeak
// attach a method to secret agent: saSpeak
// create a variable of type person
// create a variable of type secret agent
// print a field from person
// run pSpeak attached to the variable of type person
// print a field from secret agent
// run saSpeak attached to the variable of type secret agent
// run pSpeak attached to the variable of type secret agent

type person struct {
	fname string
	lname string
}

type secretAgent struct {
	person
	licenseToKill bool
}

func (p person) pSpeak() {
	fmt.Println(p.fname, `says, "Wazzzup!"`)
}

func (s secretAgent) saSpeak() {
	fmt.Println(s.fname, "has a license to kill:", s.licenseToKill)
}

func main() {
	p := person{"Dav", "Wang"}
	s := secretAgent{person{"James", "Bond"}, true}

	fmt.Println(p.fname)
	p.pSpeak()
	fmt.Println(s.fname)
	s.saSpeak()
	s.pSpeak()

}
