"02.01.2023 17:02:58 - [INFO] - Scrapy 2.7.0 started (bot: pep_parse)"
"02.01.2023 17:02:58 - [INFO] - Versions: lxml 4.8.0.0, libxml2 2.9.12, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 22.2.0, Python 3.7.16 (default, Dec  7 2022, 01:12:33) - [GCC 11.3.0], pyOpenSSL 22.0.0 (OpenSSL 1.1.1n  15 Mar 2022), cryptography 36.0.2, Platform Linux-5.15.0-56-generic-x86_64-with-Ubuntu-22.04-jammy"
"02.01.2023 17:02:58 - [INFO] - Overridden settings:
{'BOT_NAME': 'pep_parse',
 'LOG_DATEFORMAT': '%d.%m.%Y %H:%M:%S',
 'LOG_FILE': 'logs/logs.py',
 'LOG_FORMAT': '"%(asctime)s - [%(levelname)s] - %(message)s"',
 'LOG_LEVEL': 20,
 'NEWSPIDER_MODULE': 'pep_parse.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['pep_parse.spiders']}"
"02.01.2023 17:02:58 - [WARNING] - /home/sergey/Dev/scrapy_parser_pep/venv/lib/python3.7/site-packages/scrapy/utils/request.py:231: ScrapyDeprecationWarning: '2.6' is a deprecated value for the 'REQUEST_FINGERPRINTER_IMPLEMENTATION' setting.

It is also the default value. In other words, it is normal to get this warning if you have not defined a value for the 'REQUEST_FINGERPRINTER_IMPLEMENTATION' setting. This is so for backward compatibility reasons, but it will change in a future version of Scrapy.

See the documentation of the 'REQUEST_FINGERPRINTER_IMPLEMENTATION' setting for information on how to handle this deprecation.
  return cls(crawler)
"
"02.01.2023 17:02:58 - [INFO] - Telnet Password: 721530edc38e5bd2"
"02.01.2023 17:02:58 - [INFO] - Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']"
"02.01.2023 17:02:58 - [INFO] - Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']"
"02.01.2023 17:02:58 - [INFO] - Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']"
"02.01.2023 17:02:58 - [INFO] - Enabled item pipelines:
['pep_parse.pipelines.PepParsePipeline']"
"02.01.2023 17:02:58 - [INFO] - Spider opened"
"02.01.2023 17:02:58 - [INFO] - Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)"
"02.01.2023 17:02:58 - [INFO] - Telnet console listening on 127.0.0.1:6023"
"02.01.2023 17:03:28 - [INFO] - Closing spider (finished)"
"02.01.2023 17:03:28 - [INFO] - The results file has been saved: /home/sergey/Dev/scrapy_parser_pep/results/status_summary_2023-01-02_17-03-28.csv"
"02.01.2023 17:03:28 - [INFO] - Stored csv feed (601 items) in: results/pep_2023-01-02T14-02-58.csv"
"02.01.2023 17:03:28 - [INFO] - Dumping Scrapy stats:
{'downloader/request_bytes': 311157,
 'downloader/request_count': 1204,
 'downloader/request_method_count/GET': 1204,
 'downloader/response_bytes': 7047366,
 'downloader/response_count': 1204,
 'downloader/response_status_count/200': 602,
 'downloader/response_status_count/301': 601,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 30.708477,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 1, 2, 14, 3, 28, 950919),
 'httpcompression/response_bytes': 27290728,
 'httpcompression/response_count': 603,
 'item_scraped_count': 601,
 'log_count/INFO': 12,
 'log_count/WARNING': 1,
 'memusage/max': 63348736,
 'memusage/startup': 63348736,
 'request_depth_max': 1,
 'response_received_count': 603,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1203,
 'scheduler/dequeued/memory': 1203,
 'scheduler/enqueued': 1203,
 'scheduler/enqueued/memory': 1203,
 'start_time': datetime.datetime(2023, 1, 2, 14, 2, 58, 242442)}"
"02.01.2023 17:03:28 - [INFO] - Spider closed (finished)"
