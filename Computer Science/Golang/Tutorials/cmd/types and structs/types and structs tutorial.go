package main

import "fmt"

type dog struct {
	name   string
	legs   int
	breed  string
	colour string
	owner  owner
}

func (d dog) getHitByCar() {
	d.legs -= 1
}

//INSERT INTERFACE CODE HERE

type owner struct {
	name      string
	age       int
	insurance bool
}

func main() {
	fmt.Println("Hello World")

	var myDog dog = dog{"luke", 4, "Dachschund", "brown", owner{"Jay", 17, false}}
	fmt.Printf("My dog is %v\n", myDog.colour)
	fmt.Printf("%v's owner is called %v", myDog.name, myDog.owner.name)

	fmt.Println(myDog.legs)
	myDog.getHitByCar()
	fmt.Println(myDog.legs)

}
