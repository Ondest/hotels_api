from pathlib import Path

from PIL import Image

from src.tasks.celery import celery


@celery.task
def picture_process(
    path: str,
):
    image_path = Path(path)
    image = Image.open(image_path)
    image_res_800_400 = image.resize((800, 400))
    image_res_300_150 = image.resize((300, 150))
    image_res_800_400.save(f"src/static/images/800_400_{image_path.name}")
    image_res_300_150.save(f"src/static/images/300_150_{image_path.name}")
