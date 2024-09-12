import seaborn as sns
import numpy as np

def normalize_pca_df(pc_df):
    pc_df = pc_df.copy()
    max_val = max(pc_df['Principal Component 1'].abs().max(), pc_df['Principal Component 2'].abs().max())
    pc_df['Principal Component 1'] = pc_df['Principal Component 1'] / max_val
    pc_df['Principal Component 2'] = pc_df['Principal Component 2'] / max_val
    return pc_df

# Define the plot_pca_lda function to accept an axis parameter
def plot_pca_lda(ax, pc_df, ls_df, title, arrow_length=0.5):
    # Normalize the PCA DataFrame so that max value in either dimension is 1
    pc_df = normalize_pca_df(pc_df)

    # Scatter plot for PCA points
    sns.scatterplot(x="Principal Component 1", y="Principal Component 2", hue="Group", data=pc_df, s=100, palette='bright', ax=ax)

    # Normalize each loading vector and scale it to the desired length (0.5)
    for i in range(min(10, len(ls_df))):
        row = ls_df.iloc[i]
        norm = np.sqrt(row['Principal Component 1'] ** 2 + row['Principal Component 2'] ** 2)
        if norm != 0:
            ax.arrow(0, 0,
                     (row['Principal Component 1'] / norm) * arrow_length,
                     (row['Principal Component 2'] / norm) * arrow_length,
                     color='blue', alpha=0.7, head_width=0.02, head_length=0.05, linewidth=2)
            ax.text((row['Principal Component 1'] / norm) * arrow_length * 1.2,
                    (row['Principal Component 2'] / norm) * arrow_length * 1.2,
                    ls_df.index[i], color='black', ha='center', va='center', fontsize=10)

    ax.set_title(title, fontsize=24)
    ax.set_xlabel("Principal Component 1", fontsize=16)
    ax.set_ylabel("Principal Component 2", fontsize=16)

    # Set consistent limits for x and y axes
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Set specific ticks for x and y axes
    ticks = [-1, -0.5, 0, 0.5, 1]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    # Remove grid lines
    ax.grid(False)

    # Hide the spines around the plot
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    # Add grid lines at x=0 and y=0
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.7)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.7)

    # Position the legend outside the plot
    ax.legend(loc='best')
