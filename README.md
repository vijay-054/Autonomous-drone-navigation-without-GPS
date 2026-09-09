## 📌 Project Overview & Description

### **Project Title**

**Autonomous Drone Navigation in GPS-Denied Environments using Deep Q-Networks (DQN)**

### **Developer Details**

* **Name:** Vijay Raj V.
* **Institution:** Sri Krishna College of Technology (SKCT)
* **Domain:** Deep Learning / Deep Reinforcement Learning / Computer Vision

---

### **1. Professional Abstract (3-Sentence Description)**

> "This project develops an autonomous vision-based navigation framework for quadcopters operating in challenging, GPS-denied environments where traditional satellite localization is unavailable. By leveraging a Deep Q-Network (DQN) architecture, the agent learns optimal collision avoidance and target-seeking trajectories relying strictly on raw visual sensory streams, specifically optical flow vectors and depth mapping arrays. The end-to-end framework maps raw state-space images directly into discrete motion control actions, demonstrating how Deep Reinforcement Learning can replace heavy hardware sensor arrays for localized navigation."

---

### **2. System Architecture & Methodology**

The pipeline processes visual configurations in an end-to-end fashion:

1. **State Preprocessing:** The environment captures depth data and optical flow profiles. The frame-processing pipeline downsamples raw visual inputs to 84x84 resolution, normalizes pixel intensities, and stacks **4 consecutive frames** together. Stacking captures the temporal element (motion velocity and direction) within a static 2D frame.
2. **Neural Network Brain (DQN):** The state tensor is fed into a dual-stream Convolutional Neural Network (CNN) that extracts spatial features, flattens them, and passes them through Fully Connected (Dense) layers.
3. **Action Value Extraction:** The output layer yields predicted Q-values (Q(s, a)) corresponding to 4 discrete actions:
* `Move Forward`
* `Turn Left`
* `Turn Right`
* `Hover`



---

### **3. Project Directory Tree**

Your workspace layout maps explicitly to the modules you executed:

```text
DL_Autonomous_Drone_Navigation/
├── docs/
│   └── training_performance.png   # Generated evaluation plot
├── models/
│   └── dqn_drone.pth             # Saved PyTorch model weights
├── src/
│   ├── model.py                  # PyTorch CNN-DQN Architecture
│   ├── preprocess.py             # Frame stacking & normalization logic
│   ├── train.py                  # Main Deep RL training loop & mock env
│   └── plot.py                   # Matplotlib performance visualization
├── README.md                     # GitHub main documentation file
└── requirements.txt              # Project package dependencies

```

---

### **4. Technical Key Performance Metrics**

Your model evaluates performance based on standard Deep Reinforcement Learning diagnostics:

* **Cumulative Reward:** The total scalar reward accumulated per episode. An upward trend towards 0 indicates successful navigation and crash avoidance.
* **Success Rate Percentage:** The rolling percentage of flight trials where the agent reaches its target coordinate safely within the max step limit.
* **Bellman Equation Loss Convergence:** The Mean Squared Error (MSE) tracking how accurately the network estimates state-action values.

---

### **How to Run This Right Now in Your IDX Terminal:**

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the training loop (generates models/dqn_drone.pth)
python src/train.py

# Step 3: Plot the results (generates docs/training_performance.png)
python src/plot.py

```
