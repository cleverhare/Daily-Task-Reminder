import os
# Defined a funciton that shows the reminder, emits a beep & speaks a message from speaker(Earphone/Loudspeaker)
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    so = '-sound NAME'
    os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s, so])))
    os.system('say "Hey Soumyajit, Good Morning Sir, Dont forget to open Notion to check the tasks assigned to you"')

# Function calling
notify(title    = 'Hey Soumyajit',
       subtitle = 'REMINDER!',
       message  = 'Dont forget to open Notion to check the tasks assigned to you')
