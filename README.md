# Spotify Billboard Playlist Creator

This Python project creates a private Spotify playlist using the top songs from the Billboard Hot 100 chart for a specific date. The script scrapes song data from the Billboard website and uses the Spotify API to search for the tracks and add them to a newly created playlist in your Spotify account.

## Prerequisites

1. **Python 3.8 or higher**
2. **Spotify Developer Account**
   - Create a Spotify Developer Application [here](https://developer.spotify.com/dashboard/applications).
   - Obtain your `CLIENT_ID` and `CLIENT_SECRET`.
3. **Required Python Libraries**:
   - `requests`
   - `beautifulsoup4`
   - `spotipy`
   - `pprint` (optional, for debugging purposes)

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 spotipy
```

## Setup

1. Clone or download this repository.
2. Open the script and update the following variables with your Spotify API credentials:
   ```python
   CLIENT_ID = "your_client_id_here"
   CLIENT_SECRET = "your_client_secret_here"
   REDIRECT_URL = "http://example.com"
   ```
3. Replace `USER` with your Spotify username.
4. Make sure your Spotify application has the `playlist-modify-private` scope enabled in the dashboard.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the date in `YYYY-MM-DD` format when prompted. For example:
   ```
   Which year do you want to get into: Enter the date in YYYY-MM-DD format: 2020-08-15
   ```
3. The script will:
   - Fetch the top 100 songs from the Billboard Hot 100 chart for the entered date.
   - Search Spotify for the tracks.
   - Create a private playlist named after the entered date.
   - Add the tracks to the playlist.
4. Upon success, you'll see a message:
   ```
   added successfully
   ```

## Script Overview

- **`get_uri(songname, year)`**: Searches for the Spotify URI of a song by name and year.
- **Web Scraping**: Uses `BeautifulSoup` to extract song titles from the Billboard Hot 100 chart page.
- **Spotify API Integration**: Creates a private playlist and adds songs using the Spotify Web API.

## Error Handling

If there's an error during playlist creation or track addition, the script will print the error message:
```bash
error is: [Error details]
```

## Notes

- Ensure your Spotify account is active and can create private playlists.
- The script may fail to find certain songs due to mismatches between Billboard titles and Spotify track data.
- Use a valid `User-Agent` header for requests to avoid being blocked by the Billboard website.

## License

This project is open-source and available under the MIT License.

## Author

Mohammed Sadiq Ali
