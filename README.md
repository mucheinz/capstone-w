# IBM AI Enterprise Workflow Capstone
Files for the IBM AI Enterprise Workflow Capstone project. 

## Part 1

### Case study part 1

At this point in the project, and in any data science project really, it is best to loosly organize your code as libraries and scripts.  Jupyter notebooks are a convenient and powerful tool, but we have mentioned several times that they are not a good place for source code to live.  

Just run the AAVAIL.part1.ipynb Notebook


### Hints

* The JSON files may not contain uniformly named features. Be sure to account for this in your data ingestion function.
* Some of the invoice ids (`invoice`) have letters that can be removed to improve matching.
* One common way to ready time-series data for modeling is to aggregate the transactions by day. Getting the data into this form will help you prepare for part 2.
* If you have not worked with time-series or time-stamped data before the following two links can be useful.

  * [NumPy datetime](https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html)
  * [Pandas time-series](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
  * [matplotlib time-series plot](https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/date.html)


## Part 2

Have not tackled Flask, Docker - too much at Christmas - will do later