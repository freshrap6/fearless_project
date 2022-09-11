from items_api.api import create_app

app = create_app()
app.config['DEBUG'] = False

