package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	// Open file
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	// if contents, err := ioutil.ReadAll(file); err == nil {
	// 	// result := strings.Replace(string(contents), "\n", "", -1)
	// 	fmt.Println(string(contents))
	// }

	// Sample answer from instructor
	io.Copy(os.Stdout, file)

}
