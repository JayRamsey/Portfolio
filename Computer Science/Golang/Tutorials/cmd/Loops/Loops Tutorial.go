package main

import "fmt"

func main() {
	fmt.Println("Hello World")

	//different ways for loops can be declared:

	var myMap = map[string]uint8{"Hello World": 12, "Woah!": 3}

	// way 1
	for key, value := range myMap {
		fmt.Printf("The value '%v' has the key '%v'\n", key, value)
	}

	// way 2
	i := 0
	for i < 10 {
		fmt.Println(i)
		i++
	}

	// way 3
	i = 0
	for {
		if i >= 10 {
			break
		}
		fmt.Println(i)
		i++
	}

	//way 4
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

}
