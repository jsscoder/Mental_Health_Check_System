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


Once deployed, update the API_BASE URL in your frontend index.html file to point to your new Render URL (e.g., https://your-api-name.onrender.com).

⚠️ Disclaimer
Built for informational and educational purposes only. This tool uses machine learning to model general wellness trends and is not a clinical diagnostic tool. If you are struggling with your mental health, please reach out to a trusted professional.
