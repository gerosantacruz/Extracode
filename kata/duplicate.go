package main

import (
	"fmt"
	"strings"
)

func dupli(word string)string{
	//newword := strings.ToLower(word)
	res := ""
	for _,x := range word {
		rep := strings.Count(word,strings.ToLower(string(x)))
		
		if rep > 1 {
			res += ")"
		} else {
			res += "("
		}
		
	}
	return res

}

func main() {
	fmt.Println("hello world")
	fmt.Println(dupli("Success"))
}

