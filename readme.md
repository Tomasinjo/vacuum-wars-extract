
### Vacuum Wars Top 20 extract

The script scrapes the data from [Vacuum Wars Top 20 robots](https://vacuumwars.com/best-vacuum-cleaners/robot-vacuums/) and puts it to Excel file for easier comparison.

Raw export (script output):  
<img src="screenshots/raw_export.png" width="500">

Prettified export (done manually):  
<img src="screenshots/pretty_export.png" width="500">


### Installation

1. Clone this project  
2. Make sure you have Python 3.11 installed
3. Install required packages into venv on Linux:
```sh
python3.11 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Same thing on Windows:
```bat
python -m venv env
call env\Scripts\activate.bat
pip install -r requirements.txt
```
Without venv:
`pip install -r requirements.txt`


### Usage
`python extract_vw.py`

Output Excel file is saved to local directory

