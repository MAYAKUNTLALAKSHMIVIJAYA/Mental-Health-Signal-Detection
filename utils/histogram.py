import matplotlib.pyplot as plt
import os
import uuid

def generate_histogram(emotions, probabilities):
    """
    emotions: list of emotion names
    probabilities: numpy array of probabilities
    """
    os.makedirs("static/temp", exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=120)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    bars = ax.bar(emotions, probabilities, color='#2563eb', edgecolor='#1d4ed8', alpha=0.9, width=0.55)

    ax.set_xlabel("Emotions", fontsize=11, fontweight='600', color='#334155', labelpad=10)
    ax.set_ylabel("Confidence / Probability", fontsize=11, fontweight='600', color='#334155', labelpad=10)
    ax.set_title("Emotion Probability Distribution", fontsize=13, fontweight='bold', color='#0f172a', pad=12)

    ax.tick_params(axis='x', rotation=45, colors='#334155', labelsize=9)
    ax.tick_params(axis='y', colors='#334155', labelsize=9)
    ax.grid(axis='y', linestyle='--', alpha=0.35, color='#cbd5e1')

    # Remove unneeded spines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color('#cbd5e1')

    # Show numbers on top of bars if small number of classes
    if len(emotions) <= 12:
        for bar in bars:
            height = float(bar.get_height())
            if height > 0.01:
                ax.annotate(
                    f"{height:.2f}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    fontsize=8.5,
                    fontweight='600',
                    color='#1e293b'
                )

    unique_id = uuid.uuid4().hex[:8]
    path = os.path.join("static", "temp", f"histogram_{unique_id}.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)

    return path
