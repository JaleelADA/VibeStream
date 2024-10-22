# VibeStream

VibeStream is a Django application that interacts with the Spotify API to display featured playlists, new releases, and search results for artists, albums, and playlists.

## Project Structure

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the home page.
- Use the search functionality to find artists, albums, and playlists.
- Click on featured playlists or new releases to view details.

## Files

- **[music_world/views.py](music_world/views.py)**: Contains the views for handling requests and rendering templates.
- **[music_world/utils.py](music_world/utils.py)**: Contains utility functions like `get_access_token`.
- **[music_world/templates/music_world](music_world/templates/music_world)**: Contains HTML templates for rendering the web pages.
