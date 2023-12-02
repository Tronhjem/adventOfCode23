use std::io::Result;

mod read_lines;
use read_lines::read_lines;

mod day_one;
use day_one::first;
use day_one::second;

fn main() -> Result<()>
{
    let path = "/Users/christiantronhjem/dev/adventOfCode23/data/1.txt";
    let lines: Vec<String> = read_lines(path);

    // let result = first(&lines);
    let result = second(&lines);
    
    println!("__________");
    println!("result: {}", result);
    println!("__________");
    
    Ok(())
}
