from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

def get_pca_coordinates(df):
    # define and run the PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    # create a dataframe with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])
    principal_df.index = df.index

    # add the group to the dataframe for color of the points
    principal_df['Group'] = [label.split('_')[1] for label in principal_df.index]

    # Make a dataframe of the loading scores for the first and second principal components
    ls_df = pd.DataFrame(pca.components_, columns=df.columns, index=['Principal Component 1', 'Principal Component 2'])

    ls_df = ls_df.T

    ls_df['abs_distance'] = [np.sqrt(ls_df.loc[row, 'Principal Component 1']**2 + ls_df.loc[row, 'Principal Component 2']**2) for row in ls_df.index]

    ls_df = ls_df.sort_values('abs_distance', ascending=False)

    return principal_df, ls_df

# intracellular_gc_ms_pca, intracellular_gc_ms_ls = get_pca_coordinates(intracellular_df)

# display(intracellular_gc_ms_pca)

# intracellular_gc_ms_ls
