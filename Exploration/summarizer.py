from transformers import pipeline

def summarizeText(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("pipeline created")
    summary = summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)
    print(summary[0])


if __name__ == "__main__":
    summarizeText("")
