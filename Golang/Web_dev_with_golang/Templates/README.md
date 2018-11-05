# Lecture 6: Understanding templates

A template allows us to create one document and then merge data with it.

We are learning about templates so that we can create one document, a web page, and then merge customized data to that page.

Web templates allow us to serve personalized results to users.

Think of Facebook - you log into your main page and see results tailored for you. That main page was created once. It is a template. However, for each user, that template gets populated with data specific to that user.

Another common exposure to templates that most of us get every day - junk mail.

A company creates a piece of mail to send to everyone, and then they merge data with that template to customize the mailing for each individual. The result:

## Template Example - Merged With Data

*** 

Dear Mr. Jones,
 
Are you tired of high electric bills?

We have noticed that your house at .....

*** 

Dear Mr. Smith,
 
Are you tired of high electric bills?

We have noticed that your house at .....

***

## Template Example - The Template

Dear {{Name}},

Are you tired of high electric bills?

We have noticed that your house at .....




***
***





# Lecture 7: Templating with concatenation

## Techniques we will learn

- concatenate
- CLI pipeline - output to a file with > 

## Code we will use from the standard library

## [os.Create](https://godoc.org/os#Create)
This allows us to create a file.
``` Go
func Create(name string) (*File, error)
```

*** 

## [defer](https://golang.org/ref/spec#Defer_statements)
The defer keyword allows us to defer the execution of a statement until the function in which we have placed the defer statement returns.

***

## [io.Copy](https://godoc.org/io#Copy)
This allows us to copy from from a source to a destination. 
``` Go
func Copy(dst Writer, src Reader) (written int64, err error)
```

## [strings.NewReader](https://godoc.org/strings#NewReader)
NewReader returns a new Reader reading from s.
``` Go
func NewReader(s string) *Reader
```

## [os.Args](https://godoc.org/os#pkg-variables)
Args is a variable from package os. Args hold the command-line arguments, starting with the program name.
``` Go
var Args []string
```



***
***




# Lecture 8: Understanding package text/template: parsing & executing templates

## [template.Template](https://godoc.org/text/template#Template)
``` Go
template.Template
```

***

## Parsing templates

### [template.ParseFiles](https://godoc.org/text/template#ParseFiles)
``` Go
func ParseFiles(filenames ...string) (*Template, error)
```

### [template.ParseGlob](https://godoc.org/text/template#ParseGlob)
``` Go
func ParseGlob(pattern string) (*Template, error)
```
***

### [template.Parse](https://godoc.org/text/template#Template.Parse)
``` Go
func (t *Template) Parse(text string) (*Template, error)
```

### [template.ParseFiles](https://godoc.org/text/template#Template.ParseFiles)
``` Go
func (t *Template) ParseFiles(filenames ...string) (*Template, error)
```

### [template.ParseGlob](https://godoc.org/text/template#Template.ParseGlob)
``` Go
func (t *Template) ParseGlob(pattern string) (*Template, error)
```

***

## Executing templates

### [template.Execute](https://godoc.org/text/template#Template.Execute)
``` Go
func (t *Template) Execute(wr io.Writer, data interface{}) error
```

### [template.ExecuteTemplate](https://godoc.org/text/template#Template.ExecuteTemplate)
``` Go
func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
```

***

## Helpful template functions

### [template.Must](https://godoc.org/text/template#Must)
``` Go
func Must(t *Template, err error) *Template
```

### [template.New](https://godoc.org/text/template#New)
``` Go
func New(name string) *Template
```

***

## The init function

### [The init function](https://golang.org/doc/effective_go.html#init)
``` Go
func init()
```




***
***






# Lecture 9: Passing Data To Templates

You get to pass in one value - that's it!

Fortunately, we have many different types which that value can be including composite types which compose together values. (These are also known as aggregate data types - they aggregate together many different values).

## Slice
Use this for passing in a bunch of values of the same type. We could have a []int or a []string or a slice of any type.

## Map 
Use this for passing in key-value data.

## Struct
This is probably the most commonly used data type when passing data to templates. A struct allows you to compose together values of different types.









