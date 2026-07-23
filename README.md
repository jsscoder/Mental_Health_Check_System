Markdown
# Mental Health Signal 🧠📊

**Mental Health Signal** is a full-stack machine learning application designed to predict a student's mental wellness score (from 0 to 10) based on their academic workload, digital habits, sleep, and perceived stress levels. 

Built with a lightning-fast **FastAPI** backend and a responsive, vanilla **HTML/CSS/JS** frontend, this project uses a trained **Scikit-Learn** `RandomForestRegressor` pipeline to deliver instant insights via a beautifully animated UI gauge.

---

## 🚀 Features

* **Machine Learning Pipeline**: Uses a pre-trained scikit-learn model (`mental_health_pipeline.pkl`) handling data scaling, ordinal encoding, and regression.
* **FastAPI Backend**: High-performance REST API with automatic data validation via Pydantic.
* **Client-Side Validation**: Frontend mirrors backend Pydantic rules to catch errors before network requests are made.
* **Modern UI/UX**: Clean, ergonomic design with animated SVGs, state management (idle, loading, result, error), and fully responsive layout.
* **Cross-Origin Resource Sharing (CORS)**: Configured to allow seamless communication between the frontend and the API.

---

## 🛠️ Tech Stack

**Backend**
* [Python 3.12](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) - Web framework
* [Uvicorn](https://www.uvicorn.org/) - ASGI server
* [Scikit-Learn (v1.6.1)](https://scikit-learn.org/) - ML Model inference
* [Pandas](https://pandas.pydata.org/) & [Joblib](https://joblib.readthedocs.io/) - Data manipulation and model loading
* [uv](https://github.com/astral-sh/uv) - Extremely fast Python package installer and resolver

**Frontend**
* HTML5 / CSS3 (Custom Variables, Flexbox/Grid, Responsive Media Queries)
* Vanilla JavaScript (Fetch API, DOM manipulation)

---

## 📂 Project Structure

```text
├── main.py                          # FastAPI backend application
├── mental_health_pipeline.pkl       # Pre-trained ML model
├── index.html                       # Frontend UI (HTML, CSS, JS combined)
├── req.txt                          # Python dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # Project documentation
💻 Local Development Setup
We recommend using uv for blazing-fast environment management, but standard pip works too.
```
1. Clone the repository
Bash
git clone [https://github.com/yourusername/mental-health-signal.git](https://github.com/yourusername/mental-health-signal.git)
cd mental-health-signal
2. Set up the Virtual Environment (using uv)
Ensure you are using a stable Python version (like 3.12) to avoid compilation issues with scikit-learn.

Bash
# Create the environment
uv venv my_env --python 3.12

# Activate the environment (Windows)
.\my_env\Scripts\activate

# Activate the environment (Mac/Linux)
source my_env/bin/activate
3. Install Dependencies
Bash
uv pip install -r req.txt
4. Run the Backend API
Start the FastAPI server using Uvicorn with auto-reload enabled:

Bash
uvicorn main:app --reload --port 8000
The API will be available at http://127.0.0.1:8000
Interactive API docs available at http://127.0.0.1:8000/docs

5. Run the Frontend
Simply double-click the index.html file to open it in your web browser, or use an extension like Live Server in VS Code.

(Make sure the API_BASE variable in your JavaScript code is set to http://127.0.0.1:8000 for local development).

📡 API Reference
POST /predict
Evaluates the student's data and returns a mental health score.

Request Body (JSON)

JSON
{
  "age": 21,
  "gender": "Male",
  "country": "India",
  "academic_level": "Undergraduate",
  "most_used_platform": "Instagram",
  "purpose_of_use": "Entertainment",
  "avg_daily_usage_hours": 4.5,
  "daily_unlocks": 65,
  "study_hours": 5.0,
  "physical_activity_hours": 1.0,
  "sleep_hours_per_night": 7.0,
  "stress_level": "Medium"
}
Response (JSON)

JSON
{
  "predicted_mental_health_score": 6.78
}
☁️ Deployment
This project is configured for easy deployment on Render.

Create a new Web Service on Render.

Connect your GitHub repository.

Set the following configurations:

Build Command: pip install -r req.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Once deployed, update the API_BASE URL in your frontend index.html file to point to your new Render URL (e.g., https://your-api-name.onrender.com).

⚠️ Disclaimer
Built for informational and educational purposes only. This tool uses machine learning to model general wellness trends and is not a clinical diagnostic tool. If you are struggling with your mental health, please reach out to a trusted professional.
