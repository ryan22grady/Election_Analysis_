# Election_Analysis_

## Project Overview
A Colorado Board of Elections employee has given me the following taks to complete the election audit of the recent local congressional election.

1. Calculate the total bumer of votes cast.
2. Get the complete list of the candidates who receieved votes.
3. Calculate the total bumer of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.57.1

## Summary
The analysis of the election show that:
- There were 369,711 votes case in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The Candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes. 
    - Diana DeGette received 78% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette received 78% of the vote and 272,892 number of votes.

<img width="297" alt="Screen Shot 2021-07-03 at 11 59 17 AM" src="https://user-images.githubusercontent.com/84995704/124361733-37d3d780-dbf6-11eb-9d15-2ede3d7d7fd5.png">

## Challenge Overview
After helping Seth and Tom submit the election audit results, the election commission has now requested some additional data to complete the audit:
    1. The voter turnout for each county.
    2. The percentage of votes from each county out of the total count.
    3. The county with the highest turnout. 
## Challenge Summary
This script can be used--with some modifications-- for any election. If the results are in a similar CSV format, then, the script will be able to maintain the assignment of dictionaries based on candidates and counties to analyze and showcase the results. This script will work with more scripts and counties should the commission want the audit to be more encompassing. This script can be easily modified to be used with congressional district voting or specific seats on respective county boards simply by adding a new column (or series) and using the script to pull from a dictionary of variables. The script could also be modified to include election day polling, that is, including a series of responses that voters can choose as it relates to proposed policy issues. Again, more series can be adding so long as there is a control variable of pre-determined responses from which to choose. 

