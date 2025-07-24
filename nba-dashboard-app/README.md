# 🏀 NBA Player Performance Dashboard

An interactive data visualization app that lets users explore NBA player performance metrics and uses machine learning to **predict how many points a player might score** in a game.

Built with `Streamlit`, `pandas`, and an `XGBoost` model trained on 2024–25 NBA data.

---

## 🎯 Features

- Filter by player, team, opponent, or game date
- Interactive charts showing key stats (FG%, 3P%, FT%, AST, STL, etc.)
- Real-time **point prediction** using a pre-trained XGBoost model
- Clean UI built with Streamlit for fast responsiveness

---

## 📁 Folder Structure

```bash
nba-dashboard-app/
├── app/
│   ├── main.py              # Streamlit app
│   └── predict.py           # ML logic
├── data/
│   └── database_24_25.csv   # Player stats
├── models/
│   └── pts_predictor_xgb.pkl  # Pretrained XGBoost model
├── requirements.txt
└── README.md


## 🚀 Model Training (Optional for Rebuilding)
If you'd like to retrain the XGBoost model:

Clean the dataset in data/database_24_25.csv

Engineer features: FG%, 3P%, FT%, etc.

Use train_test_split() and XGBRegressor

Save the model to models/pts_predictor_xgb.pkl



## 🧠 Tech Stack
| Purpose       | Tool                       |
| ------------- | -------------------------- |
| Web UI        | Streamlit                  |
| ML Model      | XGBoost                    |
| Data Handling | pandas                     |
| Deployment    | Streamlit Cloud (optional) |
| Language      | Python 3.10+               |


## 🧰 Future Improvements
Player comparison feature

Season-level trend analysis

Deploy as public app (Streamlit Cloud)

Scrape new NBA game data via API


🧑‍💻 Author
TJ
📫 GitHub
📝 Open to collaboration and contributions!

