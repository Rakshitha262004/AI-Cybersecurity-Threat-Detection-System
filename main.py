from src.preprocessing import load_data, preprocess_data
from src.model import train_model, evaluate_model
from src.detection import detect_threats
from src.visualization import plot_label_distribution

# Step 1: Load data
data = load_data("data/dataset.csv")

# ✅ MOVE THIS HERE (VERY IMPORTANT)
plot_label_distribution(data)

# Step 2: Preprocess
X_train, X_test, y_train, y_test = preprocess_data(data)

# Step 3: Train model
model = train_model(X_train, y_train)

# Step 4: Evaluate
evaluate_model(model, X_test, y_test)

# Step 5: Detect threats
detect_threats(model, X_test)