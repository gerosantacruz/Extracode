package main

import (

    "fmt"
)

// Complete the staircase function below.
func staircase(n int32) {

	rows := int(n)
	
	for a := 0; a < rows; a++ {

		for i :=0; i <=rows-a-1;i++ {
			fmt.Print(" ");
		}

		for j:=0; j <= a; j++ {
			fmt.Print("#");
		}
		fmt.Println();
	}
}

func main(){
	staircase(6);
}

