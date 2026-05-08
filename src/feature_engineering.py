def create_features(df):
    df['price_per_sqft'] = df['price'] / df['area']
    return df
