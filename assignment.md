
# Assignment: Data Science

The goal of this assignment is to verify that you can apply data science techniques in practice. To do so, we ask that you create a time-series model that can predict the air temperature in the greenhouse.

## Instructions

Plant development and growth is a result of the direct environment of the plant. The environment consists of parameters such as air temperature, humidity, CO2 concentration and access to water and nutrients. These parameters are influenced by conditions outside, as well as control mechanisms inside the greenhouse. To achieve the right environment, the grower manipulates mechanical components of the greenhouse based on forecasted external weather conditions. These components include but are not limited to: screens, ventilation (through opening windows) and heating systems. 

For the assignment, you are expected to develop a time series model that can predict air temperature.

## Requirements

Your solution should include the following components:

1. A model that can predict air temperature (_T<sub>air</sub>_) up to 24 hours in advance, with 1 hour timesteps (i.e. assuming the current time is `t=0`, predict the air temperature for `t=1` to `t=24`, with 1 hour increments)
2. Include a confidence interval to your predictions at P10 and P90
3. Visualize your results
4. _Optional_: extend your model to include predictions on relative humidity (_RH<sub>air</sub>_)

### Non-functional requirements

- Use Python 3.6 or higher
- This assignment was designed to be completed in 6-8h. The evaluation will take into account the choices you make and what you focus on given the time you have. However, it's up to you if you spend less or more time on it.
- Please make sure the final commit to your repository is done at least 24 hours before the start of your interview

## Deliverables

This assignment should be delivered in the following way:

- All code is pushed to your private copy of this repository.
- Documentation is provided in the README.md on how the model works, which performance is expected, how to run and how to test it on new data.
- Any information, (dummy)-data, files, and other assets that are needed to run this model, are provided in this repository.

## Assessment Criteria

The solution will be assessed on the following criteria:

- How easy is it for us to run and test your model?
- How clear is the documentation?
- How reproducible are your results: can your model be trained easily for a new dataset
- Can your model easily be run on a new testset
- How did you measure your performance, what is your performance?
- Why did you choose the specific performance measure?
- What data preprocessing did you do, how did you implement it?
- What models did you try, how did you validate them, how did you select your final one?
- How well do you know the model, why should it work?
- Can you walk us through your choices and method?
- Can you clearly and concisely describe the modelling process you have followed and the choices you have made?
- Can you describe the biggest short-comings of your model and which steps could be taken to improve on that?

## Additional information and assumptions

- The required data can be found through this link: https://drive.google.com/drive/folders/1USB4dOK9UodNt1mPiLf8-jE0TkuS94-f?usp=sharing
- Please refer to the ReadMe.pdf file in the data folder. You can assume that _“Weather data”_ and _“Climate and irrigation setpoints”_ are available at `t>0`, data from other datasets is available at `t<=0`.
- In the data folder you will find six subfolders. The names of these folders represent teams that competed in the Wageningen Autonomous Greenhouse Challenge. Each team was given the assignment to grow tomatoes in a small greenhouse that could be controlled remotely. The data in each team folder describes the results of that particular team.

