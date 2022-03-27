--Data Transformation

select * from Census2011


alter table census2011 drop  column Table_Name, State_Code, District_Code --Dropped Columns State code adn district code

delete from census2011 where Total_Rural_Urban in ('Rural', 'Urban') -- Deleted records from table where the Records are shown for Rural and Urban areas statewise.

sp_rename 'census2011.Area_Name' , 'States', 'column' -- Renamed the column Area_name to States

delete from census2011 where States = 'India' -- Deleted records from table where values for Entire India which is sum of all states.

update census2011 set States = substring(States,charindex('-',States)+1,len(States)) --- Changed the values of States column from States-Jammu Kashmir to Jammu Kashmir


--Analysis Question 1

select census2011final.state, Non_workers_personsTotal, poverty_data.No_ofPersons_lakhs_Total from census2011final join poverty_data on census2011final.State = poverty_data.state

--Analysis Question 2

select census2011final.State, profession.Total_Male, profession.Total_Female from census2011final join profession on census2011final.state=profession.state

select census2011final.state, education.MaleNo_Education, 
  education.Male_Below_Matric_Secondary, education.Male_Below_Graduate,
  education.Male_Above_Graduate  from census2011final join education 
  on census2011final.state=education.state 

  select census2011final.state,profession.Male_upto_14_years,profession.
  Male_15_29_years,profession.Male_30_44_years,profession.Male_45_59_years,
  profession.Male_60_years_and_above from census2011final
  join profession on profession.state=profession.state

select census2011final.state, education.FemaleNo_Education, 
  education.Female_below_Matric_Secondary,
 education.Female_below_Graduate,
 education.Female_Above_Graduate 
 from census2011final join education 
 on census2011final.state=education.state 

select * from census2011

select census2011final.state, profession.Female_upto_14_years,
  profession.Female_15_29_years,profession.Female_30_44_years,
  profession.Female_45_59_years,profession.Female_60_years_and_above 
  from census2011final join education 
  on census2011final.state=education.state join profession 
  on education.state=profession.state
select * from census2011

--Analysis Question 3

select * from sqlbook.dbo.census2011final

select * from sqlbook.dbo.poverty_data

alter table sqlbook.dbo.census2011final drop column column1

select census2011final.state,sqlbook.dbo.census2011final.Non_Workers_PersonsIlliterate, 
 sqlbook.dbo.poverty_data.No_ofPersons_lakhs_Total
	from sqlbook.dbo.census2011final  inner join sqlbook.dbo.poverty_data 
		on sqlbook.dbo.census2011final.State=sqlbook.dbo.poverty_data.State 
			order by sqlbook.dbo.poverty_data.State



select census2011final.state,sqlbook.dbo.census2011final.Non_Workers_PersonsLiterate,
  sqlbook.dbo.poverty_data.No_ofPersons_lakhs_Total  
	from sqlbook.dbo.census2011final  inner join sqlbook.dbo.poverty_data 
		on sqlbook.dbo.census2011final.State=sqlbook.dbo.poverty_data.State 
			order by sqlbook.dbo.poverty_data.State


--Analysis Question 4
select State, Main_Activity_Beggars_Vagrants_etc_PersonsTotal from sqlbook.dbo.census2011final        -- Data to plot Bar graph to show state wise count of Beggars total 

select State, Main_Activity_Household_Duties_PersonsTotal from sqlbook.dbo.census2011final           -- Data to plot Bar graph to show State wise count of Household duties persons

select State, Main_Activity_Pensioners_PersonsTotal from sqlbook.dbo.census2011final               -- Data to plot bar graph to show State wise Count of Pensioners 

select State, Main_Activity_Dependents_PersonsTotal from sqlbook.dbo.census2011final              --Data to plot bar graph to show State wise count of Dependents