***
***







# Lecture 10: Template variables

## [template variables](https://godoc.org/text/template#hdr-Variables)

### ASSIGN
``` Go
{{$wisdom := .}}
```

### USE
``` Go
{{$wisdom}}
```

A pipeline inside an action may initialize a variable to capture the result. The initialization has syntax
 
 $variable := pipeline
 
 where $variable is the name of the variable. An action that declares a variable produces no output.
 
 If a "range" action initializes a variable, the variable is set to the successive elements of the iteration. Also, a "range" may declare two variables, separated by a comma:
 
  range $index, $element := pipeline
  
 in which case $index and $element are set to the successive values of the array/slice index or map key and element, respectively. Note that if there is only one variable, it is assigned the element; this is opposite to the convention in Go range clauses.
 
 A variable's scope extends to the "end" action of the control structure ("if", "with", or "range") in which it is declared, or to the end of the template if there is no such control structure. A template invocation does not inherit variables from the point of its invocation.
 
 When execution begins, $ is set to the data argument passed to Execute, that is, to the starting value of dot.
 
 



***
***





# Lecture 11: Passing data to templates

These files provide you with examples of passing various data types to templates.




***
***









# Lecture 12&13:  Using functions in templates

## [template function documentation](https://godoc.org/text/template#hdr-Functions)

***

## [template.FuncMap](type FuncMap map[string]interface{})

FuncMap is the type of the map defining the mapping from names to functions. Each function must have either a single return value, or two return values of which the second has type error. In that case, if the second (error) return value evaluates to non-nil during execution, execution terminates and Execute returns that error.

## [template.Funcs](https://godoc.org/text/template#Template.Funcs)
``` Go
func (t *Template) Funcs(funcMap FuncMap) *Template
```

***

During execution functions are found in two function maps: 
- first in the template, 
- then in the global function map. 

By default, no functions are defined in the template but the Funcs method can be used to add them.

Predefined global functions are defined in text/template.



***
***





# Lecture 14: Global Functions

There are "predefined global functions" which you can use.

