
fn is_prime(k: u32) -> bool {
    let square_k = k as f64;
    if k < 1 {
        return false;
    }

    if k == 1 {
        return false;
    }
    
    if k == 2 {
        return true;
    }


    let limit2 = square_k.sqrt() as u32;
    for a in 2..=limit2 {
        if k % a == 0 {
            return false;
        }
    }

    return true;
}


fn problem_10(k: u128)-> u128 {
    let limit = k;
    let mut primes_below_limit: Vec<u32> = Vec::new();

    let mut sum_of_primes: u128 = 0;

    for n in 0..=limit as u32{
        if is_prime(n){
            primes_below_limit.push(n);
        }
    }

    for i in primes_below_limit.clone() {
        sum_of_primes += i as u128;
    }
    return sum_of_primes;
}

fn main() {
    println!("{}", problem_10(10));

}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(problem_10(10), 17);
    }

    #[test]
    fn test_2() {
        // This assert would fire and test will fail.
        // Please note, that private functions can be tested too!
        assert_eq!(problem_10(2000000), 142913828922);
    }
}
