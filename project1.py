print("Since the begging of the prison system in America Black \n"
        "people have been overwhelmingly the majority of the\n "
        "population, yet are not even a quarter of the of the\n"
        "population in America. We are now in the year 2021 an\n"
        "that is still the case. Statistics will prove that majority\n"
        "of the prison population is still black")
#state is key, values are sentenced prisoners, %black in prison, %black in pop
imprisonment={
'Maryland':[20733,  72.0,   29.2],
'Louisiana':[38022,  67.8,   32.0],
'Mississippi':[17876,  65.3,   37.1],
'South Carolina':[20830,  64.7,   27.4],
'Georgia':[52485,  62.0,   30.5],
'New Jersey':[21590,  60.5,   12.9],
'Alabama':[30766,  58.5,   26.3],
'Delaware':[4141,   58.4,  21.1],
'Illinois':[48278,  58.0,   14.2],
'Virginia':[37544,  58.0,   19.0],
'North Carolina':[35769,  55.9,   21.3],
'Michigan':[43359,  53.6,   14.0],
'New York'    :[52399,  48.9,   14.6],
'Pennsylvania'    :[50423,  48.7,   10.6],
'Florida' :[102870, 47.7,   15.5],
'Ohio'    :[51519,  44.6,   12.2],
'Tennessee'   :[28769,  44.1,   16.8],
'Wisconsin'  :[21404,  42.7,   6.3],
'Arkansas'    :[17819,  42.5,   15.4],
'Connecticut'    :[11735,  41.6,   9.7],
'Missouri'    :[31938,  36.2,   11.6],
'Texas'   :[158589, 35.9,   11.7],
'Minnesota'   :[10637,  34.1,   5.5],
'Indiana' :[29261,  33.3,   9.2],
'Kansas'  :[9365,   31.4,   5.9],
'Nevada'  :[12415,  29.0,   8.1],
'Rhode Island'   :[1880,   28.9,   5.5],
'California'  :[136088, 28.6,   5.7],
'Massachusetts'  :[9486,   28.3,   6.6],
'Oklahoma'    :[27261,  27.3,   7.4],
'Nebraska'    :[5347,   26.9,   4.6],
'Iowa'    :[8798,   25.8,   3.1],
'Kentucky'    :[20969,  23.5,   8.0],
'Colorado'    :[20646,  18.7,  3.9],
'Washington'  :[18052,  17.9,   3.6],
'Arizona' :[40175,  14.0,   4.0],
'West Virginia'   :[6881,   11.7,   3.5],
'Vermont'    :[1508,  10.7,   1.1],
'Alaska' :[2754, 9.9, 3.5],
'Oregon'  :[15060, 9.4, 1.8],
'New Mexico'  :[6860, 7.3, 1.8],
'Maine'  :[2030, 7.1, 1.3,],
'North Dakota'   :[1603, 6.9, 1.7],
'Utah'    :[7024, 6.3, 1.0],
'South Dakota'    :[3605, 6.2, 1.8],
'New Hampshire'   :[2915, 5.9, 1.2],
'Wyoming' :[2383, 5.0, 1.6],
'Hawaii' :[3663, 4.7, 2.1],
'Montana' :[3699, 2.9, 0.5],
'Idaho'   :[8039, 2.8, 0.7],
}


for state, stats in imprisonment.items():
    print(f"\nIn {state.title()} "+str(stats[0])+ " people was sentenced" 
        "to prison."+str(stats[1])+"% was black with a " 
        "state population of "+str(stats[2])+"%")
    
print("This data shows the disperportion rate of black people"
    "\nimprisonment in America with very small population "
    "\nbut very high imprisonment rates")
