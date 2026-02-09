from transformers import pipeline

# Load a tiny sentiment-analysis model
classifier = pipeline("sentiment-analysis")

def classify(text):
    result = classifier(text)[0]
    label = result["label"]
    score = round(result["score"], 3)
    return f"{label} ({score})"

if __name__ == "__main__":
    sample = input("Enter text to classify: ")
    print(classify(sample))

