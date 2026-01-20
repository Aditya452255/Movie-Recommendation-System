# Movie Recommendation System

An end-to-end movie recommendation app with a Streamlit UI and a FastAPI backend. It combines TMDB-powered search/details with local TF‑IDF similarity to suggest similar titles, plus genre-based recommendations.

## Features
- Search with live suggestions (TMDB keyword search)
- Movie details: poster, overview, release date, genres
- Recommendations:
  - TF‑IDF similarity (local dataset)
  - Genre-based (TMDB Discover)
- Home feed categories: trending, popular, top_rated, now_playing, upcoming

## Project Structure
- `app.py` — Streamlit front-end
- `main.py` — FastAPI backend with TMDB and TF‑IDF endpoints
- `movies_metadata.csv` — Source data (optional for building TF‑IDF)
- `Movie_recmmendation.ipynb` — Notebook you can use to prepare pickles
- `requirements.txt` — Python deps (or install manually as below)

## Prerequisites
- Python 3.10+
- TMDB API key in a `.env` file at the project root:
  
  ```env
  TMDB_API_KEY=your_tmdb_key_here
  ```

- TF‑IDF pickles in the project root (generated from your dataset):
  - `df.pkl` — DataFrame with a `title` column
  - `indices.pkl` — title → row index map (dict or Series)
  - `tfidf_matrix.pkl` — TF‑IDF matrix (e.g., scipy sparse matrix)
  - `tfidf.pkl` — TF‑IDF vectorizer (optional but kept for reproducibility)

You can use the notebook `Movie_recmmendation.ipynb` to generate these artifacts.

## Installation
Either install from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Or install the minimal set directly:

```bash
python -m pip install fastapi uvicorn[standard] streamlit httpx numpy pandas python-dotenv pydantic scipy
```

## Running Locally
1) Start the API (FastAPI):

```bash
uvicorn main:app --reload
```

2) Start the UI (Streamlit):

```bash
streamlit run app.py
```

By default, `app.py` points `API_BASE` to a deployed backend. To use your local API, set `API_BASE` in `app.py` to `http://127.0.0.1:8000`.

## API Overview (FastAPI)
- `GET /health` — Health check
- `GET /home?category=popular&limit=24` — Home feed posters (trending, popular, top_rated, upcoming, now_playing)
- `GET /tmdb/search?query=...` — TMDB keyword search (raw TMDB shape with `results`)
- `GET /movie/id/{tmdb_id}` — Movie details
- `GET /recommend/genre?tmdb_id=...&limit=18` — Genre-based recommendations
- `GET /recommend/tfidf?title=...&top_n=10` — TF‑IDF only (debug)
- `GET /movie/search?query=...&tfidf_top_n=12&genre_limit=12` — Bundle: details + TF‑IDF + genre

## Deploying
- Backend can be hosted on any ASGI-compatible service (e.g., Render, Railway, Fly.io). Ensure `.env` includes `TMDB_API_KEY` and the TF‑IDF pickles are available at runtime.
- Frontend (Streamlit) can run on Streamlit Community Cloud or the same VM/container as the API. Update `API_BASE` in `app.py` to point to your backend URL.

## Contributing
Feel free to open issues and PRs. For local development, keep changes focused and ensure the API still boots and the Streamlit app renders without errors.

## License
Aditya Jain
