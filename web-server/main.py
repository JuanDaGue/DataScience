import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <p> Lorem </p>
        </body>
    </html>
    """
@app.get('/')
def get_list():
    return [1, 2, 3]


@app.get('/contact')
def get_list():
    return {"name": 'JuanPlatzi'}


def run():
    store.get_categories()


if __name__ == '__main__':
    run()