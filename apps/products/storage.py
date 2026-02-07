from pathlib import Path
import uuid


def product_image_path(instance, filename):
    ext = Path(filename).suffix  # ".jpg", ".png"
    new_filename = f"{uuid.uuid4()}{ext}"
    return f"products/images/{instance.product.id}/{new_filename}"