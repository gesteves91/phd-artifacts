# How to Run the Script

The script is run by typing the following command, assuming you are inside the `src/ch4` folder, and the environment is set up as described in the [README](../../README.md) file:

```bash
python usxgb.py ../../data/jureczko/total.csv
```
The script expects the dataset as a parameter. The dataset must be a `csv`. Furthermore, note that inside the script we specify the features to be used. If you want to use a different set of features, you must change the `WANTED_COLUMNS` constant inside the script.

After starting running the script (which can take hours depending on your dataset), we will have a `pickle` file with the trained model. 