from shutil import copyfileobj

from fastapi import APIRouter, File, UploadFile

from src.tasks.tasks import picture_process


router = APIRouter(prefix="/images", tags=["Images"])


@router.post("/hotels")
async def add_hotel_image(image_id: int, file: UploadFile = File(...)):
    image_path = f"src/static/images/{image_id}.webp"
    with open(image_path, "wb+") as file_object:
        copyfileobj(file.file, file_object)
    picture_process.delay(image_path)
