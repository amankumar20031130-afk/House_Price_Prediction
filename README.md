# California House Price Predictor 🏠

An interactive web application built with **Flask** and **Machine Learning** to visualize housing data across California and predict house prices based on various features.

## 🚀 Features
- **Interactive Map Visualization**: View thousands of housing data points plotted on a custom coordinate system.
- **Dynamic Selection**: Click any point on the map to automatically populate the prediction form with real dataset values.
- **Real-time Prediction**: Uses a trained Scikit-Learn pipeline to predict house prices based on:
  - Longitude & Latitude
  - Housing Median Age
  - Total Rooms & Bedrooms
  - Population & Households
  - Median Income
  - Ocean Proximity
- **Responsive Design**: Modern, clean UI with data tooltips and color-coded income levels.

## 🛠️ Technology Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, Vanilla CSS, Javascript (Canvas API)
- **Data Science**: Pandas, Scikit-Learn, Joblib
- **Deployment**: Ready for Render, Heroku, or Gunicorn

## 📦 Project Structure
```text
├── app.py                  # Flask server and prediction API
├── generate_mapdata.py     # Data cleaning and map JSON generation
├── housing.csv             # Raw California housing dataset
├── model.pkl               # Trained ML model (gitignored if >100MB)
├── pipeline.pkl            # Preprocessing pipeline
├── static/
│   └── mapdata.json        # Cleaned geographical data for the map
├── templates/
│   └── index.html          # Frontend single-page application
├── requirements.txt        # Python dependencies
└── Procfile                # Deployment configuration
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/House_Price_Pridiction.git
   cd House_Price_Pridiction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Map Data**:
   Ensure the `static/mapdata.json` is ready (this cleans the CSV and filters out missing values):
   ```bash
   python generate_mapdata.py
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   Open your browser and visit `http://localhost:5000`.

## 🌐 Deployment

This project is configured for easy deployment on **Render** or **Heroku**.

### Render Setup:
1. Connect your GitHub repository to Render.
2. Select **Web Service**.
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. The app will automatically use the `Procfile` configuration.

## ⚠️ Important Note
The `model.pkl` file is excluded from standard Git tracking if it exceeds 100MB. To deploy it, ensure you have **Git LFS** installed, or host the model file externally.

---
Developed as a demonstration of combining Machine Learning with interactive Web Visualizations.
