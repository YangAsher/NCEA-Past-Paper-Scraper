requirements:

- git
- python
- requests
- colorama
- room temperature iq

# usage

### subject name

![image](https://user-images.githubusercontent.com/117716531/201019214-4c44fa7f-59e9-4d82-ba35-ceeb2ff28201.png)

type in subject name, this is the big folder the papers will be saved under

### AS number

![image](https://user-images.githubusercontent.com/117716531/201019385-99358968-d04f-478c-97c2-a13ac5a770f8.png)

type in the AS number to download the papers of. you can download NCEA L1, L2, L3 or scholarship papers

![image](https://user-images.githubusercontent.com/117716531/201019585-572c5fee-e294-41a2-8da1-841936d8cb76.png)


# to run from src:

## install prerequisites as follows:

- open cmd

- if you do not have git:

`curl https://github.com/git-for-windows/git/releases/download/v2.38.1.windows.1/Git-2.38.1-64-bit.exe -o git.exe && git.exe` and follow the prompts

- download the code

`git clone https://github.com/YangAsher/NCEA-Past-Paper-Scraper.git`

- if you do not have python:

`curl https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe -o python.exe && python.exe` and follow the prompts


- if you do not have requests or colorama

`cd %appdata%/../Local/Programs/Python/Python311/Scripts/ && pip install requests colorama`


## to execute:

`cd %appdata%/../../NCEA-Past-Paper-Scraper && scraper.py`

alternatively navigate to user/NCEA-Past-Paper-Scraper and run scraper.py or use the binary i built (bad idea)
