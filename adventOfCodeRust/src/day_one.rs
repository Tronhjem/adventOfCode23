pub fn first(lines: &Vec<String>) -> u32
{
    // In this example, the calibration values of these four 
    // lines are 12, 38, 15, and 77. 
    // Adding these together produces 142.

    // let string_array: [&str; 4] = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"];
   let mut final_sum: u32 = 0; 
    
    for some_string in lines
    {
        let mut first_int: u32 = 0;
        let mut last_int: u32 = 0;

        for some_char in some_string.chars()
        {
            if let Some(integer_value) = some_char.to_digit(10) 
            {
                if first_int == 0
                {
                    first_int = integer_value * 10;
                }

                last_int = integer_value;
            } 
        }

        final_sum += first_int + last_int;
        // println!("{}", first_int+last_int);
        // println!("_______");
    }

    return final_sum;

}

pub fn second(lines: &Vec<String>) -> u32
{
    // In this example, the calibration values are 
    // 29, 83, 13, 24, 42, 14, and 76. 
    // Adding these together produces 281.
    let mut string_array: [&str; 7] = ["two1nine", 
    "eightwothree", "abcone2threexyz", "xtwone3four", 
    "4nineeightseven2", "zoneight234", "7pqrstsixteen"];

    let numbers: [char; 10] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let words: [&str; 10] = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eigth", "nine"];

    let mut mod_strings: Vec<String> = Vec::new();


    for (index, value) in lines.iter().enumerate() {

        let mut changedEntry = lines[index].replace("one", "o1e");

        changedEntry = changedEntry.replace("two", "t2o");
        changedEntry = changedEntry.replace("three", "t3e");
        changedEntry = changedEntry.replace("four", "f4r");
        changedEntry = changedEntry.replace("five", "f5e");
        changedEntry = changedEntry.replace("six", "s6x");
        changedEntry = changedEntry.replace("seven", "s7n");
        changedEntry = changedEntry.replace("eight", "e8t");
        changedEntry = changedEntry.replace("nine", "n9e");

    //     println!("{}", changedEntry);
        mod_strings.push(changedEntry);
    }

   return first(&mod_strings);

}