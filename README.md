# Password_generator
Simple python script for generate random passwords.

The script is called by a .bat file. This file is located in the folder with cmd.exe. For example:
```
@Echo off
if "%1" == "" goto no_param
if "%2" == "" goto no_param

python path\to\password.py %1 %2

goto exit
 
:no_param
echo Give two numbers...
goto exit
 
:exit
pause
```
As parameters of the script, the values of the length of passwords and their number are passed. (choose the one you like:))
Use case:

`password 12 5`

![image](https://user-images.githubusercontent.com/79583622/227328037-a7a9e8db-c7cf-4ad4-b13e-f8a80d2ff970.png)
