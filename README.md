requirements:

- git
- python
- requests
- colorama
- room temperature iq

# to run from src:

- install prerequisites as follows:

- open cmd

- if you do not have git:

`curl https://github.com/git-for-windows/git/releases/download/v2.38.1.windows.1/Git-2.38.1-64-bit.exe -o git.exe && git.exe` and follow the prompts

- download the code

`git clone https://github.com/YangAsher/NCEA-Past-Paper-Scraper.git`

- if you do not have python:

`curl https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe -o python.exe && python.exe` and follow the prompts


- if you do not have requests or colorama

`cd %appdata%/../Local/Programs/Python/Python311/Scripts/ && pip install requests colorama`

- prereqs installed. this process only needs to occur once

- to execute:

`cd %appdata%/../../NCEA-Past-Paper-Scraper && scraper.py`

alternatively navigate to user/NCEA-Past-Paper-Scraper and run scraper.py or use the binary i built (bad idea)
