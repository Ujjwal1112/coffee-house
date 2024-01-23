from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def get_url_from_file(request, file):
    file_name = file.name
    file_content = ContentFile(file.read())
    file_path = default_storage.save(f"static/images/Profile Pictures/{file_name}", file_content)
    url = request.build_absolute_uri(f'{file_path}')
    return url