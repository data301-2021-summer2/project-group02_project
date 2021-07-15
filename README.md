# Group 02 - {US state birth demongraphic investigation group}



## Milestones

Details for Milestone are available on Canvas (left sidebar, Course Project) or [here](https://firas.moosvi.com/courses/data301/project/milestone01.html).

## Describe your topic/interest in about 150-200 words
Our topic will be investigating growth in new population or new children born in different counties. We can use variables to determine the population demographic of USA states and couties, such as highest, lowest birthrate in terms of region, timeframe, GDP, crime rate, etc. We may also use math model to explore the relationship of different variables and birth rates. 

## Describe your dataset in about 150-200 words
| Header | Description | Data Type |
|---|---|---|
| `State` | The state (including District of Columbia) where the mother lives (states are listed as numbers in alphabetical order such that `01` = Alabama and `51` = Wyoming) | number | 
| `County` | The county where the mother lives (this is coded using the [FIPS County Code](https://en.wikipedia.org/wiki/FIPS_county_code)) | number | 
| `Month` | The month in which the birth took place (`1` = January and `12` = December) | number | 
| `Year` | The four-digit year of the birth (e.g., `2015`) | number | 
| `countyBirths` | The calculated sum of births that occurred to mothers living in a county for a given month (if the sum was less than 9, the sum is listed as `NA` as per NCHS reporting guidelines). | number | 
| `stateBirths` | The calculated sum of births that occurred to mothers living in a state for a given month (includes all birth counts, including those from counties with fewer than 9 births in a month). | number | 


## Team Members

- Person 1: Andrew Dai cs major
- Person 2: Darren Dai MG Major
- Person 3: Jimmy Hu EESC Major

## References
Datasets are from the link below:
{https://github.com/the-pudding/data/tree/master/births}
