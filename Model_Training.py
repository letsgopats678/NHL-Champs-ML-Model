
from Preprocessing import training_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from collections import defaultdict
import json


combined_df = pd.json_normalize(training_data, sep='_').fillna(0)

# Display the first few rows of the DataFrame to check the column names
#print(combined_df.head())


# Updates the column data processing
stanley_cup_champion_col = 'Playoff History_Stanley Cup Champion'
if stanley_cup_champion_col in combined_df.columns:
    combined_df[stanley_cup_champion_col] = combined_df[stanley_cup_champion_col].apply(lambda x: 1 if x == "YES" else 0)


if stanley_cup_champion_col in combined_df.columns:
    X = combined_df.drop([stanley_cup_champion_col], axis=1)
    y = combined_df[stanley_cup_champion_col]



    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #Splits the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    #Defines the logistic regression model
    model = LogisticRegression()

    #Trains the model
    model.fit(X_train, y_train)

    # Predict on the testing set
    y_pred = model.predict(X_test)

    #Evaluates the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Test Accuracy: {accuracy:.4f}')

    print('Classification Report (Test Data):')
    print(classification_report(y_test, y_pred))

    print('Confusion Matrix (Test Data):')
    print(confusion_matrix(y_test, y_pred))























