import csv
import datetime as dt
import logging

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        logging.info('Open spider ++++++++++++++++++++++++')
        self.peps_statuses = {}

    def process_item(self, item, spider):
        self.peps_statuses[item['status']] = self.peps_statuses.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        logging.info('Close spider +++++++++++++++++')
        total_peps = sum(self.peps_statuses.values())
        pep_rows = [(status, quantity) for status, quantity in self.peps_statuses.items()]
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
        except OSError as error:
            pass
        except csv.Error as error:
            pass
        except Exception as error:
            pass
