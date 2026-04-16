from flask import Blueprint, render_template, session, redirect, url_for, request
from werkzeug.utils import secure_filename
import os

views_blueprint = Blueprint('views', __name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            },
            {
                'id': 4,
                'name': 'ishowSp33d',
                'hp': '232',
                'type': 'Fire',
                'image':'static/uploads/ishowspeed-zg33717.png'

            }
        ]
    return render_template('collection.html', cards=session['cards'])

@views_blueprint.route('/add', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        name = request.form.get('name')
        hp = request.form.get('hp')
        card_type = request.form.get('type')
        file = request.files.get('image')
        if not name or not hp or not card_type or not file:
            return "Error: All fields are required!", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            new_card = {
                'id': len(session.get('cards',[])) + 1,
                'name': name,
                'hp': hp,
                'type': card_type,
                'image': '/' + filepath.replace('\\','/')
            }
            session['cards'].append(new_card)
            session.modified = True
            return redirect(url_for('views.collection'))
        else:
            return "Error: Invalid file type. Only images allowed.", 400
    return render_template('add_card.html')

@views_blueprint.route('/remove/<int:card_id>', methods=['POST'])
def remove_card(card_id):
    session['cards'] = [card for card in session['cards'] if card['id'] != card_id]
    session.modified = True
    return redirect(url_for('views.collection'))