def human_years_cat_years_dog_years(human_years):
    # Your code here
    catYears = 0
    dogYears = 0
    for age in range(human_years):
        if age + 1 == 1:
            catYears += 15
            dogYears += 15
        elif age + 1 == 2:
            catYears += 9
            dogYears += 9
        else:
            catYears += 4
            dogYears += 5
            
    
            
    return [human_years, catYears,dogYears]