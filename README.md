# Fast-Api-course | Confirm

## Summary

1. Add file CORS
2. Return file
3. Redirect url
4. Exclude data from Response such a `password`
5. Better `JsonResponse` & `Exceptions`
6. Load data from `.env` and return them

## Introduction

Now that you passed the beginner course, it's time to add perfect a bit our code.

You will see in this course :

- Add file CORS
- Return file
- Redirect url
- Exclude data from Response such a `password`
- Better `JsonResponse` & `Exceptions`
- Load data from `.env` and return them

## Add file CORS

In the future you might need to work, with files (sending, receiving, analyzing, etc...)

So you have to enable the CORS in the middleware

import CORS middleware like bellow

```py
from fastapi.middleware.cors import CORSMiddleware
```

add the middleware to your instance

```py
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"], # you can allow some routes / but here we are allowing all the existing routes
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Return file

Now we will create an API endpoint that return a file

We have downloaded the minions picture from the images folder
![](images/minions.jpg)

To return it we have to use FastAPI `FileResponse`

```py
from fastapi.responses import FileResponse
```

Now we are creating the endpoint

```py
# return an image
@app.get("/image")
def get_image():
    return FileResponse("../images/minions.jpg")
```

## Redirect URL

Now you will learn how to redirect an existing URL

import file RedirectResponse

```py
from fastapi.responses import RedirectResponse
```

Create the endpoint to redirect the user to the page

```py
@app.get("/url")
def get_my_url():
    return RedirectResponse("https://resize-parismatch.lanmedia.fr/img/var/news/storage/images/paris-match/actu/insolite/quand-un-minion-sauve-la-vie-d-une-fillette-aux-etats-unis-803112/8490396-1-fre-FR/Quand-un-Minion-sauve-la-vie-d-une-fillette.jpg")
```

## Exclude data from Response such a `password`

As you seen in the beginner course, when we called `/user/{id}`
we were returning all the infos of the user including the password, but we want to avoid returning some sensitive infos at some points

To do that you have to create 2 models one `In` and one `Out`

- `In` is the model of data sent to the api
- `Out` is the model of data the api sent to the front

```py
class UserIn(BaseModel):
    id: int
    name: str
    password: Optional[str] = None

class UserOut(BaseModel):
    id: int
    name: str
```

Now you can modify the endpoints so they can return user without the password

```py
@app.get("/user/{id}", response_model=UserOut)
def get_user(id: int):
```

The response should look like below :

```json
{
  "id": 1,
  "name": "user1"
}
```

## Better `JsonResponse` & `Exceptions`

As you already know with `FastAPI` you can return python object directly, but there is many way to format the response into json, using `JSONResponse`, `ORJSONResponse` or `UJSONResponse`

You can also throw exception using `HTTPException`

Exemple below :

```py
@app.delete("/user/{id}")
def delete_user(id: int):
    if(users[id] is None):
        raise HTTPException(
            status_code=400, detail=f'Impossible to delete User with id : {id} not found')
    users.pop(id)
    return JSONResponse(status_code=200, content={"isDeleted": True})
```

You can now try to modify the file from the beginner course, and all we seen above

## Load data from `.env` and return them

Some data should be stored inside your code, like access to a database or to external services like API's keys, database key, externals storage access.

It's important to store them inside a `.env` file. This file shouldn't be pushed on git (I did it so you can see how it looks), so add it to your `.gitignore`

Create a `.env` file at the root of the folder

We will do an endpoints, so we will return an url which is stored in that `.env` file

```env

MY_URL=https://resize-parismatch.lanmedia.fr/img/var/news/storage/images/paris-match/actu/insolite/quand-un-minion-sauve-la-vie-d-une-fillette-aux-etats-unis-803112/8490396-1-fre-FR/Quand-un-Minion-sauve-la-vie-d-une-fillette.jpg
```

Import `os` so we could load the data stored in the local environment

```py
import os
```

The endpoint should look like this :

```py
@app.get("/url")
def get_url():
    try:
        print(os.getenv("MY_URL"))
        return RedirectResponse(os.getenv("MY_URL"))
    except:
        raise HTTPException(
            status_code=500, detail="Not able to load url from .env")

```

To run your project with your environment you can run the command below

```
 uvicorn main:app --env-file=".env" --port=4000
```
