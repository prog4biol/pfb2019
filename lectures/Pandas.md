# Pandas

## What is Pandas?

**Python Data Analysis Library**

A powerful library for manipulating data arranged in tables (i.e. matricies or data frames). It's arguably the most popular Python library used for data engineering. Pandas aims to provide Python users the same type of functionality as the popular statistical language, **R**.



![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/04/Python-Pandas-Applications.jpg)



### Why familiarize yourself with Pandas?

So far we've discussed how you build your own multidimensional objects like lists of lists and dictionaries of dictionaries from raw data. However, bioinformatics modules (and many others) will often **return** results in the form of Pandas **data frame** or **a matrix**. Further manipulation of these results (e.g. filtering, statistical analysis, data reorganization) will require some knowledge of Pandas operations.

For example, lets say you want to parse your RNA-seq results to a list of genes within a specific range of p-values and log fold changes, e.g., all p-values < 1e-15 and log fold changes > 1.2. You can apply your knowledge of Python operators such as `and, >, <` to subset a data frame based on the afformentioned parameters.

#### Pandas has the ability to read in various data formats

- Open a local file using Pandas, usually a comma-separated values (CSV) file, but could also be a tab-delimited text file (TSV), Excel, etc

- Read a remote file on a website through a URL or read data from a remote database.



## Types of data manipulated in Pandas

### Matrices

A matrix is an data structure where numbers are arranged into rows and columns. They will typically conatin floats __or__ integers, but not both. Matrices are used when you need to perform mathmatical operations between datasets that contain multiple dimensions (i.e. measurements for two or more variables that change at the same time).



![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Gene_co-expression_network_construction_steps.png/720px-Gene_co-expression_network_construction_steps.png)

<br/>

### Data frames

A data frame is a table-like data structure and can contain different data types (strings, floats, integers, etc.) in different columns. This is the type of data structure you're used seeing in Excel. Each column should only contain one data type.



![](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0161567.t005&type=large)



## A brief word on vectorization

**Operations in Pandas, like R, work most efficiently when vectorized**



