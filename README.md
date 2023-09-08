
# Daily Task Reminder

its a basic python program which reminds me to open up notion when ever i get to my workspace at 10 am, I scheduled it through a cron job, Its fairly created for MacOS but it can be customised for other Linux Distros




## Use it on your system

To Clone this project

```bash
  git clone git@github.com:cleverhare/Daily-Task-Reminder.git
```

Go to the folder

```bash
  cd Daily-Task-Reminder
```

Test The App

```bash
  Sudo python3 notionOpen.py
```

Schedule the cron JOB for 10 AM as per my Use case

```bash
  0 10 * * * /usr/bin/python3 /Users/your_username/Desktop/notionOpen.py
```


## Thanks for making it till the end, Raise an Issue to contribute in it. 
