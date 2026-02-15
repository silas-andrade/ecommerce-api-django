from pathlib import Path
import uuid


def product_media_path(instance, filename):
    ext = Path(filename).suffix  # ".jpg", ".png"
    new_filename = f"{uuid.uuid4()}{ext}"
    return f"products/{instance.product.id}/{new_filename}"
