from pathlib import Path
import uuid

def customer_profile_image_path(instance, filename):
    ext = Path(filename).suffix
    filename = f"{uuid.uuid4()}{ext}"
    return f"profiles/customers/profile_images/{instance.user.id}/{filename}"

def seller_profile_image_path(instance, filename):
    ext = Path(filename).suffix
    filename = f"{uuid.uuid4()}{ext}"
    return f"profiles/sellers/profile_images/{instance.user.id}/{filename}"

def seller_cover_image_path(instance, filename):
    ext = Path(filename).suffix
    filename = f"{uuid.uuid4()}{ext}"
    return f"profiles/sellers/cover_images/{instance.user.id}/{filename}"