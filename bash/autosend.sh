# Source - https://superuser.com/a/1776208
# Posted by Dave Jarvis, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-24, License - CC BY-SA 4.0
#
#!/usr/bin/env bash

ATMT="$1"

SUBJ="Email automation test"
DEST="Alexander Anisimov <alexander.anisimov@dfki.de>"
BODY="Clean the spam after meeting!"
# ATMT="~/Desktop/dummy.csv"
thunderbird -compose "subject='$SUBJ',to='$DEST',body=$BODY,attachment=$ATMT" &

sleep 2

WID=$(wmctrl -l | grep -i thunderbird | grep Write | grep Email | cut -f1 -d' ')

xdotool key --clearmodifiers --window $WID 'Ctrl+Return'

sleep 2

xdotool key --clearmodifiers --window $WID 'Return'
