from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PostTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Post, PostTranslationOptions)