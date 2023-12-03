// Advent of Code 2023
// 2023 December 03
// Frank Schoeneman

use std::fs::File;
use std::io::{BufRead, BufReader};


fn input_to_grid(file: File) -> Vec<Vec<char>> {

    let reader = BufReader::new(file);

    let grid: Vec<Vec<char>> = reader.lines()
                                     .map(|line| line.unwrap().chars().collect())
                                     .collect();
    grid
}

fn is_symbol(this_char: char) -> bool {

    // "!@#$%^&*()-+?_=,<>/"
    let symbols = String::from("!@#$%^&*()-+?_=,<>/");
    symbols.contains(this_char)    
}

fn find_symbols(grid: &Vec<Vec<char>>) -> Vec<char> {

    let mut symbol_list = Vec::new();
    
    for row in grid {
        for &this_char in row {

            if is_symbol(this_char) {
               symbol_list.push(this_char);
            }
        } 
    }
    symbol_list
}


fn main() -> std::io::Result<()> {
    
    let file = File::open("input.txt")?;
    
    let grid: Vec<Vec<char>> = input_to_grid(file);
    //println!("{:?}", grid);

    let sym: Vec<char> = find_symbols(&grid);
    println!("{:?}", sym);

    Ok(())
}
