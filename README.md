# doorbell-mp3
Script for Raspberry Pi to play mp3 when relay is closed.

To install, open terminal and type:

git clone https://github.com/aaron-dunigan-atlee/doorbell-mp3.git

The script will download, along with sample mp3's. You can replace these with your own. 

To edit the cron table for automatic running of the script, type in the terminal:

crontab -e

You may get a prompt asking which editor to use.  Choose nano.
In the nano text editor, add the following line at the bottom:

@reboot python3 /home/pi/doorbell-mp3/doorbell.py >>doorbell-log.txt 2>&1

And then a blank line, and then ctrl+x to exit, y to confirm save, enter to confirm filename, enter to exit.
Explanation:
@reboot (Executes at reboot.)
python3 /home/pi/doorbell-mp3/doorbell.py (Runs our script.)
>>doorbell-log.txt 2>&1 (This part copies all the printed output, including any errors, to a text file so we can check back later if something weird happened. The output is appended, so you can see all the past executions of the script.)

Now reboot and test by closing each relay.
If it doesn't work, check the log file, 'doorbell-log.txt.'  It should be in the /home/pi folder.  It will contain any error messages generated by Python as well as print statements from the script.
