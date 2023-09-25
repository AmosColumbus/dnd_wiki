import os
import shutil
from flask_frozen import Freezer
from app import app, wiki_data, characters, factions_list  # Import your Flask app and sample data

# Initialize Flask-Freezer for freezing the app
freezer = Freezer(app)


# Build the Flask app for static HTML pages
@freezer.register_generator
def url_generator():
    for page_name in wiki_data.keys():
        yield 'view_page', {'page_name': page_name}

    # Generate URLs for character pages
    for character in characters:
        yield 'character', {'character_id': character['id']}

    for faction in factions_list:
        yield 'faction', {'faction_id': faction['id']}


# Run the Flask-Freezer to freeze the app
if __name__ == '__main__':
    app.config.update(FREEZER_RELATIVE_URLS=True)

    # Freeze the app
    freezer.freeze()

    # Move the generated HTML files to the 'gh-pages' directory
    build_folder = '_build'
    gh_pages_folder = 'gh-pages'

    if os.path.exists(gh_pages_folder):
        shutil.rmtree(gh_pages_folder)

    shutil.copytree(build_folder, gh_pages_folder)

    print('App successfully frozen and deployed to gh-pages folder.')
