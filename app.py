from textblob import TextBlob
import pandas as pd

comments = [
    "One of the best articles ever written on the topic. It clearly reflects the differences without any unnecessary details and is really to the point. Great job, Shweta!",
    "I love reading manhwa! The art style is amazing.",
    "Manga is so much better than manhwa.",
    "Both have their unique styles and stories.",
    "I dislike manhwa. The pacing is too slow.",
    "Manga has better character development.",
    "I enjoy both equally!",
    "Manhwa often has better color schemes.",
    "I find manga to be more engaging."
]

#creating function to analyze each comment.
def analyze_sentiment(comments):
    results = {'positive':0, 'negative': 0}

    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            results['positive'] += 1
        elif analysis.sentiment.polarity < 0:
            results['negative'] += 1

    return results

 #calling the function and summarizing the results.

sentiment_results = analyze_sentiment(comments)

total_comments = sum(sentiment_results.values())
positive_percentage = (sentiment_results['positive']/ total_comments) * 100
negative_percentage = (sentiment_results['negative']/ total_comments) * 100

summary = {
    'total_comments': total_comments,
    'positive_comments': sentiment_results['positive'],
    'negative_comments': sentiment_results['negative'],
    'positive_percentage': positive_percentage,
    'negative_percentage': negative_percentage
}

print(summary)
