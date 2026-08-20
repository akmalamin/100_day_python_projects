
from bs4 import BeautifulSoup
import requests

# ==============================================================================
# CONFIGURATION
# ==============================================================================

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
OUTPUT_FILE = "movies.txt"


# ==============================================================================
# FUNCTIONS
# ==============================================================================

def scrape_movies():

    response = requests.get(URL)
    response.raise_for_status()
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")

    # The titles are within <h3> tags
    movie_titles = soup.find_all(name="h3")
    movie_titles_text = [title.text for title in movie_titles]
    return movie_titles_text


def reverse_movies(movie_list):

    return movie_list[::-1]


def save_to_file(movies):

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for index, movie in enumerate(movies, start=1):
            if ":" in movie:
                clean_title = movie.split(":", 1)[-1].strip()
            elif ")" in movie:
                clean_title = movie.split(")", 1)[-1].strip()
            else:
                clean_title = movie.strip()

            file.write(f"{index}) {clean_title}\n")

    print(f"✅ Saved {len(movies)} clean movie titles to {OUTPUT_FILE}")

# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

def main():
    print("=" * 50)
    print("🎬 100 MOVIES SCRAPER")
    print("=" * 50)

    print("\n📥 Scraping movies from Empire...")
    movies = scrape_movies()
    print(f"✅ Scraped {len(movies)} movies!")

    print("\n🔄 Reversing order...")
    movies = reverse_movies(movies)

    print("\n💾 Saving movies to file...")
    save_to_file(movies)

    print("\n" + "=" * 50)
    print(f"🎉 Complete! Check {OUTPUT_FILE}")
    print("=" * 50)


if __name__ == "__main__":
    main()