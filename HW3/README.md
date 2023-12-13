
# Generating a Recognizer 

In this project i generated a Recognizer by ANTLR4 that can recognize :

NationalID , Email , Postal-Code , Float-Number , Version , URL

the grammer file is "Recognize.g4" and generated files are located in "gen" folder

the start rule is : NationalID | EMAIL | POSTAL_CODE | FLOAT | VERSION | URL
![Screenshot (43)](https://github.com/AMIR-M-A-2002/HomeWork_Compiler/assets/96167372/75f147e7-b61a-45a9-93b5-5407c7d64713)

the string should be placed in main.py line:12 as a value for input text like the image below
![Screenshot (44)](https://github.com/AMIR-M-A-2002/HomeWork_Compiler/assets/96167372/df98e247-6569-482b-9434-7b3210a26f54)

to use this project you should run the "main.py" file located in "gen" folder and then for a simple text below for a quick test :

"123456789 test@gmail.com 123456789 82943756 3.14 http://www.test.ut.ac.ir"

you see :
![Screenshot (45)](https://github.com/AMIR-M-A-2002/HomeWork_Compiler/assets/96167372/2424750f-4ab5-4ec1-a5fb-7f1e6a65a6de)
