import csv
import datetime as dt
import logging

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT, ERROR_TEXT
from pep_parse.items import PepParseItem
from pep_parse.spiders.pep import PepSpider


class PepParsePipeline:
    """
    When the spider starts, it creates a dictionary with statuses,
    processes Items objects, and at the end creates a file in which
    it outputs a summary of statuses.
    """
    def open_spider(self, spider: PepSpider) -> None:
        """
        When the spider starts, it creates an empty dictionary
        for pep statuses.
        """
        self.peps_statuses = {}

    def process_item(self,
                     item: PepParseItem,
                     spider: PepSpider) -> PepParseItem:
        """
        Processes each Item objects. Saves the pep statuses
        and their number to the dictionary.
        """
        self.peps_statuses[
            item['status']
        ] = self.peps_statuses.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider: PepSpider) -> None:
        """
        Creates a .csv file in which it places a summary
        of statuses from the dictionary.
        """
        total_peps = sum(self.peps_statuses.values())
        pep_rows = [
            (status,
             quantity) for status, quantity in self.peps_statuses.items()
        ]
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formated = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formated}.csv'
        file_path = results_dir / file_name
        try:
            with open(file_path, 'w', encoding='utf-8') as csvfile:
                pepwriter = csv.writer(csvfile, dialect='unix')
                pepwriter.writerow(('Статус', 'Количество'),)
                pepwriter.writerows(pep_rows)
                pepwriter.writerow(('Total', f'{total_peps}'),)
            logging.info(f'The results file has been saved: {file_path}')
        except OSError as error:
            logging.error(ERROR_TEXT, error)
            exit()
        except csv.Error as error:
            logging.error(ERROR_TEXT, error)
            exit()
        except Exception as error:
            logging.error(ERROR_TEXT, error)
            exit()
