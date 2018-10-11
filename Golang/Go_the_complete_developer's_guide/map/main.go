package main

import (
	"fmt"
)

func main() {
	// Additional ways to init an empty map

	// var colors map[string]string
	// colors := make(map[int]string)

	// we are declaring a map with all of the keys
	// type stirng and all values type string as well
	colors := map[string]string{
		"red":   "#ff0000",
		"green": "#008000",
		"white": "#ffffff",
	}

	// Add value to an existing map
	// colors[10] = "#ffffff"

	// Delete values in an existing map
	// delete(colors, 10)

	printMap(colors)
}

// Simple example of iterating a map
func printMap(c map[string]string) {
	for color, hex := range c {
		fmt.Println("Hex code for", color, "is", hex)
	}
}

/*
	** Differences between Map and Struct **

	For Map:
		* All keys must be the same type
		* All values must be the same type
		* Keys are indexed - we can iterate them
		* Use to represent a collection of related properties
		* Don't need to know all the keys at compile time
		* Reference Type!

	For Struct:
		* Values can be of different type
		* Keys don't support indexing
		* You need to know all the different fields at compile time
		* Use to represent a "thing" with a lot of different properties
		* Value Type!

*/
