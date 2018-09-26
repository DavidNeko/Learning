package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()

	// check if deck has correct number of cards
	// Note: %v here means passing the value into string
	// 为传入的值预留了空位
	if len(d) != 16 {
		t.Errorf("Expected deck length of 16, but got %v", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card of Ace of Spades, but got %v", d[0])
	}

	if d[len(d)-1] != "Four of Clubs" {
		t.Errorf("Expected last card of Four of Clubs, but got %v", d[len(d)-1])
	}
}

func TestSaveToDeckAndNewDeckTestFromFile(t *testing.T) {
	// remove dirty test files
	os.Remove("_decktesting")

	// create a new deck and save it to file
	deck := newDeck()
	deck.saveToFile("_decktesting")

	// load the deck
	loadedDeck := newDeckFromFile("_decktesting")

	// check loaded deck
	if len(loadedDeck) != 16 {
		t.Errorf("Expected 16 cards in deck, got %v", len(loadedDeck))
	}

	// remove it
	os.Remove("_decktesting")
}
