from fasthtml.common import *
app = FastHTMLWithLiveReload()

app = FastHTML()

@app.get("/")
def home():
    return "<h1>Hello, World</h1>"