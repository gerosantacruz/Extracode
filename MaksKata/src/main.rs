fn main() {
    let cc= "1111111";
    
    /* let (fist, last) = cc.split_at(cc.len()-1); */
   
    println!("{}", maskify(&cc));
}


fn maskify(cc: &str) -> String {
    let mut mask = "".to_owned();

    if cc.len() <= 4 {
        
        return (&cc).to_string();

    }else {
    //mask= &"#".repeat(cc.len()-4) + cc.split_at(cc.len() - 4);
    mask.push_str(&"#".repeat(cc.len()-4));
    mask.push_str(cc.split_at(cc.len() - 4).1);
    }

    return mask;


}  
