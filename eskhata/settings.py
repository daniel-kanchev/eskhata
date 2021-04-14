BOT_NAME = 'eskhata'
SPIDER_MODULES = ['eskhata.spiders']
NEWSPIDER_MODULE = 'eskhata.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
    'eskhata.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'
DOWNLOAD_DELAY = 1
LOG_LEVEL = 'WARNING'

# LOG_LEVEL = 'DEBUG'
