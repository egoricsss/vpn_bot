import gettext
from typing import Callable

LANGUAGES = ["ru", "en"]

_translations = {
    lang: gettext.translation(
        "messages", localedir="translations", languages=[lang])
    for lang in LANGUAGES
}

def get_translator(lang: str) -> Callable[[str], str]:
    if lang != "ru":
        return _translations.get("en", _translations["en"]).gettext
    return _translations.get("ru", _translations["en"]).gettext
