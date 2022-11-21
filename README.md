# SharkTank

## Create a virtual environment 
> make sure you present in SharkTank main directory and execute the following commands
```
$ python3 -m venv venv

$  source venv/bin/activate

$  pip3 install -r requirement.txt 

```

## Now run the server
```
$ uvicorn main:app --reload
```

You can interact with APIs using swagger UI 

```
http://127.0.0.1:8000/docs
```


