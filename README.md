# task_1

### Tools Used :- Pandas

### Dataset Used:- Netflix_titles


###  Key Steps in the Script:

1. **Load the Dataset**

   * Reads `netflix_titles.csv` using `pandas`.

2. **Remove Duplicates**

   * Ensures uniqueness of records with `drop_duplicates()`.

3. **Handle Missing Values**

   * Fills null values in:

     * `country`, `rating`, `director`, `duration` → `'Unknown'`
     * `cast` → empty string
   * Converts `date_added` to datetime (with `errors='coerce'`).

4. **Text Cleanup**

   * Strips whitespace from fields: `title`, `director`, `country`.

5. **Transform Complex Fields**

   * Splits `cast` and `listed_in` strings into Python lists.

6. **Feature Engineering**

   * Extracts `year_added` and `month_added` from `date_added`.
   * Creates `num_cast` and `num_genres` to quantify each record's size.

7. **Save Cleaned Dataset**

   * Exports the final cleaned DataFrame to `cleaned_netflix_dataset.csv`.

8. **Completion Message**

   * Prints a success confirmation in the terminal.

### Output:

* **File**: `cleaned_netflix_dataset.csv`
