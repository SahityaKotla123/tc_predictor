# Superconductor Critical Temperature Predictor

Predicting the superconducting critical temperature (Tc) of materials using machine learning, served as a production REST API.

**Live API:** https://tc-predictor.onrender.com/docs

## What it does

Superconductors lose all electrical resistance below a critical temperature (Tc). Discovering new high-Tc materials is a major research challenge as experiments are expensive. This project builds an ML model that predicts Tc from 4 physical properties of a material, enabling faster computational screening before lab synthesis.
 
The dataset was manually compiled from 15 published research papers, covering 760 hydrogen-rich superconducting materials. We trained and compared 4 models (XGBoost, Random Forest, Neural Network, SVM) with XGBoost achieving the best performance (R² = 0.74, RMSE = 43K). The model is served via a FastAPI REST API, containerized with Docker, and deployed on Render.

## Model Performance

| Model | R² | RMSE |
|---|---|---|
| XGBoost (best) | 0.74 | 43K |
| Random Forest | 0.71 | 45K |
| Neural Network | 0.53 | 58K |
| SVM | 0.27 | 72K |

XGBoost outperformed all other models. Tree-based models generalize better on small, imbalanced scientific datasets.

## Features Used

- `press_GPa` — applied pressure in gigapascals
- `ave_valency` — average valency of the material
- `valency_per_H` — valency per hydrogen atom (top predictor)
- `r_ion_Angstrom` — ionic radius in angstroms

## Tech Stack

- **Model:** XGBoost with GridSearchCV tuning
- **API:** FastAPI
- **Containerization:** Docker
- **Deployment:** Render

## Architecture

```
Request → FastAPI (/predict) → XGBoost model → JSON response
```

## Run Locally

```bash
git clone https://github.com/SahityaKotla123/tc_predictor.git
cd tc_predictor
pip install -r requirements.txt
uvicorn app:app --reload
```

Or with Docker:

```bash
docker build -t tc-predictor .
docker run -p 8000:8000 tc-predictor
```

## Example Request

```json
POST /predict
{
  "press_GPa": 200,
  "ave_valency": 2.5,
  "valency_per_H": 0.5,
  "r_ion_Angstrom": 1.0
}
```

## Example Response

```json
{
  "predicted_Tc_K": 241.62
}
```
