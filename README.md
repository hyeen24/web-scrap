## Introduction

This is a simple web scrapping project to scrap top 100 song and artist from https://www.billboard.com/charts/hot-100/

## Installation

1. Install scrapy
```bash
pip install scrapy
```
2. Create file directory for scrapy project
```bash
scrapy startproject <project-name>
```
3. cd into project folder
4. copy and paste the python file into your spiders folder.
5.   run the file with scrapy crawl
```bash
scrapy crawl <filename> -o top100.csv
```



