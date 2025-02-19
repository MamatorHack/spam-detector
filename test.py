def predict_spam(message):
    message_transformed = vectorizer.transform([message])
    prediction = model.predict(message_transformed)
    return "SPAM ❌" if prediction[0] == 1 else "HAM ✅"

# Tester avec un message
print(predict_spam("Hey, well ? Ready for competition ?"))
print(predict_spam("Hey, you have winning cup. Give your account bank detail to keep your prize !"))