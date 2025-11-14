"""
Django signals for automatic processing

Handles automatic thumbnail generation for gallery images
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os

from .models import GalleryItem


@receiver(post_save, sender=GalleryItem)
def create_thumbnail(sender, instance, created, **kwargs):
    """
    Automatically generate thumbnail for gallery items

    Creates a 400x400px thumbnail if one doesn't exist
    Triggered after GalleryItem is saved
    """
    # Only generate if main image exists and no thumbnail
    if instance.image and not instance.thumbnail:
        try:
            # Open the image
            img = Image.open(instance.image.path)

            # Convert RGBA to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create a white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

            # Calculate thumbnail size (400x400 max, maintain aspect ratio)
            img.thumbnail((400, 400), Image.Resampling.LANCZOS)

            # Save thumbnail to BytesIO
            thumb_io = BytesIO()
            img_format = 'JPEG'

            # Save with optimization
            img.save(thumb_io, format=img_format, quality=85, optimize=True)
            thumb_io.seek(0)

            # Generate thumbnail filename
            original_name = os.path.basename(instance.image.name)
            name_without_ext = os.path.splitext(original_name)[0]
            thumb_filename = f"{name_without_ext}_thumb.jpg"

            # Create InMemoryUploadedFile
            thumb_file = InMemoryUploadedFile(
                thumb_io,
                None,
                thumb_filename,
                'image/jpeg',
                sys.getsizeof(thumb_io),
                None
            )

            # Save thumbnail to model
            # Use update to avoid triggering signal again
            instance.thumbnail.save(thumb_filename, thumb_file, save=False)
            GalleryItem.objects.filter(pk=instance.pk).update(thumbnail=instance.thumbnail)

            print(f"✓ Thumbnail generated for: {instance.title}")

        except Exception as e:
            print(f"✗ Error generating thumbnail for {instance.title}: {str(e)}")
