package main

import (
	"fmt"
	"math/big")

func main() {
	var num int64 = 1
	//var prime int64 = 1
	goal := 10001
	i:= 1

	for i < goal {	
		if big.NewInt(num).ProbablyPrime(0) {
			num += 2
			i++
		} else {
			num +=2
		}
	}

	fmt.Println(num-2 , "is the prime number")
}