You can think of a vector (also reffered to as an [array](https://docs.python.org/3/library/array.html)) as a type of list that contains a single data type and optimized for parallel computing. For matricies and data frames in Pandas (also NumPy), vectors are rows and columns.

Rather that looping through individual values (scalars), we apply operations to vectors (rows/columns). That is, the vector is treated as a single object. This topic can get a bit complicated, but it is worth doing your homework if you frequently work with these data types. Here's a few articles to get you started:

- [A beginners guide to optimizing pandas code for speed.](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)
- [Why is vectorization faster in general than loops?](https://stackoverflow.com/questions/35091979/why-is-vectorization-faster-in-general-than-loops)
- [Python Lists vs. Numpy Arrays, what's the difference?](https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)




<img src="https://miro.medium.com/max/2060/1*p4zjrqG97C4bFmOXU5UQog.png" width="80%" height="80%" />

Vectorization with Pandas series is **~390x** faster than crude looping



## Basic methods for data manipulation

### Reading in csv files and row/column slicing

"Slicing" refers to subsetting, or extracting rows and columns from a data frame. Here we'll read in a data frame, look at the contents, and subset it by slicing out arbitrary regions.

```
import pandas as pd

# Setting index_col to 0 tells us that the first column contains the row names
cell_attributes = pd.read_csv("./meta_data.csv", index_col = 0)

type(cell_attributes)
``` 

Note: We can read/write data in many other formats like tab delimited text `.tsv` and excel spreadsheets `.xlsx`. Please refer to [this document]() for a full description of Pandas I/O tools.


```
# We notice rows and columns are truncated with the dimensions printed at the bottom
print(cell_attributes)

# Change the output view options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# Does this function seem familiar?
cell_attributes.head(10)
```

#### Slicing

Pandas has different methods for subsetting dataframes.
We'll dicuss the most common methods, **loc**, and **iloc**

**loc** allows us to subset data by row or column label. For example, if I would
like to subset the column 'n_counts', I would use the following command:

```
# The comma separates rows and columns, and the colon returns all rows.
cell_attributes.loc[:,'n_counts']
```



**iloc** allows us to subset rows and colums by index number. This is useful if we want to subset multiple rows or columns without typing index names. Lets say we want to remove the columns with names 'orig_ident', 'res_2', and 'louvain'.

Lets take a look at the column names first and see if we can slice out the ones we'd like to keep.



```
# Return column names
cell_attributes.columns.values
cell_attributes.columns.values[[0,1,3,5,7]]
```



Now we can apply the same indexing pattern to our **iloc** method to return only the columns we're interested in. I've also included a few more slicing variations so you can get a feel for more complex slicing patterns.


```
# Return columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:,[0,1,3,5,7]].head(10)

# Return rows 1 through 5 and columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:5,[0,1,3,5,7]].head(10)
```

##### Complex slicing patterns

```
# the method r_ allows us to slice with multiple ranges
from numpy import r_

# Let's see what it returns before we slice our data frame
pd.np.r_[1:2, 4, 5:7]

# With column names
cell_attributes.columns.values[pd.np.r_[1:2, 4, 5:7]]

# With the first 5 rows of the data frame
cell_attributes.iloc[:5,pd.np.r_[1:3, 5:7]]
```


### Ordering dataframes by column values

Here we'll take look at ordering our data by a particular column value, or multiple column values.



```
# Let's make a smaller dataset to work with
cell_df_sub = cell_attributes.iloc[:25,[0,1,3,5]]

# Set ascending=True to reverse the order
cell_df_sub.sort_values('n_counts', ascending=False)

# Sort by multiple columns in different directions
cell_df_sub.sort_values(by=['tree_ident', 'n_counts'], ascending=[True, False])
```



### Subsetting data by condition

Understanding how to subset your data using conditional operations is *very*, _very_ useful. You'll often encounter situations where you want to filter your data on a certain set of parameters to reduce it to a more "meaningful" state.

```
# Subsetting on a single condition
cell_df_sub.loc[(cell_df_sub['tree_ident'] == 1),]
```

In the example below we chain boolean operators together to achieve results that satisfy multiple conditions. You can make these statments complex as you'd like.

Note: Pandas uses the bitwise logical operators (see earlier lecture). A pipe symbol `|`  represents `or`, and an ampersand symbol `&`  represents `and`. The backslashes in code simply allow us to break up our statement at arbitrary points for readbility.

```
# Subsetting on multiple conditions.
cell_df_sub.loc[
    (cell_df_sub['tree_ident'] == 1) | \
    (cell_df_sub['tree_ident'] == 2) & \
    (cell_df_sub['n_genes'] > 1000),]
```

What's actually going on here? The rows in the data frame are actually subsetted on a vector of True/False statements. That is, for every row for which the condition evaluates to True will be returned. If we examine the boolean statements placed within `cell_df_sub.loc[]`, you can see why this is occuring.

```
cell_df_sub['tree_ident'] == 1 | \
    (cell_df_sub['tree_ident'] == 2) & \
    (cell_df_sub['n_genes'] > 1000)
```

### Performing mathmatical operations on vectors

Lets look at a couple examples where we apply caculations to our data frame. First lets calculate some summary statistics. This can be a useful when viewing our results for the first time to get a handle on how our data is distributed.

```
# Returning summary statistics for all columns
cell_df_sub.describe()

# Returning summary statistics for a single column
cell_df_sub.loc[:,'n_counts'].describe()
```

`n_counts` refers to the number of counts for "unique molecular identifiers", which are barcodes for individual transcripts within in a single cell. Ideally, if the number of `n_counts` is high, then the number of genes per cell should also be high. The number of genes per cell is in the `n_genes` column. Lets see if this observation holds true by calculating the pairwise correlation between these two variables. 


```
# Simply add the .corr() method to your dataframe subset
cell_df_sub.loc[:,['n_counts','n_genes']].corr()
```

That summarizes our introduction to Pandas. As you can see, Pandas greatly simplifies the process of exploring and making calculations in data frames and matricies. Check out the link below for the offical documentation.

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)












