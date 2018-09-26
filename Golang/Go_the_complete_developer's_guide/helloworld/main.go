package main

/*
  Question: What does `package main` mean?

    There are two types of packages in Golang:
      - executable packages
        Generates a file that we can run
      - Reusable packages
        Code used as 'helpers'.
        Good place to put reusable logic

    package main -> go build -> main.exe
    'main'作为关键字，表示此package是executable
    如果package name是其他的词，`go build`则不会生成.exe文件
    所以除了 package main以外，其他的 package name都会生成 Reusable package
*/

import "fmt"

/*
  What does `import "fmt"` mean here?

    import allow us to access other packages written by others
    Here it means import a package called "fmt" (which lies in the standard lib)

    visit golang.org/pkg/ to find out more about all packages that you can use

*/

func main() {
	fmt.Println("Hi there!")
}

/*
  What does this func() thing mean?
    func() declares a function.

  How is the main.go file organized?
    - package declaration -
    - import other packages that we need -
    - Declare functions, tell Go to do things -

*/

/*
Lecture note:

1) How to run it?
  `go run main.go`

  - other commands in go -
  1. `go build main.go`
      builds and complies a executable file
  2. `go fmt`
      formats all the code in each file in the current
      directory
  3. `go install`
      Compiles and "installs" a package
  4. `go get`
      Downloads the raw source code of someone
      else's package
  5. `go test`
      Runs any tests associated with the current
      project
*/
