package main

import "testing"


func TestEndWith(t *testing.T){

	test1 := endwith("","  ")
	test2 := endwith("abc","c")
	test3 := endwith("ddad","cc")
	
	if test1 == true && test2 == true{
		t.Log("Pass the true test")
	}

	if test3 == false {
		t.Log("test False passed")
	}

}