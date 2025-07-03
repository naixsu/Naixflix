# 🎬 Naixflix - Movie Management Platform

Naixflix is a full-stack movie management application that allows users to upload, view, update, and delete movie entries with associated video files. Built with **Django** (backend) and **Vue 3** (frontend).

> 📌 This project was created as part of a technical assessment assigned by a recruiter. It was completed within the given 3-day deadline and demonstrates full-stack development skills under time constraints.

---

## 🔧 Tech Stack

| Layer      | Tech                      |
|------------|---------------------------|
| Backend    | Django, Django REST Framework |
| Frontend   | Vue 3, Axios              |
| Database   | SQLite (development)      |
| Deployment | (Optional) Docker         |

---

## 🚀 Features

### Backend (Django)
- Movie model with:
  - `title` (string)
  - `description` (string)
  - `date_added` (auto-set date)
  - `video_file` (uploaded file)
  - `is_removed` (boolean, used for soft delete)

- API Endpoints:
  - `GET /movies/` — List all **non-deleted** movies
  - `POST /movies/` — Create a new movie with a video file
  - `PATCH /movies/<pk>/` — Update movie fields (title, description, video file, etc.)
  - `PATCH /movies/<pk>/` — Soft delete a movie by setting `is_removed: true`

> ⚠️ **Note:** The app uses `PATCH` exclusively for updates and soft-deletes.  
> `PUT` is not used, as it requires all fields including the video file, which isn't practical for partial edits.


### Frontend (Vue 3)
- All API calls are implemented in a single `<script setup>` section
- List movies (title, date added)
- View movie details and play video
- Create/edit movies with file upload
- Soft delete functionality using PATCH
- Error handling with `required`
- Netflix-style layout and modal interactions

---

## 📦 Prerequisites

### Backend
- Python 3.8+
- pip or pipenv
- Virtualenv (recommended)

### Frontend
- Node.js 16+
- npm or yarn

---

## 🛠 Setup Instructions

### 🐍 Backend (Django)

```bash
# Clone the repo
git clone https://github.com/naixsu/Naixflix.git
cd Naixflix/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Media files will be served at `http://127.0.0.1:8000/media/`

---

### 🎨 Frontend (Vue 3)

```bash
# Open a new terminal
cd ../frontend

# Install dependencies
npm install

# Run the frontend
npm run serve
```

App will be served at `http://localhost:8080`

> Make sure the Django server is running to access API endpoints.

---

## 🧪 Testing the App

### To upload a movie:
1. Go to the homepage.
2. Click **Add Movie**, fill in the details, and upload a video.
3. Click **Submit**.

### To watch a video:
- Click on any movie card to open its detail page.
- Video will be played on the embedded `<video>` tag.

### To delete a movie:
- Click the delete icon or button — this performs a **soft delete** by setting `is_removed = true`.

---

## 🧱 Project Structure

```
Naixflix/
├── backend/               # Django Project
│   ├── movies/            # Django app
│   └── media/             # Uploaded videos (this will auto create if not existing yet)
├── frontend/              # Vue 3 Project
│   ├── node_modules/      # Installed after `npm i`
│   ├── public/            # Contains `index.html`
│   ├── src/               # Contains `App.vue` and all the necessary files
```

---

## 🐞 Known Issues / Limitations

- No authentication
- No video thumbnails or streaming via HLS
- Soft delete only; no restore feature
- When editing, the video input is not populated
- Video files are not stored directly in the database.
---

## 🎥 Demo Instructions

> 📺 You can view a walkthrough demo video [HERE](https://drive.google.com/file/d/1ixqbprSKP7ocIOFky7Q83BH44RVYkPQz/view?usp=sharing).

Steps:
1. Run backend and frontend servers
2. Open `http://localhost:8080`
3. Add a movie, edit it, delete it, and view playback
4. Profit?

