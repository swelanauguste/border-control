from django.core.management.base import BaseCommand

from ...models import Location

class Command(BaseCommand):
    help = "Add locations to the database"
    
    def handle(self, *args, **options):
        Location.objects.get_or_create(l_name="Port Castries")
        Location.objects.get_or_create(l_name="Port Vieux Fort")
        Location.objects.get_or_create(l_name="Rodney Bay Marine")
        Location.objects.get_or_create(l_name="Port Soufriere")
        Location.objects.get_or_create(l_name="Hewanorra International")
        Location.objects.get_or_create(l_name="George FL Charles")
        self.stdout.write(self.style.SUCCESS("Locations added"))
        