# Obstacle Tower Challenge - Agent Analysis

The following results have been obtained from an agent trained for the <a href="https://www.aicrowd.com/challenges/unity-obstacle-tower-challenge" target="_blank"> Unity Obstacle Tower Challenge </a>. The agent needs to navigate a maze of rooms to get to a door which leads him one floor up. On the way he can collect blue spheres which supply more time. Starting at level 5, the agent needs to find and pick up a key in order to open certain doors. Starting from level 10, the agent needs to solve puzzles in which he is supposed to push a box onto a designated area for a door to open. The agent shown here can't achieve this yet.

<a href="RL-Encodings-Notebook.html" target="_blank"> Here </a> you can find the Jupyter Notebook used to generate the following figures and animations.


## The Agents Brain and How it Learns
I use proximal policy optimization (PPO) to train the agent. Figure 1 shows the underlying network structure (blue). The agent makes decisions based on visual and vector observations provided by the environment (yellow). Vector observations are composed of the time left, the number of key which the agent possesses and the level in which he finds himself.

![Figure 1](./content/images/NetworkStructure.png "Figure 1: Network Structure")

We will now look at the agents brain in one particular run. Figure 2 shows the overall statistics of this run. You can see that the agent reached level 10 within less than 2000 steps.

![Figure 2](./content/images/Performance_Actions.png "Figure 2: Performance and Action Distribution")

## Activity in the Agents Brain
The following animation shows the embedded layer activations in the agents brain (left) with the corresponding visual observations (right) and the actions which the agent selects. R and V display the obtained reward from the environment and the value estimate respectively.

<div align="center">
<iframe width="600" height="300" frameborder="0" scrolling="no" src="content/anim_encodings.html"></iframe>
</div>

## K-Means Clustering on the Visual Activations
In Figure 3 you can see the distribution of images into 10 clusters calculated with k-means clustering. The clustering is performed on the embedding of the visual observations (256 dimensions). When looking at the images in the different clusters one can make out some semantic patterns. Some cluster contain images where the agent walks through doors or sees other rewarding events coming such as blue spheres or keys (for instance see cluster 0 &1), other clusters contain frames where the agent walks through rooms (cluster 3 & 4) while others contain jumping (cluster 2) or right/left turns (cluster 9).

<div align="center">
<p><img src="./content/images/KMeans_10_Distribution.png" alt="Figure 3" title="Figure 3: K-Means Distribution"></p>
</div>

<a href="content/anim_k-means.html" target="_blank"> Explore Cluster</a>


## PCA on the Activations in the Visual Embedding
Principal component analysis reveals quite a lot of variance in the activations. The first three components explain only 46.68% of the variance and even 20 principal components can explain only 85.57% of the variance.

![Figure 4](./content/images/PCA.png "Figure 4: PCA")

When looking at the K-Means clustered data projected onto the principal component one can see somehow distinct point clouds.

<div align="center">
<p><img src="./content/images/PCA3_Vis_Cluster.png" alt="Figure 5" title="Figure 5: PCA Colored by Cluster"></p>
</div>

## ICA on the Activations in the Visual Embedding
In the animation below you can see the results of an independent component analysis on the network activations in the embedding of the visual input. The independent components are shown on the left, paired the corresponding observations on the right.

<div align="center">
<iframe width="600" height="300" frameborder="0" scrolling="no" src="content/anim_ICA.html"></iframe>
</div>

In figure 6 you can see the correlation between the IC values and the value estimate. Overall the correlation isn't very strong.

<div align="center">
<p><img src="./content/images/ICA_Correlation.png" alt="Figure 6" title="Figure 6: ICA Correlation"></p>
</div>

## Correlation Between Embeddings and Value Estimate

In figure 7 you can see the correlation between the neuron activations in the hidden layer and the value estimate.

<div align="center">
<p><img src="./content/images/Val_Correlation.png" alt="Figure 7" title="Figure 7: Correlation VE - Activations"></p>
</div>

When looking at the most correlated neuron in the visual part of the embedding one can se spikes in the neuron strongly correlated with going through level doors or obtaining other rewards.

<div align="center">
<iframe width="800" height="550" frameborder="0" scrolling="no" src="content/most_cor.html"></iframe>
</div>

When we now look at the visual observations that lead to this neuron being activated we can see that a lot of these observations contain doors and spheres.

<div align="center">
<iframe width="600" height="300" frameborder="0" scrolling="no" src="content/anim_most_corr.html"></iframe>
</div>

## Embeddings Correlated with Actions

Figure 8 shows the correlation between network activations and the four action branches. You can see a stronger correlation with the visual part of the embedding than the vector part.

<div align="center">
<p><img src="./content/images/Act_Correlation.png" alt="Figure 8" title="Figure 8: Correlation Action - Activations"></p>
</div>

## Correlations of Neurons With Each Other
In this display you can see the correlation of each neuron with all the other neurons. If you want to see the visual observations which led to the selected neuron being active click on the button "Active Frames" and they will appear in the display below.

<div align="center">
<iframe width="600" height="700" frameborder="0" scrolling="no" src="content/anim_correlations.html"></iframe>
</div>
