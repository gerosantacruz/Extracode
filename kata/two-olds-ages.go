package main

import (
    "fmt"
    "sort"
)

func twoAges() {
	
	s := []int{4, 2, 3, 1}
	sort.Ints(s)
	fmt.Println(s[len(s)-1]) // [1 2 3 4]
}


