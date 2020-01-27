# NCAA-Championships-Data
These python files were used to create a dataframe that contains every result from the 2019 NCAA Wrestling Championships per wrestler.

Fair warning, the code is ugly, confusing, with no comments explaining anything because it was a solo mission.

This was an important project for me because I have a passion for wrestling and a passion for data, but as far as I know this key information
is not available to the public anywhere online. Now it is (for 2019 Championships at least). I will probably extend this to other years in the future.

The final results that contain all of the data are in the csv files starting with the word 'all' ex. 'all_125_scored_df'. The rest of the csv files are simply
auxillary that were necessary to lead to the final result.

This was a very tedious project, as you can see the txt file was not easy to work with. The entire structure of the bracket and scoring
system was built with a whole lot of iteration. 

Things that cause errors in the code that need prior edit in the txt file:
1. Wrestlers sharing the same name or having subsets of each others' names. ex. 'Vincenzo Joseph' and 'Joseph Smith' both in 165 bracket.
  fix: add a letter to one of the names and remove it in the final csv doc
2. Wrestlers with multiple last names ex. "Requir van der Merwe" 
  fix: concatenate in txt file --> 'Requir vanderMerwe'
3. Wrestlers from Maryland, because their school code is 'MD' while 'MD' stands for major decision in the rest of the doc
  fix: change 'MD' to 'MDU' when it is in parentheses (this could be added to the program, but it frankly wasn't an issue)
  Note: This issue only occured one time because Maryland is bad at wrestling. Nice job Youssif Hemida.
