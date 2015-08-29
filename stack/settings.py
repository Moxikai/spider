# -*- coding: utf-8 -*-

# Scrapy settings for stack project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'stack'

SPIDER_MODULES = ['stack.spiders']
NEWSPIDER_MODULE = 'stack.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stack (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'stack.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'stack.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'stack.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'


ITEM_PIPELINES = ['stack.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = '192.168.10.10'
MONGODB_PORT = 27017
MONGODB_DB = 'imooc'
MONGODB_COLLECTION = '0720'

HEADER = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'laracasts.com',
    'Referer':'https://laracasts.com/all',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
}

COOKIES = {
    'remember_82e5d2c56bdd0811318f0cf078b78bfc':'eyJpdiI6ImtUb0RabG0zcENLOThUdkNOeUg3dHc9PSIsInZhbHVlIjoieTZDWkdqSnNhcWtEUVQ2WDBNZXMyUkFyWnR0MXdRKzZTdnZ3R0xER1VFQVJIVnJ1dW5lSStyNDVKS0JINXNPTWdXXC9lMnV4VFZCNTQ0d21JNzdXaGhQYUVJU0xHeHpteG9CdFkwb3Z6K093PSIsIm1hYyI6IjM1ZDZmNmRkNTk4YWU2MTA3MWU5N2UyYTI0MWY1YTE2OTAwOWVkNjNjOGQ1YzVkYjhmNGJkNDA0YmVkNjQ1NTkifQ%3D%3D',
    '_gat':1,
    'laravel_session':'eyJpdiI6IjZvTVwvTmdLcUtcLzBGNElrR3JqR3Uzdz09IiwidmFsdWUiOiJYdXJrdDFBNEIrblJ6WnN3WjJrMmlDNDZBNVluSFZhRk9neEwrOEorT1V2TjVOSENmaU5PNXVlemp0cyttTk11cEE5cG5oVlBCeXFqcnUxeVpPSURQdz09IiwibWFjIjoiNjBmYWY0ZDA3YmMxZDUxZDZkYmYzOTRlMzJjZDRhZTA3OTNhYTUyM2RhYWVlMzBjMWQ1ZDNhM2Q4YTg3N2I5ZiJ9',
    '_ga':'GA1.2.466984329.1433516828'
}

DOWNLOAD_DELAY = 5