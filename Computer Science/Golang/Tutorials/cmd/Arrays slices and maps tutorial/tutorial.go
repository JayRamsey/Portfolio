package main

import "fmt"

func main() {
	fmt.Println("Hello World")

	//arrays
	var intArr [3]int32
	//or intArr := [3]int32{1, 2, 3}
	fmt.Println(intArr[0:3]) //[0 0 0]
	intArr[0] = 281
	fmt.Println(intArr[0:3]) //[1 0 0]     range is [x:y) inclusive
	fmt.Println(intArr[0:2])

	// & gets pointer
	fmt.Println(&intArr[0])

	//slices
	var intSlice []int32 = []int32{4, 5, 6}
	fmt.Println(intSlice)
	intSlice = append(intSlice, 7)
	fmt.Println(intSlice)

	//maps
	var myMap = map[string]uint8{"Adam": 28, "Sarah": 45}
	fmt.Println(myMap)

}
