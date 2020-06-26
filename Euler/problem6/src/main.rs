fn main() {
    use std::io;

    let mut input_text = String::new();
    io::stdin()
        .read_line(&mut input_text)
        .expect("failed to read from stdin");

    let trimmed = input_text.trim();
    let num = trimmed.parse::<i32>().unwrap();

    sum_square_diference(num);
    sum_square_diference_arithmetic(num);
}

fn sum_square_diference(num: i32){

    let mut sum1 = 0;
    let mut sum2 = 0;
    let mut result =0;

    for i in 1..=num {
        sum1 += i.pow(2);
        sum2 += i;
    }

    sum2 = sum2.pow(2);
    result = sum2 - sum1;

    println!("The sum of square diference is {} ", result);
}

fn sum_square_diference_arithmetic(num:i32){
    let sum = num * (num+1) / 2;
    let square = (num * (num + 1) * (2*num + 1))/6;

    let result = sum * sum - square;

    println!("The result in arithmetic way is {}", result);
}