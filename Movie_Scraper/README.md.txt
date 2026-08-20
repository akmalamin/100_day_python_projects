# 🎬 Top 100 Movies Web Scraper

An automated Python web scraper built with **BeautifulSoup** and **Requests** that extracts and formats the "100 Greatest Movies of All Time" from Empire's historical web archive.

---

## 📌 Features

- **Automated Data Extraction**: Scrapes all 100 movie titles from web archive HTML.
- **Data Sanitization**: Cleans inconsistent formatting, colon variations, and numbering artifacts.
- **Export to File**: Formats and outputs the cleaned ranking list into a UTF-8 encoded `movies.txt` file.
- **Robust Error Handling**: Handles network requests and HTTP errors gracefully.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - [`BeautifulSoup4`](https://pypi.org/project/beautifulsoup4/) (DOM Parsing)
  - [`Requests`](https://pypi.org/project/requests/) (HTTP client)

---

## 🚀 Getting Started

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/100-movies-scraper.git
cd 100-movies-scraper
\`\`\`

### 2. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Run the script
\`\`\`bash
python main.py
\`\`\`

---

## 📄 Output Sample (`movies.txt`)

\`\`\`text
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
...
100) Stand By Me
\`\`\`

---

## 👤 Author

- **Akmal Amin** 