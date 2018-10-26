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





