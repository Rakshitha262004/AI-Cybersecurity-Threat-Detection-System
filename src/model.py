from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def train_model(X_train, y_train):
    print("🚀 Training model...")

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("✅ Model training completed!")
    return model


def evaluate_model(model, X_test, y_test):
    print("📊 Evaluating model...")

    y_pred = model.predict(X_test)

    print("\n🔹 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n🔹 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # Save image
    plt.savefig("outputs/confusion_matrix.png")
    plt.show()