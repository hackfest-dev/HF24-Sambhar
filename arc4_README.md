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
> Time complexity involved in model training and prediction for each data update.

> To allocate the amount that can be invested based on the total budget should is 

> Model needed or greedy strategy with heuristic of fractional knapsack will solve the 

> Problem in O(n * nl*og ( n )  ) instead of 2^n - go with XGBoosts.







## Context and Scope












## Solution Strategy

> Use Decision Tree Regressor or Random Forest Regressor to predict the budget allocation. Fine tune the parameters to achieve less error.

> Use matplotlib or other visualisation methods and use PCA to show the overall statistical summary.

### Parameters needed:

> Stock status per item_id and item_name as a bar plot.(to know the raw material status)
> Company vs quantity procured per item_id for current week.(to know the customer)
> Price vs item as a linear graph and use this parameter in machine learning to predict the future price as well (stock price).
> Finished product vs quantity. (amount of finished stock for selling)



