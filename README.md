[README.md](https://github.com/user-attachments/files/29706417/README.md)
# 🏆 FIFA World Cup Qatar 2022 Analytics Dashboard

## 📌 Project Overview

This project is an interactive, data-driven web application built with **Python** and **Streamlit** to analyze and visualize the matches of the FIFA World Cup Qatar 2022.

---

## 🧠 How It Works & Code Explanation

The project follows a **Modular Architecture**, dividing the application into specific layers. Here is how each component works:

### 1️⃣ Data Loading Layer (`data_loader.py`)

- **Purpose:** Handles data ingestion and initial cleaning.
- **Explanation:** It uses `pandas.read_csv()` to load the dataset into memory. To prevent syntax bugs and ensure seamless calling across other files, it strips trailing spaces from the dataset's column names using `.str.strip()`. It utilizes `@st.cache_data` so the file is loaded only once, optimizing app performance.

### 2️⃣ Analytics & Logic Engine (`analytics.py`)

- **Purpose:** Performs all pure data manipulation and algorithmic calculations.
- **Explanation:**
  - **Tournament Stats:** Calculates top-level metrics using Pandas (`.sum()`, `.mean()`, and `.max()`) on goal columns.
  - **Stage Filtering:** Uses boolean indexing (`df[df['category'] == selected_stage]`) to dynamically isolate matches based on user input.
  - **Match Classification (NumPy):** Implements `np.where()` to apply conditional logic across rows. If the total goals in a match exceed a certain threshold, NumPy tags it as a `"🔥 High Scoring Game"`, otherwise it is categorized as a `"⚽ Defensive/Tactical Game"`.

### 3️⃣ Visualization & Scoreboard Component (`visualisation.py`)

- **Purpose:** Transforms filtered data into visual UI components.
- **Explanation:**
  - **Live Scoreboard:** Extracts specific match series and pipes team names and goals into custom `st.columns()` layout rows using `st.metric()`.
  - **Possession Representation:** Parses string percentage values (e.g., `'45%'`), strips the `%` sign, casts them to integers, and renders native Streamlit progress bars.
  - **Micro Pie Chart:** Generates a Matplotlib figure explicitly via `plt.figure()`. It draws a customized pie chart with distinct tournament colors, sets transparent backgrounds (`set_alpha(0.0)`) to natively blend with Streamlit's Dark Mode, and binds it layout-tight using `st.pyplot(fig, width="stretch")`.

### 4️⃣ The Orchestrator (`Qatar.py`)

- **Purpose:** The main entry point that wires all modules together and establishes the Streamlit layout grid.
- **Explanation:** It sets up page configs, calls the loading layer, displays the tournament overview metrics, and sets up a global dropdown filter. It implements **Smart Dynamic Layout UI**: it checks the row length of the filtered data (`len(filtered_df) > 1`); if a full group stage is selected, it displays a clean table grid, but if a single match final is selected, it hides the table entirely to avoid clutter and renders the detailed Scoreboard smoothly.
