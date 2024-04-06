# INDEX

> Introduction and Goals
> Constraints
> Context and Scope
> Solution Strategy


## Introduction and Goals :

	INTRODUCTION:
> This documentation provides the goals of our project, and the requirements to achieve the goal, the constraints and the method used to overcome them and the solution strategy

	GOALS:
>The model must predict the budget to be allocated for each raw material provided the user gives his budget.

>The model must forecast the overall statistical summary of the stock movement.

>Try to provide a map between the two warehouses using google API.

>The data from the user-end must flow to the back-end and then to the model as the input parameter for testing and the output from the model should be displayed in the same vice-versa way to the user-end seamlessly.



## Constraints:
> Time complexity involved in model training and prediction for each data update To allocate the amount that can be invested based on the total budget should is Model needed or greedy strategy with heuristic of fractional knapsack will solve the Problem in O(n * nl*og ( n )  ) instead of 2^n - go with XGBoosts.

> Rainy day of our system.

> Making generic for physical inventory as well as for a digital inventory.






## Context and Scope

> Is a generic model that can be used by any kind of inventory system along with even digital inventory systems.
> Especially designed for SMEs



## Solution Strategy

> Provide data integrity by having the data access restrictions following the Three Schema Architecture.

> Use Decision Tree Regressor or Random Forest Regressor with gradient based boosting to predict the budget allocation. Fine tune the parameters to achieve less error.

> Use matplotlib or other visualisation methods to show the overall statistical summary and to forecast the predictions.

> Runs in docker so that the system is compatible with any machine.




