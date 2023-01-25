/*
 * Sample implementation of a Q-learning agent, using a tabular Q value store and epsilon-greedy action selection
 * Dr. Patrick Mannion, National University of Ireland Galway
 * Slide numbers reference the lecture notes file ML_04_ReinforcementLearning.pdf
 */

package ie.nuig.rlintro;

public class Agent {
	
	// Q table parameters	
	private int numStates;
	private int numActions;
	private float[][] qTable; // Slide #36, tabular q value store, [stateNumber, actionNumber]	

	// agent parameters, default values
	private float alpha = 0.1f; // Slide #37, learning rate
	private float gamma = 0.9f; // Slide #27, discount factor
	private float epsilon = 0.1f; // Slide #38, exploration rate
	private boolean debug = false; // set to true to enable console output for debugging
	
	// constructor with default agent parameters
	public Agent(int numStates,int numActions) {
		this.numStates = numStates;
		this.numActions = numActions;
		initialiseQvalues();
	}
	
	// constructor with specified agent parameters
	public Agent(int numStates, int numActions, float alpha, float gamma, float epsilon) {
		this.numStates = numStates;
		this.numActions = numActions;
		this.alpha = alpha;
		this.gamma = gamma;
		this.epsilon = epsilon;
		initialiseQvalues();
	}

	private void initialiseQvalues() {
		qTable = new float[numStates][numActions];

		// set q values initially to 0
		for(int i=0;i<numStates;i++) {
			for(int j=0; j<numActions;j++) {
				qTable[i][j] = 0.0f;
			}
		}
	}

	public void updateQValue(int previousState, int selectedAction, int currentState, float reward) {
		// implementation of Q-learning TD update rule (see slides #37, #47 )
		float oldQ = qTable[previousState][selectedAction];
		float maxQ = getMaxQValue(currentState);
		float newQ = oldQ + alpha*(reward + gamma*maxQ - oldQ);
		qTable[previousState][selectedAction] = newQ;
	}

	public int selectAction(int state) {
		// epsilon-greedy action selection strategy implementation (see slide #38)
		int selectedAction = -1;
		double randomValue = Math.random();
		
		if(debug) {
			System.out.println("Agent: selecting action, epsilon="+epsilon+", randomValue="+randomValue);
		}
		
		if(randomValue<epsilon) { // select a random action with probability epsilon
			selectedAction = selectRandomAction();
			if(debug) {
				System.out.println("Agent: selected action " + selectedAction + " at random");
			}
		}
		else { // else select the most valuable action
			selectedAction = getMaxValuedAction(state);
			if(debug) {
				System.out.println("Agent: selected action " + selectedAction + " greedily");
			}
		}
		return selectedAction;
	}

	public int selectRandomAction() {
		// select a random action between 0 and (numActions-1)
		return (int) (Math.random() * numActions);
	}
	
	public int getMaxValuedAction(int state) {
		// greedy action selection implementation
		// return the index of the most valuable action for a particular state
		int maxIndex = -1;
		float maxValue = -Float.MAX_VALUE;
		for(int action=0;action<numActions;action++) {
			if(qTable[state][action]>maxValue) {
				maxIndex = action;
				maxValue = qTable[state][action];
			}
		}
		return maxIndex;
	}

	public float getMaxQValue(int state) {
		// return the Q value of the most valuable action for a particular state
		int maxIndex = getMaxValuedAction(state);
		return qTable[state][maxIndex];
	}
	
	public void enableDebugging() {
		this.debug = true;
	}
	
	public void disableDebugging() {
		this.debug = false;
	}
	
	public float getAlpha() {
		return this.alpha;
	}
	
	public void setAlpha(float alpha) {
		this.alpha = alpha;
	}
	
	public float getGamma() {
		return this.alpha;
	}
	
	public void setGamma(float gamma) {
		this.gamma = gamma;
	}
	
	public float getEpsilon() {
		return this.epsilon;
	}
	
	public void setEpsilon(float epsilon) {
		this.epsilon = epsilon;
	}
	
	// returns a copy of the agent's Q values table
	public float[][] copyQTable() {
		float[][] copy = new float[numStates][numActions];
		for(int s=0;s<numStates;s++) {
			for(int a=0;a<numActions;a++) {
				copy[s][a] = qTable[s][a]; 
			}
		}
		return copy;
	}
	
	public void setQtable(float[][] values) {
		for(int s=0;s<numStates;s++) {
			for(int a=0;a<numActions;a++) {
				qTable[s][a] = values[s][a]; 
			}
		}
	}
}


