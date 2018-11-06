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






# Lecture 21: HTTP Server

HTTP uses TCP.

To create a server that works with HTTP, we just create a TCP server.

To configure our code to handle request/response in an HTTP fashion which works with browsers, we need to adhere to HTTP standards.

### HTTP/1.1 message

An HTTP message is made up of the following:

- a request/status line 
- zero or more header fields 
- an empty line indicating the end of the header section 
- an optional message body.

***

### Request line (request)

GET / HTTP/1.1

[method SP request-target SP HTTP-version CRLF](https://tools.ietf.org/html/rfc7230#section-3.1.1)

### Status line (response)

HTTP/1.1 302 Found

[HTTP-version SP status-code SP reason-phrase CRLF](https://tools.ietf.org/html/rfc7230#section-3.1.2)

***

## Writing a response

``` Go
body := "CHECK OUT THE RESPONSE BODY PAYLOAD"
io.WriteString(conn, "HTTP/1.1 200 OK\r\n") 			// status line
fmt.Fprintf(conn, "Content-Length: %d\r\n", len(body)) 	// header
fmt.Fprint(conn, "Content-Type: text/plain\r\n") 		// header
io.WriteString(conn, "\r\n") 							// blank line; CRLF; carriage-return line-feed
io.WriteString(conn, body) 								// body, aka, payload
```

***

## Useful for parsing the request-line & status-line

### Parsing String

[strings.Fields](https://godoc.org/strings#Fields)
``` Go
func Fields(s string) []string
```






***
***





