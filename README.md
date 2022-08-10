# cgan-fastapi

Generate new image based on rock_paper_scissors [dataset|https://www.tensorflow.org/datasets/catalog/rock_paper_scissors]

## prerequisite

* Install torch, torchvision, matplotlib

* ```pip install -r requirements.txt```


## Run Project

```uvicorn main:app --reload --port 8001```

Each request which conforms graphQL conventions generate 24 new images on the project directory and return its path. 

## Samples

![Tux, the Linux mascot](/assets/images/tux.png)