[You can read about these functions here](https://godoc.org/text/template#hdr-Functions)

The following code samples will demonstrate some of these "predefined global functions":

- index

- and

- comparison
 
 ***
 
# Comments

## [Template Comments](https://godoc.org/text/template#hdr-Actions)
- A comment; discarded. May contain newlines. Comments do not nest and must start and end at the delimiters, as shown here.
``` Go
{{/* a comment */}}
```



***
***




# Lecture 15: Nested templates

[nested templates documentation](https://godoc.org/text/template#hdr-Nested_template_definitions)

## define: 
``` Go
{{define "TemplateName"}}
insert content here
{{end}}
```
## use: 
``` Go
{{template "TemplateName"}}
```






***
***





# Lecture 16: Passing data to templates

These files provide you with more examples of passing data to templates.

These files use the [composition](https://en.wikipedia.org/wiki/Composition_over_inheritance) design pattern. You should favor this design pattern. 

Read more about [composition with Go here](https://www.goinggo.net/2015/09/composition-with-go.html).







***
***




# Lecture 18: Cross-site scripting (XSS)

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications.

XSS enables attackers to inject client-side scripts into web pages viewed by other users. 

A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy): you have a script on one site that makes a request to another site. For example: you come to my cool website about kittens, and a script runs to transfer money from UnionBank to my foreign account. If it wasn't for the "same-origin policy" implemented in browsers, and if you had a cookie on your machine that said you were logged into Union Bank, then the money would transfer. 

Cross-site scripting carried out on websites accounted for roughly 84% of all security vulnerabilities documented by Symantec as of 2007. Their effect may range from a petty nuisance to a significant security risk, depending on the sensitivity of the data handled by the vulnerable site and the nature of any security mitigation implemented by the site's owner.

***

## Same-origin policy

In computing, the same-origin policy is an important concept in the web application security model. 

Under the policy, a web browser permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin. 

An origin is defined as a combination of URI scheme, hostname, and port number. 

This policy prevents a malicious script on one site from obtaining access to sensitive data on another site.

## Example

Assume a user is visiting a banking website and doesn't log out. 

Then he goes to another site and that site has some malicious JavaScript code running in the background that requests data from the banking site. 

Because the user is still logged in on the banking site, without the "same-origin policy" implemented in browsers, that malicious code could do anything on the banking site. 

For example, get a list of your last transactions, create a new transaction, etc. This is because the browser can send and receive session cookies to the banking website based on the domain of the banking website. A user visiting that malicious site would expect that the site he is visiting has no access to the banking session cookie. While this is true, the JavaScript has no direct access to the banking session cookie, but it could still send and receive requests to the banking site with the banking site's session cookie, essentially acting as a normal user of the banking site! 

Regarding the sending of new transactions, even CSRF (cross-site request forgery) protections by the banking site have no effect, because the script can simply do the same as the user would do. 

So this is a concern for all sites where you use sessions and/or need to be logged in. 

### All modern browsers implement some form of the Same-Origin Policy as it is an important security cornerstone.

This mechanism bears a particular significance for modern web applications that extensively depend on HTTP cookies to maintain authenticated user sessions, as servers act based on the HTTP cookie information to reveal sensitive information or take state-changing actions. 

A strict separation between content provided by unrelated sites must be maintained on the client-side to prevent the loss of data confidentiality or integrity.







***
***






# Lecture 19: Understanding servers


[Link to learning note for lecture 19](https://github.com/DavidNeko/Learning/tree/master/Golang/Web_dev_with_golang/Templates/Lecture19/README.md)



***
***





# Lecture 20: HTTP Server

HTTP uses TCP.

To create a server that works with HTTP, we just create a TCP server.

To configure our code to handle request/response in an HTTP fashion which works with browsers, we need to adhere to HTTP standards.

## TCP server essentials

### Listen
 
 [net.Listen](https://godoc.org/net#Listen)
``` Go
func Listen(net, laddr string) (Listener, error)
```

### Listener

[net.Listener](https://godoc.org/net#Listener)
``` Go
type Listener interface {
    // Accept waits for and returns the next connection to the listener.
    Accept() (Conn, error)

    // Close closes the listener.
    // Any blocked Accept operations will be unblocked and return errors.
    Close() error

    // Addr returns the listener's network address.
    Addr() Addr
}
```

### Connection

[net.Conn](https://godoc.org/net#Conn)
``` Go
type Conn interface {
    // Read reads data from the connection.
    Read(b []byte) (n int, err error)

    // Write writes data to the connection.
    Write(b []byte) (n int, err error)

    // Close closes the connection.
    // Any blocked Read or Write operations will be unblocked and return errors.
    Close() error

    // LocalAddr returns the local network address.
    LocalAddr() Addr

    // RemoteAddr returns the remote network address.
    RemoteAddr() Addr

    SetDeadline(t time.Time) error

    SetReadDeadline(t time.Time) error

    SetWriteDeadline(t time.Time) error
}
```

### Dial

[net.Dial](https://godoc.org/net#Dial)
``` Go
func Dial(network, address string) (Conn, error)
```

***

## Write

[io.WriteString](https://godoc.org/io#WriteString)
``` Go
func WriteString(w Writer, s string) (n int, err error)
```

[fmt.Fprintln](https://godoc.org/fmt#Fprintln)
``` Go
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
```

***

## Read

- [ioutil.ReadAll](https://godoc.org/io/ioutil#ReadAll)
``` Go
func ReadAll(r io.Reader) ([]byte, error)
```

- [bufio.NewScanner](https://godoc.org/bufio#NewScanner)
``` Go
func NewScanner(r io.Reader) *Scanner
```

- [bufio.Scan](https://godoc.org/bufio#Scanner.Scan)
``` Go
func (s *Scanner) Scan() bool
```

- [bufio.Text](https://godoc.org/bufio#Scanner.Text)
``` Go
func (s *Scanner) Text() string
```

***

## Read & Write

- [io.Copy](https://godoc.org/io#Copy)
``` GO
func Copy(dst Writer, src Reader) (written int64, err error)
```





***
***





