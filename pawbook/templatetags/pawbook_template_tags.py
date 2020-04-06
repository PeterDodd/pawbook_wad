from django import template
from pawbook.models import PetPedia

register = template.Library()

@register.inclusion_tag('pawbook/modules/PetInfoPanel.html')
def get_pet_info_links():
    return {"allPosts": PetPedia.objects.all()}
