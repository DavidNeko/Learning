package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

type logWriter struct{}

func main() {
	resp, err := http.Get("https://cn.bing.com/")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	lw := logWriter{}

	// only a temp way to log out response msg
	// fmt.Println(resp)

	// another way to log out response msg
	// a built-in function make() that creates a slice
	// with 99999 empty elements inside.

	// bs := make([]byte, 99999)
	// resp.Body.Read(bs)
	// fmt.Println(string(bs))

	// But you can replace the 3 lines of code above with this
	// one liner
	// This is the usage of the writer interface
	// io.Copy(os.Stdout, resp.Body)
	io.Copy(lw, resp.Body)
}

// We'll implement our own Write function
func (logWriter) Write(bs []byte) (int, error) {
	fmt.Println(string(bs))
	fmt.Println("Just wrote this many bytes:", len(bs))
	return len(bs), nil
}
