fn is_prime(k: u32) -> bool {
    if k < 1 {
        return false;
    }

    if k == 1 {
        return true;
    }

    for a in 2..k {
        if k % a == 0 {
            return false;
        }
    }

    return true;
}


fn main() {
    let mut x = 0;

    for n in 1..10{
        let p = is_prime(n);
        println!("{}", p);
        if is_prime(n){
            x += n;
        }
    }
}
