package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"strings"
	"time"
)

// Creawte a new type of `deck`
// which is a slice of strings
type deck []string

func newDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spades", "Diamonds", "hearts", "Clubs"}
	cardValues := []string{"Ace", "Two", "Three", "Four"} // Just for testing

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value+" of "+suit)
			// append(append_to_what, what_to_append)
		}
	}

	return cards
}

// recever中 一般用1或2个字母的简写代表指定type
func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

// paramters: deck and handsize
// return values; deck and deck
func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

// helper function: convert deck to string
// Question here: use deck as a received or pass
// it in as a prameter??
func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}

// Use ioutil->WriteFile() to save to file
// this function saves a deck to hard drive
// permission 0666 means anyone can r/w the file
func (d deck) saveToFile(filename string) error {
	return ioutil.WriteFile(filename, []byte(d.toString()), 0666)
}

// load a new deck from file
// this function uses io/ioutil -> readfile
func newDeckFromFile(filename string) deck {
	bs, err := ioutil.ReadFile(filename)
	if err != nil {
		// Option #1 - Log the error and return a call
		// to newDeck()
		// Option #2 - Log the error and entirely quit
		// the program (what we use here)
		fmt.Println("Error:", err)
		os.Exit(1) // 0 for success, other number otherwise
	}

	// convert byteslice bs into a string and split it
	s := strings.Split(string(bs), ",")
	// convert it into a deck
	// we can do deck(s) because deck type is slice of string
	return deck(s)
}

// Shuffle function
func (d deck) shuffle() {
	// make a REAL random number generator
	// to get a int64 to pass into NewSource()
	// use time->UnixNano(which generate a int64)
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)

	for i := range d {
		newPosition := r.Intn(len(d) - 1)

		// swap positions
		d[i], d[newPosition] = d[newPosition], d[i]
	}
}
