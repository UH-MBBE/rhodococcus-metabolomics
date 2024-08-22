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
