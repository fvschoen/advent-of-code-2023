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

fn main() -> std::io::Result<()> {
    
    let file = File::open("input.txt")?;
    
    let grid: Vec<Vec<char>> = input_to_grid(file);

    println!("{:?}", grid);
    Ok(())
}
