package main

import "fmt"
import "strings"



func main() {
	str1 := ""
	str2 := "c"

	fmt.Println(endwith(str1, str2))
	
}

func endwith(str, ending string) bool {

	trimstr := strings.Trim(ending," ")

	

	if len(str) == 0 && len(trimstr) == 0 {
		return true
	} else if len(str) == 0 && len(ending) != 0 {
		return false
	}

	num := len(ending)

	slice := str[len(str)-num:]

	fmt.Println(slice)


	if slice == ending {
		return true
	}
		return false


}