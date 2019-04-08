# KNKY > Yandex-Zen-Parser
Python 3 script for parsing pages from the Yandex.Zen service. Script use BeautifulSoup library for HTML-parsing.

## Valid tags
Parse only Articles with text and images ['p', 'h2', 'h3', 'img']. Video tags  are not supported yet.

## Input urls
Put input.json into script roor folder.

### input.json structure
```javascript
{
  "urls": [
    "https://zen.yandex.ru/...",
    "https://zen.yandex.ru/...",
    "https://zen.yandex.ru/..."
  ]
}
```
## Start parsing
Execute script in command line.
```
python ZenParser.py
```

## This project can be improved
This script is provided as is. If you have noticed bugs or can offer an improvement, then welcome!

## KNKY.RU
Please visit our site for more information [KNKY.RU](https://knky.ru/)
