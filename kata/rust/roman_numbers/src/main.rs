fn num_as_roman(num: i32) -> String {
 //let mut _RomanNumber = '';
 
 if num >= 1000 {
     return "M".to_string() + &num_as_roman(&num - 1000);

 } 

 if num >= 900 {
     return "CM".to_string() + &num_as_roman(&num - 900);
     
 } else {
     return " ".trim().to_string()
 }

}


fn main() {

    println!("{}",num_as_roman(1900).len());
}
