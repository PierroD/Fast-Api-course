from app.utils.env_util import get_url_from_env
from fastapi import HTTPException
from fastapi.responses import FileResponse, RedirectResponse


def get_env_url():
    return get_url_from_env()


def get_image_file():
    return FileResponse("./project_files/app/assets/minions.jpg")


def redirect_url():
    try:
        return RedirectResponse(get_url_from_env())
    except:
        raise HTTPException(
            status_code=500, detail="Not able to load url from .env")
