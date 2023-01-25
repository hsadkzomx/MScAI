/*
 * Sample implementation of a Gridworld environment, using a Q-learning agent
 * Dr. Patrick Mannion, University of Galway
 */

package ie.nuig.rlintro;

import java.util.ArrayList;

public class Environment {

	// environment parameters
	private int numActions = 4;
	private String[] actionLabels = new String[] {"North","East","South","West"};
	private static int xDimension = 10;
	private static int yDimension = 10;
	private int numEpisodes = 1000;
	private int maxTimesteps = 100;
	private boolean debug = false; // set to true to enable console output for debugging
	private boolean goalReached = false;
	private int[] goalLocationXY = new int[] {6,6};
	private int[] agentStartXY = new int[] {2,2};
	private float goalReward = 10.0f;
	private float stepPenalty = -1.0f;
	
	// Agent parameters
	private Agent agent;
	private int[] currentAgentCoords = new int[]{-1,-1}; // agent's current x,y position (state vector)
	private int[] previousAgentCoords  = new int[]{-1,-1};; // agent's previous x,y position (state vector)
	private float alpha = 0.10f;
	private boolean alphaDecays = false;
	private float alphaDecayRate = 0.9f;
	private float gamma = 1.0f;
	private float epsilon = 0.10f;
	private boolean epsilonDecays = false;
	private float epsilonDecayRate = 0.9f;
	
	// data logging
	ArrayList<Integer> movesToGoal = new ArrayList<Integer>();
	
	public Environment() {
		
	}
	
	public void setupAgent() {
		agent = new Agent(getNumStates(),numActions,alpha,gamma,epsilon);
		if(debug) {
			agent.enableDebugging();
		}
	}
	
	public void doExperiment() {
		setupAgent();
		for(int e=0;e<numEpisodes;e++) {
			if(debug) {
				System.out.println("\nEnvironment: *************** Episode " + e + " starting ***************");
			}
			doEpisode();
		}
				
	}	
	
	public void doEpisode() {
		int stepsTaken = 0;	// performance metric, see slide # 
		currentAgentCoords[0] = agentStartXY[0]; // reset agent position
		currentAgentCoords[1] = agentStartXY[1];
		goalReached = false;
		
		for(int t=0; t<maxTimesteps;t++) {
			if(!goalReached) {
				if(debug) {
					System.out.println("\nEnvironment: *************** Timestep " + t + " starting ***************");
				}
				doTimestep();
				stepsTaken++;
			}
			else {
				break;
			}
		}
		
		// wrap up episode
		decayAlpha();
		decayEpsilon();
		movesToGoal.add(stepsTaken);
	}
	
	public void doTimestep() {
		int currentStateNo = Utilities.getStateNoFromXY(currentAgentCoords, new int[] {xDimension,yDimension});
		int selectedAction = agent.selectAction(currentStateNo);
		previousAgentCoords = currentAgentCoords;
		currentAgentCoords = getNextStateXY(previousAgentCoords, selectedAction);		
		float reward = calculateReward(previousAgentCoords, selectedAction, currentAgentCoords);
		int nextStateNo = Utilities.getStateNoFromXY(currentAgentCoords, new int[] {xDimension,yDimension});
		agent.updateQValue(currentStateNo, selectedAction, nextStateNo, reward);	
		if(debug) {
			System.out.println("Environment: previousState [" + previousAgentCoords[0] + "," + previousAgentCoords[1] + "]; selected move " + actionLabels[selectedAction] + "; currentState [" + currentAgentCoords[0] + "," + currentAgentCoords[1] + "];");
		}
	}
	
	// Implementation of the Environment Reward Function (see slides #13, #21)
	public float calculateReward(int[] previousAgentCoords, int selectedAction, int[] currentAgentCoords) {
		float reward = 0.0f;
		// check if the goal state has been reached
		if(currentAgentCoords[0] == goalLocationXY[0] && currentAgentCoords[1] == goalLocationXY[1]) {
			reward = goalReward;
			goalReached = true;
		}
		else {
			reward = stepPenalty;
		}
		return reward;
	}
	
	// Models environment transitions (i.e. returns the next state s', given the current state and selected action (see slide #19)
	public int[] getNextStateXY(int[] currentStateXY, int action) {
		// work out the agent's next position, x=0 y=0 is at the bottom left corner of the grid
		// actions which would move the agent off the grid will leave its position unchanged		
		int[] nextStateXY = new int[] {-1,-1};
		
		if(action == 0) { // move north
			if(currentStateXY[1] < yDimension-1) { // ensure agent is not at northmost row
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]+1};
			}
			else { // keep agent at current position if this action would move it off the grid
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]};
			}
		}
		else if(action == 1) { // move east
			if(currentStateXY[0] < xDimension-1) { // ensure agent is not at eastmost column
				nextStateXY = new int[] {currentStateXY[0]+1,currentStateXY[1]};
			}
			else { // keep agent at current position if this action would move it off the grid
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]};
			}
		}
		else if(action == 2) { // move south
			if(currentStateXY[1] > 0) {  // ensure agent is not at southmost row
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]-1};
			}
			else { // keep agent at current position if this action would move it off the grid
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]};
			}
		}
		else if(action == 3) { // move west
			if(currentStateXY[0] > 0) { // ensure agent is not at westmost column
				nextStateXY = new int[] {currentStateXY[0]-1,currentStateXY[1]};
			}
			else { // keep agent at current position if this action would move it off the grid
				nextStateXY = new int[] {currentStateXY[0],currentStateXY[1]};
			}
		}
				
		return nextStateXY;
	}
		
	public int getNumStates() {
		return xDimension * yDimension;
	}
	
	public void enableDebugging() {
		this.debug = true;
	}
	
	public void disableDebugging() {
		this.debug = false;
		agent.disableDebugging();
	}
	
	public void decayAlpha() {
		if(alphaDecays) {
			alpha = alpha*alphaDecayRate;
			agent.setAlpha(alpha);
		}
	}
	
	public void decayEpsilon() {
		if(epsilonDecays) {
			epsilon = epsilon*epsilonDecayRate;
			agent.setEpsilon(epsilon);
		}
	}
	
	public ArrayList<Integer> getMovesToGoal() {
		return movesToGoal;
	}
	
	public float [][] getQTable() {
		return agent.copyQTable();
	}
	
	public static int getXDimension() {
		return xDimension;
	}
	
	public static int getYDimension() {
		return yDimension;
	}
}
