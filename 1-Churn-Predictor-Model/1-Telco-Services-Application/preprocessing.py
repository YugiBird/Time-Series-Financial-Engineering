import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess(df, option):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """
    # Defining the map function
    def binary_map(feature):
        return feature.map({"Yes": 1, "No": 0})

    # Encoding gender category
    df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

    # Encode binary categorical features
    binary_list = [
        # "Gender",
        "Married",
        "Phone_Service",
        "Multiple_Lines",
        #"Internet_Service",
        "Online_Security",
        "Online_Backup",
        "Device_Protection_Plan",
        "Premium_Tech_Support",
        "Streaming_TV",
        #"Streaming_Movies",
        #"Streaming_Music",
        #"Unlimited_Data",
        "Paperless_Billing",
    ]
    df[binary_list] = df[binary_list].apply(binary_map)

    # Drop values based on operational options
    if option == "Online":
        columns = [
            "Gender",
            "Married",
            "Phone_Service",
            "Multiple_Lines",
            "Online_Security",
            "Online_Backup",
            "Device_Protection_Plan",
            "Premium_Tech_Support",
            "Streaming_TV",
            "Paperless_Billing",
            "Number_of_Dependents",
            "Number_of_Referrals",
            "Tenure_in_Months",
            "Monthly_Charge",
            "Offer_Offer_D",
            "Internet_Type_DSL",
            "Internet_Type_Fiber_Optic",
            "Internet_Type_None",
            "Contract_One_Year",
            "Contract_Two_Year",
            "Payment Method_Credit_Card",
        ]
        # Encoding the other categorical categoric features with more than two categories
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    elif option == "Batch":
        pass
        df = df[
            [
                "Gender",
                "Married",
                "Phone_Service",
                "Multiple_Lines",
                "Online_Security",
                "Online_Backup",
                "Device_Protection_Plan",
                "Premium_Tech_Support",
                "Streaming_TV",
                "Paperless_Billing",
                "Number_of_Dependents",
                "Number_of_Referrals",
                "Tenure_in_Months",
                "Monthly_Charge",
                "Offer",
                "Internet_Type",
                "Contract",
                "Payment_Method",
            ]
        ]
        columns = [
            "Gender",
            "Married",
            "Phone_Service",
            "Multiple_Lines",
            "Online_Security",
            "Online_Backup",
            "Device_Protection_Plan",
            "Premium_Tech_Support",
            "Streaming_TV",
            "Paperless_Billing",
            "Number_of_Dependents",
            "Number_of_Referrals",
            "Tenure_in_Months",
            "Monthly_Charge",
            "Offer_Offer_D",
            "Internet_Type_DSL",
            "Internet_Type_Fiber_Optic",
            "Internet_Type_None",
            "Contract_One_Year",
            "Contract_Two_Year",
            "Payment Method_Credit_Card",
        ]
        # Encoding the other categorical categoric features with more than two categories
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    else:
        print("Incorrect operational options")

    return df
