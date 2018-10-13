package main

import (
	"fmt"
)

type bot interface {
	/*
		If you are a type in this program with a function
		called 'getGreeting' and you return a string, then
		you are now an honorary member of type 'bot'
	*/
	getGreeting() string
}

type englishBot struct{}
type spanishBot struct{}

/*
	For this file, we are gonna create two chatbots
	to get familiar with interface in golang
*/

func main() {
	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}

func printGreeting(b bot) {
	/*
		Now that you're also an honorary member of type 'bot',
		you can now call this function called 'printGreeting'
	*/
	fmt.Println(b.getGreeting())
}

/*
	For printGreeting function, we'll use the same logic
	So the functions would be like this:

func printGreeting(eb englishBot) {
	fmt.Println(eb.getGreeting())
}

func printGreeting(sb spanishBot) {
	fmt.Println(sb.getGreeting())
}

	But this code won't work. We need interface to solve this
	problem.
	Therefore, we declare a new interface type.
*/

/*
	For getGreeting function, we'll pertend that each bot
	uses it's own logic.
*/
func (englishBot) getGreeting() string {
	// VERY custom logic for generating an english greeting
	return "Hi there!"
}

func (spanishBot) getGreeting() string {
	return "Hola!"
}

/*
Notes about interfaces:

	- Interfaces are NOT generic types
	- Interfaces are implicit
	- Interfaces are a contract to help us manage types
	- Interfaces are tough. Step#1 is understanding how
	  to read them
*/

/*
For types:
	Concrete type:
		- map
		- struct
		- int
		- string
		- englishBot

	Interface Type:
		- bot
*/
