# DOI model
This is just a demo of the doi model 


There is two model in the project 
1. MLP model for rollout
2. PPO(using MLP for policy) 

## How to run 
1. `pip install -r requirements.txt`
1. `python doi_model.py` to create the world model
2. `python env.py` to create the environment and train the ppo


## What's more 
the planning in the model space, could also use the MPC or Other things

## Todo
- [ ] more precise transition function
- [ ] more precise ppo training process