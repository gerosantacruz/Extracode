fn main() {
    println!("Hello, world!");
    let x = create_phone_number(&[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);

    println!("{}",x);

}

fn create_phone_number(numbers: &[u8]) -> String {
    let mut phone:String = "(".to_owned();

    for (pos,e) in numbers.iter().enumerate() {

        if pos == 3 {
            phone.push_str(") ");
        }

        if pos == 6 {
            phone.push_str("-");

        }

        phone.push_str(&e.to_string());
        
    }
    return phone;

}

