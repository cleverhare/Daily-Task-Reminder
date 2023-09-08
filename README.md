# Daily-Task-Reminder
its a basic python program which reminds me to open up notion when ever i get to my workspace at 10 am, I scheduled it through a cron job,  Its fairly created for MacOS but it can be customised for other Linux Distros

## CronJob

To run this project everyday at 10 AM, Paste the following

```bash
  0 10 * * * /usr/bin/python3 /Users/your_username/Desktop/notionOpen.py
```
