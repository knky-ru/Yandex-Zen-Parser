# KNKY > Yandex-Zen-Parser
Python 3 script for parsing pages from the Yandex.Zen service. Script use BeautifulSoup library for HTML-parsing.

Yandex-Zen-Parser download images and return pure HTML-file without any class or style attributes.

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

## Output HTML and images
Files will be stored in the appropriate folders. Jpeg images are stored right there.
```
./output/
--------/article-alias/
----------------------/article-alias-1.jpg
----------------------/article-alias-2.jpg
----------------------/article-alias-3.jpg
----------------------/article-alias-4.jpg
----------------------/article-alias.html
--------/another-article-alias/
...
```

## Start parsing
Execute script in command line.
```
python ZenParser.py
```

## This project can be improved
This script is provided as is. If you have noticed bugs or can offer an improvement, then welcome!

## KNKY.RU
Please visit our website for more information [KNKY.RU](https://knky.ru/)
