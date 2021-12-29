
from django.core.management.base import BaseCommand



# this must be named 'Command'
# otherwise its not going to work
class Command(BaseCommand):
    help = "with this management tool you can manage the projects' REST API"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("first", type=str)
        # Positional arguments
        parser.add_argument("second", type=str)

        # Named (optional) arguments
        parser.add_argument(
            "--third",
            help="something interesting about third",
            default="something intersting avbout third")


    def handle(self, *args, **options):
        print(args)
        print(options)
        print("hello from rest api aka /api django app")

        print(options["first"])
        print(options["second"])
        print(options["third"])


    # doesnt work
    def test(self, *args, **options):
        print(args)
        print(options)
        print("just handled test")

# actually this is run before the class runs
print("command runned after class def")