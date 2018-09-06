from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from viruses.models import Virus
from pytz import UTC

DATETIME_FORMAT = '%Y-%m-%d'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from virus_data.csv into our viruses model"
    
    def handle(self, *args, **options):
        if Virus.objects.exists():
            print('Virus data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading virus data for analysis")
        for row in DictReader(open('./virus_data.csv')):
            data = Virus()
            data.order = row['order']
            data.family = row['family']
            data.subfamily = row['subfamily']
            data.genus = row['genus']
            data.species = row['species']
            data.genome = row['genome']
            data.host = row['host']
            data.nucleotides = row['sequence_name']
        
            raw_submission_date = row['submission_date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            data.submission_date = submission_date
            data.save()
        print("virus data finished loading")

