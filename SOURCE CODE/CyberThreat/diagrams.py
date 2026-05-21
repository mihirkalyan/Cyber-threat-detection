"""
Run this script once to generate architecture and use-case diagram PNGs.
Output saved to assets/architecture.png and assets/usecase.png
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def draw_architecture():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('#f8f9fa')

    ax.text(7, 9.5, 'Cyber Threat Detection — System Architecture',
            ha='center', va='center', fontsize=14, fontweight='bold', color='#2c3e50')

    det_box = FancyBboxPatch((0.5, 5.2), 13, 3.8, boxstyle="round,pad=0.1",
                              linewidth=2, edgecolor='#2980b9', facecolor='#ebf5fb')
    ax.add_patch(det_box)
    ax.text(7, 8.7, 'DETECTION LAYER', ha='center', fontsize=11,
            fontweight='bold', color='#2980b9')

    components_det = [
        (1.5, 7.5, 'KDD99\nDataset', '#3498db'),
        (4.0, 7.5, 'TF-IDF\nPreprocessing', '#3498db'),
        (6.5, 7.5, 'Event Vector\nSplit (80/20)', '#3498db'),
    ]
    model_labels = ['LSTM', 'DNN', 'SVM', 'KNN', 'RF', 'NB', 'DT']
    for i, label in enumerate(model_labels):
        components_det.append((1.0 + i * 1.8, 6.0, label, '#1a5276'))

    for x, y, label, color in components_det:
        box = FancyBboxPatch((x - 0.6, y - 0.4), 1.2, 0.8,
                              boxstyle="round,pad=0.05", linewidth=1.5,
                              edgecolor=color, facecolor='white')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
                fontweight='bold', color=color)

    for x in [2.1, 4.6]:
        ax.annotate('', xy=(x + 1.4, 7.5), xytext=(x, 7.5),
                    arrowprops=dict(arrowstyle='->', color='#2980b9', lw=1.5))
    ax.annotate('', xy=(7.0, 6.5), xytext=(7.0, 7.1),
                arrowprops=dict(arrowstyle='->', color='#2980b9', lw=1.5))
    ax.text(7.0, 5.5, 'Metrics Dashboard\n(Accuracy, Precision, Recall, F1)',
            ha='center', va='center', fontsize=9, color='#1a5276',
            bbox=dict(boxstyle='round', facecolor='#d6eaf8', edgecolor='#2980b9'))

    ax.annotate('', xy=(7, 4.8), xytext=(7, 5.2),
                arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2))
    ax.text(7.5, 5.0, 'Threat Label', ha='left', fontsize=8, color='#27ae60', style='italic')

    intel_box = FancyBboxPatch((0.5, 1.0), 13, 3.6, boxstyle="round,pad=0.1",
                                linewidth=2, edgecolor='#27ae60', facecolor='#eafaf1')
    ax.add_patch(intel_box)
    ax.text(7, 4.3, 'INTELLIGENCE LAYER  (Proposed RAG Bridge)',
            ha='center', fontsize=11, fontweight='bold', color='#27ae60')

    intel_components = [
        (2.5, 3.0, 'Template\nKnowledge Base\n(MITRE ATT&CK / CVE)', '#1e8449'),
        (7.0, 3.0, 'Brief\nRenderer', '#1e8449'),
        (11.5, 3.0, 'Analyst-Readable\nThreat Brief', '#1e8449'),
    ]
    for x, y, label, color in intel_components:
        box = FancyBboxPatch((x - 1.4, y - 0.6), 2.8, 1.2,
                              boxstyle="round,pad=0.05", linewidth=1.5,
                              edgecolor=color, facecolor='white')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
                fontweight='bold', color=color)

    for x_from, x_to in [(3.9, 5.6), (8.4, 10.1)]:
        ax.annotate('', xy=(x_to, 3.0), xytext=(x_from, 3.0),
                    arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1.5))

    ax.text(7, 1.5, '[Simulated RAG — Production: Vector DB + LLM generates explanation]',
            ha='center', fontsize=8, color='#7f8c8d', style='italic')

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, 'architecture.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")


def draw_usecase():
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('#f8f9fa')

    ax.text(6, 8.6, 'Cyber Threat Detection — Use Case Diagram',
            ha='center', fontsize=13, fontweight='bold', color='#2c3e50')

    sys_box = FancyBboxPatch((2.5, 0.5), 7, 7.5, boxstyle="round,pad=0.1",
                              linewidth=2, edgecolor='#2c3e50', facecolor='white')
    ax.add_patch(sys_box)
    ax.text(6, 7.7, 'Threat Detection System', ha='center', fontsize=10,
            fontweight='bold', color='#2c3e50')

    use_cases = [
        (6, 6.8, 'Upload Dataset'),
        (6, 5.9, 'Preprocess Data (TF-IDF)'),
        (6, 5.0, 'Generate Event Vector'),
        (6, 4.1, 'Train & Compare Models'),
        (6, 3.2, 'View Metrics Dashboard'),
        (6, 2.3, 'Generate Threat Brief'),
        (6, 1.4, 'View Architecture Report'),
    ]
    for x, y, label in use_cases:
        ellipse = mpatches.Ellipse((x, y), 3.6, 0.6, linewidth=1.5,
                                    edgecolor='#2980b9', facecolor='#d6eaf8')
        ax.add_patch(ellipse)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, color='#1a5276')

    def draw_actor(x, y, label):
        head = plt.Circle((x, y + 0.5), 0.2, color='#2c3e50')
        ax.add_patch(head)
        ax.plot([x, x], [y + 0.3, y - 0.3], color='#2c3e50', lw=2)
        ax.plot([x - 0.3, x + 0.3], [y + 0.1, y + 0.1], color='#2c3e50', lw=2)
        ax.plot([x, x - 0.25], [y - 0.3, y - 0.7], color='#2c3e50', lw=2)
        ax.plot([x, x + 0.25], [y - 0.3, y - 0.7], color='#2c3e50', lw=2)
        ax.text(x, y - 0.95, label, ha='center', fontsize=8, fontweight='bold', color='#2c3e50')

    draw_actor(1.2, 5.0, 'Security\nAnalyst')
    draw_actor(10.8, 3.5, 'System\n(ML Engine)')

    for _, y, _ in use_cases:
        ax.plot([1.6, 4.2], [5.0, y], color='#7f8c8d', lw=1, linestyle='-')

    for _, y, _ in use_cases[3:6]:
        ax.plot([7.8, 10.3], [y, 3.5], color='#7f8c8d', lw=1, linestyle='--')

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, 'usecase.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")


if __name__ == "__main__":
    draw_architecture()
    draw_usecase()
    print("All diagrams generated in assets/")
