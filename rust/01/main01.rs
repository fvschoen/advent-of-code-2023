use std::fs::File;
use std::io::{self, BufRead};

// Advent of Code 2023
// 2023 December 01
// Frank Schoeneman


fn find_cal_codes(file_path: &str) -> io::Result<i32> {

    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut total = 0;

    for line in reader.lines() {

        let line = line?;
        let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();

        let first_digit = digits[0].to_string();
        let last_digit = digits.last().unwrap().to_string();
 
        let concat_digits = format!("{}{}", first_digit, last_digit);
        let line_code: i32 = concat_digits.parse().unwrap();

        total += line_code;

    }
    Ok(total)

}

fn main() {

    let file_path = "input.txt";
    match find_cal_codes(file_path){
        Ok(total) => println!("Total: {}", total), Err(err) => eprintln!("Error: {}", err),
    }
}
