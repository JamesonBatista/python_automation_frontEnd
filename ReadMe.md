# install:

pip install -U selenium
pip install -U allure-behave
pip install -U behave

### Execute reporter allure:
behave -f allure_behave.formatter:AllureFormatter -o reports/ features

### esse comando deve ser usando no CMD estando no caminho do seu projeto
allure serve reports/

### Download e configuração do Allure


https://www.youtube.com/watch?v=xdjN-4UxL1c
