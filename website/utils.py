from .models import Tag

def create_tag_list(tag_str_list):
    tag_list = []
    for tag_str in tag_str_list.split(','):
        tag_str = tag_str.strip().lower()
        try:
            tag = Tag.objects.get(title__iexact=tag_str)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(title=tag_str)
        tag_list.append(tag)
    return tag_list

def create_tag_str_list(tag_list):
    tag_str_list = []
    for tag in tag_list:
        tag_str_list.append(tag.title)
    return ', '.join(tag_str_list)
