# A Look Into Seattle Airbnb Rental Market using Data


## Installation
[Python 2.7, Anaconda distribution](https://www.anaconda.com/download/) is recommended, but any Python 2.7 installation should work. 
Packages that are required includes Scikit-learn, NumPy, Pandas and Seaborn. 
For details on specific package revisions and a full list of packages, please refer to `requirements.txt` file.

The python notebook, `airbnb-analysis.ipynb`, 
In order to run the notebook, install packages listed in `requirements.txt`. 
The `data` folder contains all the data necessary required to run the notebook.

## Project Motivation
If you're a host on Airbnb or thinking about becoming one, then at one point or another, you might have wondered what drive ratings and prices on Airbnb. Afterall, we want happy guests and happy hosts.

This is an analysis that aims to answer the following questions:
- What time of year that is busier than other?
- As a host, what factors should I focus on to drive ratings up?
- What factors affect price of the rental?
- Finally, can we develop a model that can be used to predict (or determine) price?

## File Descriptions
`data/`
- Directory that contains the data files used in this project.

`airbnb-analysis.ipynb`
- The Jupyter notebook that contains the analysis and training of the pricing model.

`README.md`
- This README.

`requirements.txt`
- Required packages to run the notebook code in this project are listed in this file.

## Results
We analyzed 2016 Airbnb listing for Seattle, WA. First, we wanted to know the busiest time of year for Seattle. We found that January was the busiest month. January 2016 had the highest demand and lowest inventory in the year, especially at the beginning of the year. Next, we explored what factors affect overall rating the most. We found that value and cleanliness had the highest correlation. Third, we wanted to know what the biggest drivers of price were. We discovered that the more people a rental could accommodate the more it costed. Finally, we developed a machine learning model that can predict the price of the rental given its size and location. The advantage of having a model is that it we can ask it to determine prices for properties of any variation of size and location. It could be deployed to use programmatically because it’s generalized. Hosts can use it for guidance on setting custom prices for their rentals.

## Acknowledgements 
The data was obtained from [Kaggle](https://www.kaggle.com/airbnb/seattle/data). It consists of listings in Seattle, WA for year 2016.
