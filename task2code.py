import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv('/kaggle/input/customer-support-tickets-futureinterns/customer_support_tickets.csv')

# Preview data
print("First few records:\n", df.head(), "\n")
print("Columns:\n", df.columns, "\n")

# Combine all text from the 'Issue' or similar column
text_data = ""

# Assuming a column named 'Issue' or similar
for col in df.columns:
    if 'issue' in col.lower() or 'description' in col.lower():
        text_data = ' '.join(df[col].dropna().astype(str))
        break

# Text preprocessing
tokens = word_tokenize(text_data.lower())
tokens = [word for word in tokens if word.isalpha()]  # remove numbers/punctuation
filtered_words = [word for word in tokens if word not in stopwords.words('english')]

# Count common issues
word_freq = Counter(filtered_words)
common_issues = word_freq.most_common(10)

print("🔧 Most Frequently Reported Issues:")
for issue, freq in common_issues:
    print(f"- {issue}: {freq} times")

# Recommendations (example logic based on keywords)
recommendations = []
if 'delay' in text_data or 'late' in text_data:
    recommendations.append("Improve internal ticket routing system to reduce delays.")
if 'refund' in text_data:
    recommendations.append("Implement automated refund tracking and update system.")
if 'login' in text_data or 'password' in text_data:
    recommendations.append("Enhance login/password recovery support and self-service options.")
if 'support' in text_data:
    recommendations.append("Consider extending support hours or adding chatbot assistance.")

# Final Report
print("\n📄 Summary Report:")
print("Most Frequently Reported Problems:")
for issue, freq in common_issues:
    print(f"✔️ {issue.capitalize()} (Reported {freq} times)")

print("\nRecommended Process Improvements:")
for rec in recommendations:
    print(f"➡️ {rec}")
