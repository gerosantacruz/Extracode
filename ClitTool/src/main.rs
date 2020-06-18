use structopt::StructOpt;
use failure::ResultExt;
use exitfailure::ExitFailure;

// Seach the pattern in a file and display lines that contain it.
#[derive(StructOpt)]
struct Cli {
    // the pattern to look`kj
    pattern:String,
    //the path to the file to read 
    #[structopt(parse(from_os_str))]
    path: std::path::PathBuf,
}

fn find_matches(content: &str, pattern: &str, mut writer: impl std::io::Write){
    for line in content.lines(){
        if line.contains(pattern){
            println!("{}", line);
        }
    }
}

#[test]
fn find_a_match(){
    let mut result = Vec::new();
    find_matches("lorem ipsum\ndolor sit amet", "lorem", &mut result);
    assert_eq!(result, b"lorem ipsum\n");
}

fn main() -> Result<(), ExitFailure> {
    let args = Cli::from_args();
    let content = std::fs::read_to_string(&args.path)
        .with_context(|_| format!("could not read file `{}`", args.path.display()))?;

    find_matches(&content, &args.pattern, &mut std::io::stdout());

    Ok(())
}

