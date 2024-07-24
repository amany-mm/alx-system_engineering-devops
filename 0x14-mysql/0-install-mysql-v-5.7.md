# [How to : ] Fresh Reset and Install mysql 5.7

```
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```


If this command did not install 5.7 correctly you can continue reading the following guide.

NOTE AS YOU PROCEED: At any point in this guide, don’t go to the next step if you have errors in the current step you are in, make sure there are no errors.

You can also use this guide for more visual and sample outputs :

[For a comprehensive Guide Click Here 📄](https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit#heading=h.nu0sqigqw1o9)


## Check if all good
```
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
```