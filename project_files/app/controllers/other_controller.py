from fastapi import APIRouter
from app.services.other_service import get_env_url, get_image_file, redirect_url


other_controller = APIRouter(
    prefix="/other",
    tags=["other-api-calls"]
)

# return from .env


@other_controller.get("/fromEnv")
def get_from_env():
    return get_env_url()

# return an image


@other_controller.get("/image")
def get_image():
    return get_image_file()


# redirect url
@other_controller.get("/url")
def get_url():
    return redirect_url()
