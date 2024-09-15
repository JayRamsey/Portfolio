package main

import "fmt"

func main() {
	fmt.Println("Hello World")

	var intNum int = 1 //can use signed and unsigned (uint32 or i32)
	fmt.Println(intNum)

	var floatNum float64 = 3.14159
	fmt.Println(floatNum)

	var myString string = "Hello World" + " - this string has been concatenated"
	fmt.Println(myString)

	//len() cannot account properly for non utf-8 characters (unicode)
	//import unicode/utf8
	//use utf8.RuneCountInString() to solve this.

	var myRune rune = 'a' // single quotes define a rune datatype
	fmt.Println(myRune)

	v1, v2 := 1, 2

	fmt.Println(v1, v2)

}
