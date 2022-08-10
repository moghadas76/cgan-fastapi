# cgan-fastapi

Generate new image based on rock_paper_scissors [dataset|https://www.tensorflow.org/datasets/catalog/rock_paper_scissors]

## prerequisite

* Install torch, torchvision, matplotlib

* ```pip install -r requirements.txt```


## Run Project

```uvicorn main:app --reload --port 8001```

Each request which conforms graphQL conventions generate 24 new images on the project directory and return its path. 


## GraphQL Request sampel

```bash
curl 'http://127.0.0.1:8001/graphql' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Origin: http://127.0.0.1:8001' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: http://127.0.0.1:8001/graphql' \
  -H 'Accept-Language: en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7' \
  --data-raw '{"query":"# Welcome to GraphiQL\n#\n# GraphiQL is an in-browser tool for writing, validating, and\n# testing GraphQL queries.\n#\n# Type queries into this side of the screen, and you will see intelligent\n# typeaheads aware of the current GraphQL type schema and live syntax and\n# validation errors highlighted within the text.\n#\n# GraphQL queries typically start with a \"{\" character. Lines that starts\n# with a # are ignored.\n#\n# An example GraphQL query might look like:\n#\n#     {\n#       field(arg: \"value\") {\n#         subField\n#       }\n#     }\n#\n# Keyboard shortcuts:\n#\n#  Prettify Query:  Shift-Ctrl-P (or press the prettify button above)\n#\n#     Merge Query:  Shift-Ctrl-M (or press the merge button above)\n#\n#       Run Query:  Ctrl-Enter (or press the play button above)\n#\n#   Auto Complete:  Ctrl-Space (or just start typing)\n#\nmutation\n{\n  generateClassPhoto(imageCls: {classNumber:1}){\n    path\n  }\n}","variables":null}' \
  --compressed
```

## Samples

![sample 1](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077723.132387.png)

![sample 2](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077722.580476.png)

![sample 3](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077722.10165.png)
