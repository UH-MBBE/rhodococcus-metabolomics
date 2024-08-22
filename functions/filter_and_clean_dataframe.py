import pandas as pd
### Define a function to remove rows that are not in the labels_to_keep list
# Note: this function only keeps columns with names in the labels to keep list, and only keeps metabolites where 50% of samples have detected it

# define a function to remove rows that are not in the labels_to_keep list
def filter_and_clean_dataframe(df, labels_to_keep, filter_unknowns=False):
    df = df.copy()

    new_rows = []

    # loop through the rows of the dataframe and only keep the rows that are in the labels_to_keep list
    for index, row in df.iterrows():
        if index in labels_to_keep:
            new_rows.append(row)

    df = pd.DataFrame(new_rows)

    cols_to_drop = []

    # loop over the columns and remove the columns that are all NaN or all 0
    for column in df.columns:
        # get the values of the column
        col_values = df[column].values

        # determine the fraction of NaN values in the column
        zero_values = [value for value in col_values if float(value) == 0]

        # determine the fraction of 0 values in the column
        zero_fraction = len(zero_values) / len(col_values)

        # if the fraction of NaN values is greater than 0.5, add the column to the list of columns to drop
        if zero_fraction >= 0.5:
            cols_to_drop.append(column)

        if filter_unknowns and 'unknown' in column.lower():
            cols_to_drop.append(column)

    # drop the columns in the list
    df = df.drop(cols_to_drop, axis=1)

    return df

# intracellular_df = filter_and_clean_dataframe(intracellular_df, labels_to_keep)
# intracellular_df