# CSC1100 bit grader W24
Grades bits for CSC1100 which can be spent at https://bit-pocket.com/ 
## Setup
### Python
I reccomend using Python 3.8+ 
Installation guides can be found [here](https://github.com/Akuli/python-tutorial/blob/master/basics/installing-python.md)

### Code Setup

1. First add your username and password to log into OnlineGDB
   
  ![image](https://github.com/MMazenA/bit_grader/assets/84817881/848bdce7-bb25-4aa4-a70e-7d635d45d508)
  
2. Add links from onlineGDBS 'pending for evaluation" link. This is where results table will be extracted.
  
  ![image](https://github.com/MMazenA/bit_grader/assets/84817881/b7acb1ad-7d4f-4dc9-8975-d40d52481c5b)
  ![image](https://github.com/MMazenA/bit_grader/assets/84817881/b92ab1ae-38cc-4ba3-8a21-f49eeec995ea)

3. Add the name of all the students you want to calculate the bits for. This should be the name as listed in **OnlineGDB** _not canvas_!

   ![image](https://github.com/MMazenA/bit_grader/assets/84817881/cda3a749-7b09-4cf4-8193-9ff3462f4db5)

4. Lastly, modify the start and end dates that you're grading for.
   
   ![image](https://github.com/MMazenA/bit_grader/assets/84817881/e1997913-7f0e-41b6-b8e6-457540f3ba98)


## Grading Past First Week 
The program assumes that the "streak" bonus is active on the first run, doing anything besides start_date = 0 should be handled like this:
Assuming X is your real start week and Y is your final start week (for the weeks that you are grading for i.e. if I wanted to grade weeks 8->12, X=8 and Y=12)
1. Calculate Week 0 -> Week Y
2. Calculate Week 0 -> Week X
3. Subtract Step 1 from Step 2

## Tips 
I reccomend grading in batches so this calculation doesn't take too long. You are also more than welcome to modify the code to account for this.
In case of rate limiting by OnlineGDB, uncomment the sleep line on line 52  
