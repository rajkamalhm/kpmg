## Requirement

Python command line tool that optionally takes a count as an argument and lists the top 20 (or specified count) stories from Hacker News. An example output could be:

./get_top_20_articles.py
 1. <title 1> <url 1>
 2. <title 2> <url 2>  
 ......
 20. <title 20> <url 20>

## Usage  
```python3 get_top_20_articles.py```

## CLI Help  
```
python3 get_top_20_articles.py --help
usage: get_top_20_articles.py [-h] [-c COUNT]

Tool to get the top 20 stories from Hacker News.

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Number of top stories to fetch from Hacker News. (default: 20)
```
## Sample Outputs  
```
python3 get_top_20_articles.py -c 7
No.       Title                                             URL
--        -----                                             ---
1         What to do when you 've ruined your life          https://www.bigfeels.club/public-articles/what-to-do-when-youve-ruined-your-life
2         Direct Memory Access computing machine RP2040     https://people.ece.cornell.edu/land/courses/ece4760/RP2040/C_SDK_DMA_machine/DMA_machine_rp2040.html
3         A Dump of the Raw Stadia Controller BT Firmware   https://github.com/Scyne/stadiaRawBtFw
4         An unexpected benefit of unit tests               https://matthewc.dev/musings/unit-tests/
5         GNU Octave                                        https://octave.org/index
6         A page with no code                               https://danq.me/2023/01/11/nocode/
7         Capital One axes 1k tech roles                    https://www.theregister.com/2023/01/20/capital_one/
```

## Notes
* pylint and autopep8 were used for code analysis and formatting
* Code was written based on KISS principle. It should be modularized if new features are added
* Placeholder files and directories were created for tests, exceptions and packaging. They can be filled with relevant data if required