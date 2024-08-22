import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

def get_lda_coordinates(df):
    df = df.copy()

    # Add the group to the dataframe for color of the points
    groups = [label.split('_')[1] for label in df.index]

    # Define and run the LDA
    lda = LDA(n_components=None)  # Use all linear discriminants

    # Fit the LDA model
    lda_output = lda.fit_transform(df, groups)

    # Convert the LDA results to a dataframe
    lda_columns = [f'Principal Component {i + 1}' for i in range(lda_output.shape[1])]
    lda_df = pd.DataFrame(data=lda_output, columns=lda_columns)
    lda_df['Group'] = groups

    # Get the coefficients (equivalent to loading scores in PCA)
    lda_coefficients = pd.DataFrame(lda.coef_.T, index=df.columns, columns=[f'LD{i + 1} Coef' for i in range(lda.coef_.shape[0])])

    # Sort the coefficients by their magnitude for the first discriminant (LD1)
    lda_coefficients['abs_LD1_LD2_distance'] = [np.sqrt(lda_coefficients.loc[row, 'LD1 Coef']**2 + lda_coefficients.loc[row, 'LD2 Coef']**2) for row in lda_coefficients.index]
    lda_coefficients = lda_coefficients.sort_values(by='abs_LD1_LD2_distance', ascending=False)

    # rename 'LD' columns to 'Principal Component' columns
    lda_coefficients = lda_coefficients.rename(columns={'LD1 Coef': 'Principal Component 1', 'LD2 Coef': 'Principal Component 2'})

    return lda_df, lda_coefficients

# Example usage:
# intracellular_gc_ms_lda, lda_coefficients = get_lda_coordinates(intracellular_df)
# lda_coefficients
