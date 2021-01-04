# Overview of Election Audit

In this audit, we looked to perform an analysis of the tabulated results for a US congressional district in Colorado. We will look to create a program to perform automated tabulations of all of the total votes, the votes for each candidate, and the total votes per each county in the congressional district.

# Election-Audit Results

After creating a Python program to tabulate the votes and perform the calculations needed for this audit, we have put together the following answers.

## How many votes were cast in this congressional election?

- In the election that we tabulated results for, there were a total of 369,711 votes in the Colorado congressional district. We have verified this result by matching our final total from our Python program and compared this to the total count of columns from the Excel document that housed all of the raw voting results seen in the Election_Results.csv

![Colorado Congressional District Total Votes](/Resources/total_votes_election_analysis.png "Colorado Congressional District Total Votes")

## Provide a breakdown of the number of votes and the percentage of total votes for each county in the precint.

- The output of our program ran through all of the counties in the congressional district, creating a list of unique counties in which we needed to tally the votes for. The output of this tabulation can be seen below, in which we can see that Denver accounted for 306,055 - which was nearly 83% of the total votes in the district. The county of Jefferson had the second highest voter totals in the district with 38,855 votes - accounting for over 10% of the votes. The final county of Arapahoe made up the remaining 24,801 votes in the district - accounting for nearly 7% of the votes.

![Colorado Congressional District Per County Votes](/Resources/county_votes_election_analysis.png "Colorado Congressional District Per County Votes")

## Which county had the largest number of votes?

- As seen in the screenshot above, Denver was the county with the most votes in this US congressional district - accounting for nearly 83% of the total votes in the district.

## Provide a breakdown of the number of votes and the percentage of total votes each candidate received.

- The output of our program ran through all of the candidates running for office in the congressional district, creating a list of unique candidates in which we needed to tally the votes for. The output of this tabulation can be seen below, in which we can see that Diana DeGette accounted for 272,892 - which was nearly 74% of the total votes in the district. Charles Casper Stockham had the second highest voter totals in the district with 85,213 votes - accounting for 23% of the votes. The final candidate, Raymon Anthony Doane, made up the remaining 11,606 votes in the distrct - accounting for 3% of the votes.

![Colorado Congressional District Per Candidate Votes](/Resources/candidate_votes_election_analysis.png "Colorado Congressional District Per Candidate Votes")

## Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

- We created a formula to properly calculate the winner of the election based on the total results, to ensure there would be no mistake if the vote totals were close. As can be seen in the image below, the clear winner of this election was Diana DeGette. She won the election with a total vote count of 272,892 - accounting for 73.8% of all votes cast in the congressional district.

![Colorado Congressional District Winning Candidate Information](/Resources/winning_candidate_election_analysis.png "Colorado Congressional District Winning Candidate Information")

# Election-Audit Summary

As this analysis was run for just one congressional district, there is a proposal that could be made to the election commission to leverage this code with a few modifications to tabulate other elections across the state. This will ensure there is accuracy (assuming the data set is clean) across all additional elections this program would be used for.

The first example of how to improve upon this program to benefit the election commission, would be to add additional logic to tabulate results for other roles on the election card. It is uncommon to have an election for just a single office holder, so by adding the necessary logic to identify the voters selection for numerous office holders (ie: Senators, Judges) we can perform all of the voting calculations at once for the district.

The second example of how to improve upon this program to benefit the election commission, would be to extend the logic to also account for the congressional districts - so that voting results could be calculated for the entire state. In this audit, we were provided the counties within a single district - however we could expand this program to perform an analysis of the total votes, county votes, and winners of numerous office holders across all of the congressional districts in the state of Colorado.