# Gherkin_tables_styler
a very simple python script convert the ugly unintended tables into pretty ones 

Example :

it converts the unformated tables from your feature file like this  
```
|id|secure key|processing|
|1|11| 2% |
| 2 |22| 3% |
```
into pretty one like this :

```
| id | secure key | processing |
| 1  | 11         | 2%         |
| 2  | 22         | 3%         |
```

no matter how many tables in the file, it can prettify them all
