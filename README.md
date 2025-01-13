# JavaScript Exercise Evaluator

This tool automatically evaluates JavaScript exercises by cloning a GitHub repository and analyzing the implementation against specified requirements, using OpenInterpreter

## Prerequisites

- Python 3.11
- pyenv (recommended for Python version management)
- Git configured with SSH access
- SSH key for GitHub authentication
- OpenAI API key

## Installation

1. Set up Python environment:

## Install Python 3.11 using pyenv

```bash
pyenv install 3.11
pyenv local 3.11
pyenv versions
eval "$(pyenv init -)"
````

## Verify Python version

python --version

## Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate\n

2. Install dependencies:
```bash
pip install -r requirements.txt
```


3. Configure environment:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Ensure your SSH key is properly set up at `~/.ssh/id_rsa`

## Usage

Run the script by providing a GitHub repository URL as an argument:

```bash
python minimal.py git@github.com:user/repo.git
```


The script will:
1. Clone the repository
2. Analyze the `js/main.js` file
3. Compare the implementation against the requirements
4. Provide a verdict (PASS/FAIL/UNCERTAIN)

## Requirements Being Evaluated

The tool evaluates two JavaScript exercises:

1. Exercise "Bat":
   - Change the color of all h1 headers to red when clicking a button

2. Exercise "Bi":
   - Change the text of h2 headers to show "goiburu2-1", "goiburu2-2", etc. when clicking a button

## Error Handling

- The script will exit if no GitHub URL is provided
- It will automatically fail submissions that don't use github.com domain
- SSH authentication errors will be reported if SSH key is not properly configured

## License

[Add your license information here]