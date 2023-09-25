from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (you can replace this with your own data storage)
wiki_data = {
    "characters": {"title": "Characters", "content": "Here you can find the list of characters.", "id": "characters"},
    "factions": {"title": "Page 2", "content": "This is the content of Page 2.", "id": "factions"}}
    #"Locations": {"title": "Page 3", "content": "This is the content of Page 3.", "id": "locations"},
    #"History": {"title": "Page 4", "content": "This is the content of Page 4.", "id": "history"}
#}

characters = [
        {"id": "anariel", "name": "Anariel Raekhem", "description": "Sun elf paladin of Anar the sun god"},
        {"id": "lady_ishurit", "name": "Lady Ishur Nekht-Tet",
         "description": "Lady of the Nekht-Tet family, a noble family of sun elves"},
        {"id": "elthara", "name": "Elthara Nekht-Tet",
         "description": "Fourth daughter of the Nekht-Tet family, quiet and loves to read"},
        {"id": "lord_harun", "name": "Lord Harun Nekht-Tet",
         "description": "Lord of the Nekht-Tet family, esteemed leader of the sun elf community"},
        {"id": "kaelon", "name": "Kaelon Nekht-Tet",
         "description": "First son of the Nekht-Tet family, charismatic and ambitious future leader of the family"},
        {"id": "elara", "name": "Elara Nekht-Tet",
         "description": "Second daughter of the Nekht-Tet family, adventurous and free-spirited"},
        {"id": "lirael", "name": "Lirael Nekht-Tet",
         "description": "Fifth daughter of the Nekht-Tet family, a talented musician and singer"},
        {"id": "selene", "name": "Selene Nekht-Tet",
         "description": "Sixth daughter of the Nekht-Tet family, charismatic and skilled in diplomacy"},
        {"id": "rhydian", "name": "Rhydian Nekht-Tet",
         "description": "Seventh son of the Nekht-Tet family, deep thinker and philosopher"},
        {"id": "davhyr", "name": "Davhyr Nekht-Tet",
         "description": "Third son of the Nekht-Tet family, skilled warrior and tactician"},
        {"id": "kyiara", "name": "Kyiara Nekht-Tet",
         "description": "Youngest of the Nekht-Tet family, spirited and brilliant sorceress"}
    ]

factions_list = [
        {"id": "sun_elves_empire", "name": "Sun elves empire", "description": "The empire of the sun elves, residing in the white sea"}
    ]


@app.route('/')
def index():
    # Display a list of wiki pages
    return render_template('index.html', pages=wiki_data.keys())

@app.route('/page/<page_name>')
def view_page(page_name):
    # Display the content of a specific wiki page
    page = wiki_data.get(page_name)
    if page:
        return render_template('base.html', page=page)
    else:
        return "Page not found", 404

@app.route('/edit/<page_name>', methods=['GET', 'POST'])
def edit_page(page_name):
    # Edit the content of a specific wiki page
    page = wiki_data.get(page_name)
    if request.method == 'POST':
        if page:
            page['content'] = request.form['content']
        return redirect(url_for('view_page', page_name=page_name))
    return render_template('edit.html', page=page)


