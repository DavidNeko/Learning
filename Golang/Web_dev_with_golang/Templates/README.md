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




