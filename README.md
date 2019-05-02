# Pandas-search: Alfred-workflow (2 May, 2019)
A workflow to search in Scipy core packages documentation and display in-line. Only supports **Alfred 3**

<p align="center">
<img src="https://github.com/TonyWu20/Scipy-package-search-Alfred-workflow/blob/master/source_scipy/pandas.png?raw=true" height=100px>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/1024px-Created_with_Matplotlib-logo.svg.png" height=100px>
<img src="https://github.com/TonyWu20/Scipy-package-search-Alfred-workflow/blob/master/source_scipy/numpy-logo-300.png?raw=true" height =100px>
</p>

## Currently Supported Documentations
- Pandas
- Matplotlib
- Numpy
## Preview
![illustration1](preview.gif)
## Requirements
* This workflow is developed with **Python 3** and it relies on **Selenium** + Chromedriver to get the Javascript generated search results. The chromedriver has been packed into the workflow, so it helps you avoid the chromedriver path assigning trouble. **However, you still needs to install Selenium beforehand.**
* This workflow uses JSON format to present the formatted results to Alfred. As only Alfred 3 supports JSON format, this workflow is an **Alfred 3 only** workflow.
## Features
- In-line search in alfred. You can preview the results by tapping **Shift** or press **CMD + Y**.
- **New on 30 April, 2019**: If the search result contains a preview description, it will be shown instead of its url. Else the url will be shown. 
## P.S.
It may takes several seconds before the results are shown(as the results are JS generated), depending on your network connection condition. Just be patient! It still takes less time than you perform the search manually by yourself.
## Inspiration
[aviaryan's google search workflow](https://github.com/aviaryan/alfred-google-search). As a beginner in Alfred Workflow development and my knowledge to Python is not systematic, I learned how to format the search results into Alfred-accepted JSON format from his workflow. No external lib is required and it saved my life cuz I only learn Python 3 :)
