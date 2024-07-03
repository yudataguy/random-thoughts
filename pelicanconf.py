AUTHOR = 'Sam Yu'
SITENAME = "Bl◯◯k P◯st"
SITEURL = "https://blkpst.com"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

STATIC_PATHS = ["assets"]

EXTRA_PATH_METADATA = {
    "assets/robots.txt": {"path": "robots.txt"},
    "assets/favicon.ico": {"path": "favicon.ico"},
    "assets/CNAME": {"path": "CNAME"},
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

# Archives
ARCHIVES_URL = "archive/"
ARCHIVES_SAVE_AS = "archive/index.html"

### Plugins

PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    "sitemap",
    "neighbors",
    "assets",
    "post_stats",
]

# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

AUTHOR_META = {
    "samu": {
        "name": "Sam Yu",
        "cover": "https://images.unsplash.com/photo-1531219572328-a0171b4448a3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "image": "assets/images/avatar.jpg",
        "website": "https://blkpst.com/",
        "linkedin": "yusiye",
        "github": "yudataguy",
        "location": "California, USA",
        "bio": "Curious about almost everything.",
    }
}

MENUITEMS = (
    ("Home", "/"),
    ("Tag", "/tag/getting-started/"),
    ("Author", "/author/samu/"),
    ("Category", "/category/examples/"),
    ("Archives", "/2024/07/"),
    ("Plugins", "https://github.com/pelican-plugins"),
)

SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = True
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = False

# CSS_OVERRIDE = ["assets/css/myblog.css"]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = "themes/attila"
