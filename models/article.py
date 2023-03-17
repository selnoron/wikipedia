import datetime


class Article:
    """Create/Update Article."""

    def __init__(
        self,
        user_name: str,
        genre: str,
        title: str,
        text_content: str
    ) -> None:
        self.user_name = user_name
        self.genre = genre
        self.title = title
        self.text_content = text_content
        self.time = datetime.datetime.now()

    @staticmethod
    def create(
        user_name: str,
        genre: str,
        title: str,
        text_content: str
    ) -> 'Article':
        artic: 'Article' = Article(
            user_name=user_name,
            genre=genre,
            title=title,
            text_content=text_content
        )
        return artic
    
    @staticmethod
    def update(
        user_name: str,
        text_content: str,
        article: 'Article'
    ) -> 'Article':
        artic: 'Article' = Article(
            user_name=user_name,
            genre=article.genre,
            title=article.title,
            text_content=text_content
        )
        return artic