@app.route('/characters')
def character_list():
    # Assuming you have a list of characters with names and descriptions
    characters = [
        {"id": "anariel", "name": "Anariel Raekhem", "description": "Sun elf paladin of Anar the sun god"},
        {"id": "lady_ishurit", "name": "Lady Ishur Nekht-Tet",
         "description": "Lady of the Nekht-Tet family, a noble family of sun elves"},
        {"id": "elthara", "name": "Elthara Nekht-Tet",
         "description": "Fourth daughter of the Nekht-Tet family, quiet and loves to read"},
        {"id": "lord_harun", "name": "Lord Harun Nekht-Tet",
         "description": "Lord of the Nekht-Tet family, esteemed leader of the sun elf community"},
        {"id": "kaelon", "name": "Kaelon Nekht-Tet",
         "description": "First son of the Nekht-Tet family, charismatic and ambitious future leader of the family"},
        {"id": "elara", "name": "Elara Nekht-Tet",
         "description": "Second daughter of the Nekht-Tet family, adventurous and free-spirited"},
        {"id": "lirael", "name": "Lirael Nekht-Tet",
         "description": "Fifth daughter of the Nekht-Tet family, a talented musician and singer"},
        {"id": "selene", "name": "Selene Nekht-Tet",
         "description": "Sixth daughter of the Nekht-Tet family, charismatic and skilled in diplomacy"},
        {"id": "rhydian", "name": "Rhydian Nekht-Tet",
         "description": "Seventh son of the Nekht-Tet family, deep thinker and philosopher"},
        {"id": "davhyr", "name": "Davhyr Nekht-Tet",
         "description": "Third son of the Nekht-Tet family, skilled warrior and tactician"},
        {"id": "kyiara", "name": "Kyiara Nekht-Tet",
         "description": "Youngest of the Nekht-Tet family, spirited and brilliant sorceress"}
    ]

    return render_template('characters.html', characters=characters)

@app.route('/character/<character_id>')
def character(character_id):
    characters = [
        {"id": "anariel", "name": "Anariel Raekhem", "description": "Sun elf paladin of Anar the sun god"},
        {"id": "lady_ishurit", "name": "Lady Ishur Nekht-Tet", "description": "Lady of the Nekht-Tet family, a noble family of sun elves"},
        {"id": "elthara", "name": "Elthara Nekht-Tet", "description": "Fourth daughter of the Nekht-Tet family, quiet and loves to read"},
        {"id": "lord_harun", "name": "Lord Harun Nekht-Tet", "description": "Lord of the Nekht-Tet family, esteemed leader of the sun elf community"},
        {"id": "kaelon", "name": "Kaelon Nekht-Tet", "description": "First son of the Nekht-Tet family, charismatic and ambitious future leader of the family"},
        {"id": "elara", "name": "Elara Nekht-Tet", "description": "Second daughter of the Nekht-Tet family, adventurous and free-spirited"},
        {"id": "lirael", "name": "Lirael Nekht-Tet", "description": "Fifth daughter of the Nekht-Tet family, a talented musician and singer"},
        {"id": "selene", "name": "Selene Nekht-Tet", "description": "Sixth daughter of the Nekht-Tet family, charismatic and skilled in diplomacy"},
        {"id": "rhydian", "name": "Rhydian Nekht-Tet", "description": "Seventh son of the Nekht-Tet family, deep thinker and philosopher"},
        {"id": "davhyr", "name": "Davhyr Nekht-Tet", "description": "Third son of the Nekht-Tet family, skilled warrior and tactician"},
        {"id": "kyiara", "name": "Kyiara Nekht-Tet", "description": "Youngest of the Nekht-Tet family, spirited and brilliant sorceress"}
    ]
    # Find the character by ID
    character = next((char for char in characters if char["id"] == character_id), None)

    if character:
        # Construct the template name dynamically based on character_id
        template_name = f"{character_id}.html"
        return render_template(template_name, character=character)
    else:
        return "Character not found", 404


@app.route('/factions')
def factions():
    # Assuming you have a list of characters with names and descriptions
    factions = [
        {"id": "sun_elves_empire", "name": "Sun elves empire", "description": "The empire of the sun elves, residing in the white sea"}
    ]

    return render_template('factions.html', factions=factions)

@app.route('/faction/<faction_id>')
def faction(faction_id):
    factions = [
        {"id": "sun_elves_empire", "name": "Sun elves empire",
         "description": "The empire of the sun elves, residing in the white sea"}
    ]


# Find the character by ID
    faction = next((char for char in factions if char["id"] == faction_id), None)

    if faction:
        # Construct the template name dynamically based on character_id
        template_name = f"{faction_id}.html"
        return render_template(template_name, faction=faction)
    else:
        return "Character not found", 404




if __name__ == '__main__':
    app.run(debug=True)
