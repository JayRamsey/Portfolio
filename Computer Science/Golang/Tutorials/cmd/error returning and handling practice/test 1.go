package main

import (
	"errors"
	"fmt"
)

func main() {
	printMe("Hello World")

	var numerator int = 11
	var denominator int = 2
	var result, remainder, err = intDevision(numerator, denominator)

	if err != nil {
		fmt.Println(err.Error())
	} else if remainder == 0 {
		fmt.Printf("The result of the interger division is %v", result)
	} else {
		fmt.Printf("The result of the integrer division is %v with the remainder %v", result, remainder)
	}
}

func intDevision(numerator int, denominator int) (int, int, error) {
	var err error
	if denominator == 0 {
		err = errors.New("Cannot divide by zero")
		return 0, 0, err
	}
	var result int = numerator / denominator
	var remainder int = numerator % denominator
	return result, remainder, err
}

func printMe(printValue string) {
	fmt.Println(printValue)
}
