import os
import gettext

from fastapi.templating import Jinja2Templates
from babel.support import Translations

from app.core.config import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TRANSLATIONS_DIR = os.path.join(BASE_DIR, "translations")

LANGUAGES = settings.SUPPORTED_LOCALE
translations = {
    lang: gettext.translation(
        domain="messages",
        localedir=TRANSLATIONS_DIR,
        languages=[lang],
        fallback=True
    )
    for lang in LANGUAGES
}

def get_translator(lang: str) -> gettext.NullTranslations:
    """A function instance that is passed to an html template that uses Jinja2"""
    return translations.get(lang, translations["en"])

#Singleton for working with templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)