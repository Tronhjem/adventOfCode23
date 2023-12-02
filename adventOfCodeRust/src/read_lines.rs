use std::fs::File;
use std::path::Path;
use std::fs::read_to_string;

pub fn read_lines(filename: &str) -> Vec<String> 
{
    let path = Path::new(filename);
    let _file = match File::open(&filename) {
        Err(why) => panic!("couldn't open {}: {}", path.display(), why),
        Ok(file) => file,
    };    
    
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}