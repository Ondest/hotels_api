from shutil import copyfileobj

from fastapi import APIRouter, File, UploadFile


router = APIRouter(prefix="/images", tags=["Images"])


@router.post("/hotels")
async def add_hotel_image(image_id: int, file: UploadFile = File(...)):
    with open(f"api_practice/static/{image_id}.webp", "wb+") as file_object:
        copyfileobj(file.file, file_object)
    return {"status_code": 201}
