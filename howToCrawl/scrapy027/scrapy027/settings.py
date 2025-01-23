# Scrapy settings for scrapy027 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy027"

SPIDER_MODULES = ["scrapy027.spiders"]
NEWSPIDER_MODULE = "scrapy027.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Cookie':
        'Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1728383832; Hm_lvt_0113b461c3b631f7a56'
        '8630be1134d3d=1728094519,1728372609; Hm_lpvt_8e745928b4c636da693d2c43470f541'
        '3=1728383832; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1728383832; Hm_lvt_8e'
        '745928b4c636da693d2c43470f5413=1728094519,1728372609; Hm_lvt_93b4a7c2e07353c3'
        '853ac17a86d4c8a4=1728094519,1728372609; __51uvsct__KSHU1VNqce379XHB=3; __51vc'
        'ke__KSHU1VNqce379XHB=dbacdb84-fb29-58df-a417-2712113f89f1; __51vuft__KSHU1VNq'
        'ce379XHB=1728094518801; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22efae3'
        'ce0-bf96-526b-a81b-492f48f4d7d5%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%20'
        '0%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201728385597236%2C%20%22ct%22%3'
        'A%201728383797236%7D; HMACCOUNT=1EA4498744E0CEC0',
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
        '(KHTML, like Gecko) Version/18.0.1 Safari/605.1.15',
    'Host': 'www.dytt89.com'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy027.middlewares.Scrapy027SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy027.middlewares.Scrapy027DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "scrapy027.pipelines.Scrapy027Pipeline": 300,
    "scrapy027.pipelines.DownloadImages": 500
}

# LOG_LEVEL = 'WARNING'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
