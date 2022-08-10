# cgan-fastapi

Generate new image based on rock_paper_scissors [dataset|https://www.tensorflow.org/datasets/catalog/rock_paper_scissors]

## prerequisite

* Install torch, torchvision, matplotlib

* ```pip install -r requirements.txt```


## Run Project

```uvicorn main:app --reload --port 8001```

Each request which conforms graphQL conventions generate 24 new images on the project directory and return its path. 

## Samples

![sample 1](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077723.132387.png)

![sample 2](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077722.580476.png)

![sample 3](https://github.com/moghadas76/cgan-fastapi/blob/main/1660077722.10165.png)
