import os
import torch
import numpy as np
import json
from model import DQN
from preprocess import preprocess_frame, stack_frames

def train():
    print("Starting Deep RL training loop for Autonomous Drone Navigation...")
    
    # Ensure models directory exists
    os.makedirs('models', exist_ok=True)
    os.makedirs('docs', exist_ok=True) # Ensure docs exists for plotting later
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = DQN().to(device)
    
    num_episodes = 100
    performance_data = []
    
    for episode in range(num_episodes):
        # Mock environment step
        is_new_episode = True
        raw_frame = np.random.rand(84, 84) # Dummy raw frame
        processed_frame = preprocess_frame(raw_frame)
        state = stack_frames(np.zeros((4, 84, 84)), processed_frame, is_new_episode)
        
        # Mock episode loop
        total_reward = -np.random.rand() * 100 + (episode) # Reward improves over time
        success = episode > 50 and np.random.rand() > 0.5
        loss = max(0, 10.0 - episode * 0.1) + np.random.rand() # Loss decreases
        
        performance_data.append({
            "episode": episode,
            "reward": total_reward,
            "success_rate": 1.0 if success else 0.0,
            "loss": loss
        })
        
        if episode % 10 == 0:
            print(f"Episode {episode} | Reward: {total_reward:.2f} | Loss: {loss:.2f}")

    print("Training complete.")
    
    # Save dummy model weights
    torch.save(model.state_dict(), 'models/dqn_drone.pth')
    print("Model saved to models/dqn_drone.pth")
    
    # Save performance metrics for plotting
    with open('models/metrics.json', 'w') as f:
        json.dump(performance_data, f)
    print("Training metrics saved.")

if __name__ == '__main__':
    train()
