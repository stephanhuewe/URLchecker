
# URLchecker

URLchecker is a tool for verifying the functionality of URL filtering.  URLchecker sends http GET requests to a target list of websites and sees if the target webserver properly responds.  This can be useful for determing what sites URL web filtering is actually blocking for end users browsers.

## Usage

**-s** List of websites to test against.  Must be one URL per line.  
**-o** Output file in CSV format

The repository includes a lsit of the top 1000 websites from alexa to test against.

Example:
```
./urlchecker.py -s top-1000-sites.txt -o output.csv
```

## Dependencies
Requests Library [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
pip install --upgrade requests
pip install --upgrade ndg-httpsclient
```