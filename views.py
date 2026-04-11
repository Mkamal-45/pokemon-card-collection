from flask import Blueprint, render_template, session

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def home():
    return render_template('home.html')

@views_blueprint.route('/collection')
def collection():
    if 'cards' not in session:
        session['cards']=[
            {
                'id': 1,
                'name': 'Scizor',
                'hp': '140',
                'type': 'Steel',
                'image': 'https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV03/SV03_EN_205.png'
            },
            {
                'id': 2,
                'name': 'Nidoking',
                'hp': '330',
                'type': 'Dark',
                'image': 'https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV10/SV10_EN_233.png'

            },
            {
                'id': 3,
                'name': 'Blaziken',
                'hp': '170',
                'type': 'Fire',
                'image': 'https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SWSH3/SWSH3_EN_24.png'
            }
        ]
    return render_template('collection.html', cards=session['cards'])