fn num_as_roman(num: i32) -> String {
 //let mut _RomanNumber = '';
 
 if num >= 1000 {
     return "M".to_string() + &num_as_roman(&num - 1000);

 } 

 if num >= 900 {
     return "CM".to_string() + &num_as_roman(&num - 900);
     
 }
 
 if num >= 500 {
     return "D".to_string() + &num_as_roman(&num - 500)
 }

 if num >= 400 {
     return "CD".to_string() + &num_as_roman(&num - 400)
 }


 if num >=100 {
     return "C".to_string() + &num_as_roman(&num - 100)
 }

 if num >=90 {
     return "XC".to_string() + &num_as_roman(&num - 90)
 }

 if num >=50{
     return "L".to_string() + &num_as_roman(&num - 50)
 }

 if num >=40 {
     return "XL".to_string() + &num_as_roman(&num - 40)
 }

 if num >=10 {
     return "X".to_string() + &num_as_roman(&num - 10)
 }

 if num >=9 {
     return "IX".to_string() + &num_as_roman(&num - 9)
 }

 if num >=5 {
     return "V".to_string() + &num_as_roman(&num - 5)
 }

 if num >=4 {
     return "IV".to_string() + &num_as_roman(&num - 4)
 }

 if num >=1 {
     return "I".to_string() + &num_as_roman(&num - 1)
 }
 
 else {
     return " ".trim().to_string()
 }

}


fn main() {
    //Complete Kata link -> https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/rustls
    println!("{}",num_as_roman(1900));
}
