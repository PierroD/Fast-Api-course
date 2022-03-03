from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.user_controller import user_controller
from app.controllers.other_controller import other_controller
import uvicorn

"""
    Fast API
"""
# create a FastAPI instance
app = FastAPI(
    title="PierroD - Advanced course",
    description=("Learn Fast API"),
    version="1.0.0",
    redoc_url="/swagger",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    # you can allow some routes / but here we are allowing all the existing routes
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller)
app.include_router(other_controller)

"""
    API endpoints
"""


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=4000, reload=True)
