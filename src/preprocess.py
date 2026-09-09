import numpy as np

def stack_frames(stacked_frames, frame, is_new_episode):
    if is_new_episode:
        # Clear our stacked_frames
        stacked_frames = np.stack([frame] * 4, axis=0)
    else:
        # Append frame to deque, then stack
        stacked_frames = np.append(stacked_frames[1:, :, :], np.expand_dims(frame, axis=0), axis=0)
        
    return stacked_frames

def preprocess_frame(frame):
    # Mock downsampling and normalization
    # Frame is assumed to be raw camera input
    # Here we just generate a random 84x84 normalized frame for the mock
    return np.random.rand(84, 84).astype(np.float32)
