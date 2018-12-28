## Merge Adestra CSVs

###### This script joins the csv files downloaded from Adestra to make this process a little bit more automated.

The CSVs have to be saved to a 'files' directory, each file has to be named as the date downloaded from adestra in format 'YYYY-MM-DD'.

The script will spit out a 'merged.csv' file and upload it to the instance running matillion. **Remember to change the 'matillion_usrname' variable to your ssh user and to be connected to the VPN!**