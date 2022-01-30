import io
from PIL import Image


def generate_photo(image_name, size=(100, 100)):
    """
    Returns an image file. Currently supports png
    :image_name:
    :param ext:
    :param size:
    :returns:
    """
    splitted = image_name.split(".")
    name = image_name
    ext = "png"
    if len(splitted) > 1:
        name = splitted[:-1]
        ext = splitted[-1]

    assert ext == "png", f"File extension: {ext} not supported"
    file_instance = io.BytesIO()
    image = Image.new("RGBA", size=size, color=(0, 0, 0))
    image.save(file_instance, ext)
    file_instance.name = name
    file_instance.seek(0)

    return file_instance
