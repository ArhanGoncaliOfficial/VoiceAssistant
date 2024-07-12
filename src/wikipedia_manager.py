import wikipedia

"""

[ UNDER CONSTRUCTION ]

"""

class WikipediaManager:
    def __init__(self, language:str, sentence_limit:int) -> None:
        self.language = language
        self.sentence_limit = sentence_limit

    def search_wiki(self, keyword:str) -> str:
        wikipedia.set_lang(self.language)
        return wikipedia.summary(f'{keyword}', sentences=self.sentence_limit)