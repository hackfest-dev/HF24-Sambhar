# MACHINE LEARNING MODELS

> There are three versions of the machine learning models used for predictions and are tested in the database to select the precise model for our application.
#### 1) DecisionTreeRegressor
#### 2) DecisionTreeRegressor with Gradient Boost
#### 3) DecisionTreeRegressor with extreme Gradient Boosting XGBoost

> We have also used heuristic based approach for prediction as in the Fractional Knapsack based on Greedy Strategy

Model that will be Integrated is the DecisionTreeRegressor with XGBoost

### DecisionTreeRegressor
This model is although suitable for large scale data the constraint comes in the case of computational power required by the system. In each iteration at each level of the tree we take all possible combinations to find the best split to take the decision. If the number of feature is h then aymptotically,
O ( 2 ^ h ) is the time taken by the model. So for each record the model needs such a computational power and time to train.

> To reduce this time complexity we go gradient based boosting procedure.

> Gradient = Slope so we sort the features at each node in each level of tree as we go by to adjacently compare and find the best split.

### DecisionTreeRegressor with Extreme Gradient Boosting XGBoost
In this we implement the above said procedure which reduces the computational requirements directly to O( h + h * log h ) [ Merge sort + h - 1 splits]

So it has been devised to use the DecisionTreeRegressor with XGBoost.


