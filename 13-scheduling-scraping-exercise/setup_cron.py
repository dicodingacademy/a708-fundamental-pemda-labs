from crontab import CronTab 

cron = CronTab(user=True)
job = cron.new(command='<Absolute Path Python binary dalam virtual environment> <Absolut path lokasi intermediate_scraping.py>', comment='Scraping bookstoscrape')
job.minute.every(3)

cron.write()
print('Scraping data sudah dijadwalkan.')
