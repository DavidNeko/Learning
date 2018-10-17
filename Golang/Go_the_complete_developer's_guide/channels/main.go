package main

import (
	"fmt"
	"net/http"
	"time"
)

/*
We use this program to check the avaliability of
each websites

- we first loop through the list following it's order
- then we re-factor our code and fetch multiple requests
	at the same time (using goRoutine)

	- By default, Go tries to use one core!
	- **Concurrency**
		- We can have multiple threads executing code
		- If one thread blocks, another one is picked up and
		  worked on

	- **Parallelism**
		- Multiple threads executed at the exact same time.
		- Require multiple CPUs

*/
func main() {
	// a list of websites we are going to check
	// Note: commented websites don't work in China. :)
	links := []string{
		// "http://google.com",	// not working
		// "http://facebook.com", // not working
		"http://stackoverflow.com",
		// "http://golang.org",	// not working
		// "http://amazon.com",	// not working
		"http://baidu.com",
		"http://github.com",
		"http://www.v2ex.com",
		"http://www.csdn.net",
	}

	// create a channel with type string
	c := make(chan string)

	// loop through all links
	for _, link := range links {
		// checkLink(link) // not using goRoutine
		// to use goRoutine use 'go' keyword
		// addon: pass in channel c to communicate
		go checkLink(link, c)
		/*
			If you simply use go checkLink(link)
			the program would quit after you run it.
			Because the main Routine exits after the for loop
			is executed.

			To solve this, we are going to use 'channel'

			* Using channels is the only way we have
			  to communicate between different goRoutines
		*/

	}
	/*
		'fmt.Println(<-c)' receive value from channel
		And this is a blocking call.
		If you have five of them called here,
		it will work as you expected
	*/
	// fmt.Println(<-c)
	// fmt.Println(<-c)
	// fmt.Println(<-c)
	// fmt.Println(<-c)
	// fmt.Println(<-c)

	// loop through all channel messages
	// for i := 0; i < len(links); i++ {
	// 	fmt.Println(<-c)
	// }

	// go on to check the next link (infinite loop)
	// for {
	// 	go checkLink(<-c, c)
	// }

	// Alternative loop (exactly the same as the loop above)
	for l := range c {
		// go checkLink(l, c)
		// we'll replace the goRoutine call with a function Literal
		// Which is similar to Lambda in Python
		go func(link string) {
			// pause the current goRoutine for 5 seconds
			time.Sleep(5 * time.Second)
			checkLink(link, c)
			/*
				* Channel Gotcha!

				Warning: loop variable l captured by func literal

					After you executed the code, it will fetch all
					5 websites at first and keep fetching from only one
					website(here is github.com)

					This is because the goRoutine is still looking
					at the value l after the checkLink request in resolved

					to solve this, pass in 'l'
			*/
		}(l)
	}

}

func checkLink(link string, c chan string) {
	// we don't care the response here, only errors
	_, err := http.Get(link)

	if err != nil {
		fmt.Println(link, "might be down!")
		// send signal to channel
		// c <- "Might be down I think"
		c <- link
		return
	}

	fmt.Println(link, "is up!")
	// send signal to channel
	// c <- "Yep its up"
	c <- link
}
