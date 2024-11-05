from django.core.management.base import BaseCommand
from django.templatetags.static import static
import pokebase as pb
from home.models import Berry


class Command(BaseCommand):
    help = "Loads data from pokabase API to the Database."

    def handle(self, *args, **kwargs) -> str | None:
        id = 1
        while id < 65:
            data = pb.berry(id)
            berry, _ = Berry.objects.update_or_create(
                id = data.id,
                name = data.name,
                size = data.size,
                smoothness = data.smoothness,
                soil_dryness = data.soil_dryness,
                growth_time = data.growth_time,
                max_harvest = data.max_harvest,
                image = static(f'images/berries/{data.name}-berry.png')
            )
            id += 1
            print(f'SAVED {data.name}-berry...')
        