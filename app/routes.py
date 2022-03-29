from app import app
from flask import render_template

@app.route('/')
def index():
    title = 'Home'
    posts = [ 
        {
            'id': 1,
            'title': 'Rubber Tree',
            'body': 'A South American tropical tree that can grow up to 50 feet tall.',
            'type': 'Fiscus Elastica'
        },
        {
            'id': 2,
            'title': 'ZZ-plant',
            'body': 'Perennial native to East Africa. Almost impossible to kill due to their tolerance for neglect.',
            'type': 'Zamioculcus zamifolia'
        },
        {
            'id': 3,
            'title': 'Pinstripe Calathea',
            'body': 'This prayer plant is known for its beautiful pink strips and large leaves.',
            'type': 'Calathea Ornata'
        },
        {
            'id': 4,
            'title': 'Croton',
            'body': 'An evergreen shrub native to India. The leaves turn hues of yellow, orangee, and red when exposed to sun.',
            'type': 'Codiaum variegatum'
        },
        {
            'id': 5,
            'title': 'White bird of paradise',
            'body' : "Known for it's banana-like leaves, they can grow up to 20 feet indoors.",
            'type': 'Strelitzia nicolai'
        }
    ]
    return render_template('index.html', title=title, posts=posts)


@app.route('/test')
def test():
    return "This is a test"

@app.route('/more')
def more():
    return render_template('more.html')