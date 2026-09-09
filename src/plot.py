import json
import matplotlib.pyplot as plt
import os

def plot_metrics():
    metrics_file = 'models/metrics.json'
    if not os.path.exists(metrics_file):
        print("Metrics file not found. Run train.py first.")
        return
        
    with open(metrics_file, 'r') as f:
        data = json.load(f)
        
    episodes = [d['episode'] for d in data]
    rewards = [d['reward'] for d in data]
    losses = [d['loss'] for d in data]
    
    # Smooth success rate
    success_rates = [d['success_rate'] for d in data]
    window = 10
    smoothed_success = [sum(success_rates[max(0, i-window):i+1])/len(success_rates[max(0, i-window):i+1]) for i in range(len(success_rates))]

    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    
    axs[0].plot(episodes, rewards, color='blue', alpha=0.6)
    axs[0].set_title('Cumulative Reward per Episode')
    axs[0].set_xlabel('Episode')
    axs[0].set_ylabel('Reward')
    axs[0].grid(True)
    
    axs[1].plot(episodes, smoothed_success, color='green', linewidth=2)
    axs[1].set_title('Success Rate (%)')
    axs[1].set_xlabel('Episode')
    axs[1].set_ylabel('Success Rate')
    axs[1].grid(True)
    
    axs[2].plot(episodes, losses, color='red', alpha=0.6)
    axs[2].set_title('Bellman Equation Loss Convergence')
    axs[2].set_xlabel('Episode')
    axs[2].set_ylabel('MSE Loss')
    axs[2].grid(True)
    
    plt.tight_layout()
    
    os.makedirs('docs', exist_ok=True)
    save_path = 'docs/training_performance.png'
    plt.savefig(save_path)
    print(f"Plot saved to {save_path}")

if __name__ == '__main__':
    plot_metrics()
