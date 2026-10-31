# Insurance Review NLP — Rating Prediction & Sentiment Analysis

**Natural Language Processing · Machine Learning · Transformers · Explainability · Streamlit**

An academic team project investigating how text from **24,103 insurance customer reviews** can be analyzed to predict **1–5 star ratings**, identify themes and visualize language embeddings.

## What we explored

- **Exploratory analysis and preprocessing** of English-translated customer reviews.
- **Topic modeling** with Latent Dirichlet Allocation (LDA).
- **Text representations**: TF-IDF, Word2Vec and pretrained GloVe embeddings.
- **Rating classification**: Logistic Regression and neural-network/transformer alternatives, including DistilBERT.
- **Rating regression**: Ridge and other regression approaches.
- **Sentiment and theme analysis**, plus embedding visualizations.
- **Streamlit interface** for rating prediction and word-level explanations.

```text
Insurance reviews
      ↓
Data preparation → EDA → Topic modeling / Embeddings
      ↓
TF-IDF and neural NLP approaches
      ├─ 5-class star rating classification
      └─ Continuous rating regression
      ↓
Evaluation / Interpretation → Streamlit interface
```

## Reported results

| Task | Approach | Reported result |
|---|---|---|
| Five-class rating prediction | TF-IDF + Logistic Regression | **53.3% accuracy** |
| Rating regression | TF-IDF + Ridge | **RMSE 0.89**, MAE 0.70, R² 0.66 |
| Sentiment analysis | Positive / neutral / negative | **80.6% accuracy** |
| Limited-sample classification experiment | Fine-tuned DistilBERT | 49.2% accuracy on a **500-review test subset** |

These figures are taken from the team's [final report](reports/final_report.md), **not independently reproduced for this portfolio copy**. The DistilBERT subset is not directly comparable with the full-test-set baselines. See the report for conditions and limitations.

## Repository contents

| Location | Purpose |
|---|---|
| `notebooks/01_eda.ipynb` | Exploratory data analysis |
| `notebooks/02_cleaning.ipynb` | Preprocessing |
| `notebooks/03_topics.ipynb` | Topic modeling |
| `notebooks/04_embeddings.ipynb` | Word representations |
| `notebooks/05_classification.ipynb` | Star-rating classification experiments |
| `notebooks/05_regression.ipynb` | Rating regression experiments |
| `src/data/` | Reusable loading and cleaning functions |
| `retrain_classification.py` | Train and save TF-IDF + Logistic Regression |
| `app/streamlit_app.py` | Interactive prediction interface |
| `reports/final_report.md` | Methods, results and discussion |

## Installation

```bash
git clone https://github.com/fdlghita/insurance-review-nlp.git
cd insurance-review-nlp
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Dataset and training assets

**The original raw Excel files and the large processed review datasets are intentionally not redistributed here.** To rerun experiments, obtain the data from the project's authorized source and place the Excel inputs under `data/raw/`, then run:

```bash
python src/data/load_data.py
python src/data/preprocessing.py
python retrain_classification.py
```

This generates `data/processed/dataset_clean.csv` and the **classification** model at `models/tfidf_logreg_classification.pkl`. The app also expects `models/tfidf_ridge_regression.pkl`: train/export the Ridge pipeline with the regression notebook before launching it.

```bash
streamlit run app/streamlit_app.py
```

**Important:** the Streamlit app is **not immediately runnable after cloning** because trained model artifacts and datasets are excluded. The notebooks may rely on additional model downloads and compute resources; the scripts have not been end-to-end retested in this portfolio repository.

## Limitations

- Five-class ratings are difficult to infer from text alone; adjacent rating classes overlap and the data exhibit class imbalance.
- Some benchmarks use smaller training/test subsets or different setups.
- Review translations may change language nuances.
- This is an **academic proof of concept**, not an operational insurance assessment system.
- The final report contains some class-frequency and baseline descriptions that are not fully consistent; consult the code and reproduce metrics before citing them as independently verified findings.

## Team & attribution

**Ghita Fadili and Louis** — ESILV academic team project (March 2026). This portfolio repository republishes selected **collaborative work**, without claiming sole authorship or assigning individual module ownership.

Source materials were supplied from the team's `NLP_projet_1` project, branch `projet2`. Original project link: https://github.com/Louis-ibt/NLP_projet_1/tree/projet2.

No separate open-source license has been granted in these materials; third-party reuse is subject to the contributors' rights and dataset terms.
