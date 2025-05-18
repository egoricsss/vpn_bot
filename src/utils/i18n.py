import gettext

LANGUAGES = ["ru", "en"]

_translations = {
    lang: gettext.translation(
        "messages", localedir="translations", languages=[lang])
    for lang in LANGUAGES
}


def get_translator(lang: str):
    try:
        return gettext.translation("messages", localedir="translations", languages=[lang])
    except FileNotFoundError:
        return gettext.translation("messages", localedir="translations", languages=["en"])


_ = lambda s: s


def set_language(lang: str):
    global _
    _ = get_translator(lang)
