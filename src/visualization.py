import matplotlib.pyplot as plt

def plot_label_distribution(df):
    plt.figure()
    df['label'].value_counts().plot(kind='bar')
    plt.title("Normal vs Attack Distribution")
    plt.xlabel("Label (0 = Normal, 1 = Attack)")
    plt.ylabel("Count")
    plt.savefig("outputs/label_distribution.png")
    plt.savefig("outputs/label_distribution.png")
    plt.close()   # ✅ add this
print("📊 Plotting label distribution...")
