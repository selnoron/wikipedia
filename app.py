#Local
import models.user_setting as user_setting
import models.article as article

# Flask
import flask

app: flask.app.Flask = flask.Flask(__name__)
users: list['user_setting.User'] = []
creating_user: 'article.Article' = None
articles_data: list['article.Article'] = []
genres_artico: list[str] = []

@app.route('/', methods=['GET', 'POST'])
def registration() -> flask.Response:
    if flask.request.method == 'POST':
        data: dict = flask.request.form
        users.append(
            user_setting.User.create(**data, users=users)
        )

    return flask.render_template(
        'regis.html'
    )

@app.route('/auth', methods=['GET', 'POST'])
def auth() -> flask.Response:
    if flask.request.method == 'POST':
        global creating_user
        data: dict = flask.request.form
        creating_user = user_setting.User.check_auth(**data, users_data=users)
        return flask.redirect(
            flask.url_for('main_page')
        )

    return flask.render_template(
        'auth.html'
    )

@app.route('/articles', methods=['GET', 'POST'])
def main_page():
    if flask.request.method == 'POST':
        search_articles: list['article.Article'] = []
        data: str = flask.request.form.get('search')
        data_genre: str = flask.request.form.get('genre')
        for art in articles_data:
            if (
                data.lower() in art.text_content.lower()
            ) or (
                data.lower() in art.title.lower()
            ):
                search_articles.append(art)
        print(data_genre)
        if data_genre != '':
            for art in articles_data:
                if data_genre == art.genre and art not in search_articles:
                    search_articles.append(art)

            for art in search_articles:
                if (
                    data_genre != art.genre
                ) or (
                    art.text_content.lower() != data.lower()
                ):
                    search_articles.remove(art)
        return flask.render_template(
            'index.html',
            articles=search_articles
        )

    for art in articles_data:
        if art.genre not in genres_artico:
            genres_artico.append(art.genre)
    return flask.render_template(
        'index.html',
        articles=articles_data,
        genres=genres_artico
    )

@app.route('/artico/<int:id>', methods=['GET', 'POST'])
def article_page(id: int):
    return flask.render_template(
        'artico.html',
        art=articles_data[id]
    )

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_page(id: int) -> flask.Response:
    if flask.request.method == 'POST':
        global creating_user
        global articles_data
        data: dict = flask.request.form
        articles_data.append(
            article.Article.update(
                user_name=creating_user.first_name,
                **data,
                article=articles_data[id]
            )
        )
        articles_data.pop(id)
        print(articles_data)
        return flask.redirect(
            flask.url_for('main_page')
        )

    return flask.render_template(
        'update.html',
        id=id
    )


@app.route('/create', methods=['GET', 'POST'])
def create_page() -> flask.Response:
    if flask.request.method == 'POST':
        global creating_user
        global articles_data
        data: dict = flask.request.form
        articles_data.append(
            article.Article.create(
            user_name=creating_user.first_name,
            **data
        )
        )
        return flask.redirect(
            flask.url_for('main_page')
        )

    return flask.render_template(
        'create.html'
    )

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )