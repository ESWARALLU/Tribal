from .ml_utils import predict_sentiment

label, score = predict_sentiment("I love this product!")
print(label, score)
