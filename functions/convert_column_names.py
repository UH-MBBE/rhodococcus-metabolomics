# Define a function to convert the column names to descriptive labels
def convert_column_names(df, metadata_df):
    # create a new list to store the new column names
    new_columns = []
    
    # loop over the columns in the dataframe
    for column in df.columns:
        # get the descriptive label for the column
        new_label = get_descriptive_label(metadata_df, column)
        
        # append the new label to the new_columns list
        new_columns.append(new_label)
    
    # set the columns of the dataframe to the new_columns list
    df.columns = new_columns
    
    return df

# Define a function that takes in a 'Label' and converts it to a 'descriptive_label'
def get_descriptive_label(df, label):
    # clean up the label name
    label = label.replace('In ', '')
    label = label.replace('Ex ', '')
    
    # loop over the rows of metadata to find the row with the matching label
    for _, row in df.iterrows():
        if row['Label'] == label:
            return row['descriptive_label']
    
    # handle the error if the label is not found
    print(f'No descriptive label found for {label}')
    return label
