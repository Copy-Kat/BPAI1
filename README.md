# Food Entity Extraction with Regular Expressions (RE) and Conditional Random Fields (CRF)

## To start:
- Clone the repository.
- Install the dependencies (Can start a new virtual environment if needed).
- Run all cells in explore.ipynb to generate the dataset used in experiments (The final datasets used in experiments are already included but they can be generated again using this notebook).

## Ingredient tree:
- Run test_dict.ipynb first to separate all the ingredients in different token length (This is not recommended as the file is very large and could break the current system. The existing separation is already sufficient for the experiments)
- Run test_dict_2.ipynb after to generate the ingredient tree. The final tree is named tree.json

## Regular expressions:
- Run all cells in regex_test_clean.ipynb for all the RE experiments.
- The whole model is broken down into 3 parts:
  - The pure RE is in the third cell.
  - The Grammar RE is in the next cell.
  - The filtering in between the 2 REs are included in the evaluation function.
  - Noted that filtering is heavily related to the pure RE section so any changes to the RE should be reflected in the filters as well.
- The evaluation is at the end of the file.
 
## Conditional Random FIelds:
- The feature generation function is named "word2featuresBase".
  - This function can be modified by changing the feature included for each token.
  - All the functions used in feature generation are all on top of the file.
- The cross-validation function is commented out. It is not recommended to run all cells with this enabled as it can take a long time to complete.
- The evaluation is at the end of the file.
