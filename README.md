# Nuclear IT Hack - YADRO Case

### Installation
*Built for python 3.14*

* Create a python Virtual Environment;
* Run "pip install -r ./Source/requirements.txt";

### Running

*Run from ".../Nuclear-IT-hack/"*
```bash
streamlit run .\Source\UserInterface\Dashboard.py
```
Launch pytests
```bash
pytest .\Source\Tests\GeneratedTests.py
```

### Bugs found

* Reading from 4th register will not work after writing into 3rd register
* If last two digits in 2nd register are 42 (in hex form), then other digits are nullified 
* 32-bit integer overflow is not processed properly
