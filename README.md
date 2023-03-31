
# WhatsApp Bulk Messages

A quick and dirty solution.

## About

When writing direct messages to many people at once, WhatsApp provides 2 methods:

1. Forwarding an existing message
2. Using a broadcast

These methods are flawed, because the message either displays a "forwarded" flag  or will only be delivered to people who have the senders number in their contacts (broadcast) [1][2]. They also do not allow personalization.

This script solves these problems by using the [keyboard](https://pypi.org/project/keyboard/) library to automate the process of writing/copying a message template while adding the recipients name for a list of contacts.

## Requirements

- [WhatsApp Desktop](https://www.whatsapp.com/download)
- [Python 3](https://www.python.org/downloads/)
- [keyboard](https://pypi.org/project/keyboard/)

## Use

Clone the repository or download and unpack the archive.

Write a message template an save it in ```message_template.txt```. The placeholder for the recipients name is ```{name}```. For emojis use the CLDR short name from [here](https://unicode.org/emoji/charts/emoji-list.html), preface it with a colon (:) and replace all spaces with an underscore (_). Example: ```:grinning_face_with_big_eyes```

```txt
Hello {name},
this is the message template.
You can even use emojis like that :smiling_face_with_smiling_eyes
Greetings
John
```

Fill ```recipients.csv``` with the recipients ```full_name``` from you address book and the ```short_name``` with which they will be addressed in the message.

```csv
full_name,short_name
Jane Doe,Jane
John Doe,Johnny
```

Make sure you are logged in to WhatsApp.

Run the script. It does not matter whether WhatsApp is open or closed. Watch carefully, but do not touch you input devices other than to stop the script.

```bash
python3 script.py
```

## Disclaimers

- Currently only works with WhatsApp Desktop
- Test your message_template before using it on a long list of recipients
- Currently it only works with emoji short codes (see next section)
- The script might happen to run in issues, since it won't get feedback for what it is doing. You might have to intervene.
- Not all emojis work with WhatsApp in the same way, flags for example have a different short code than in unicode's emoji list.

## Sources

[1] Forwarding flags: https://faq.whatsapp.com/1053543185312573
[2] Broadcasting limitation: https://faq.whatsapp.com/861663048350950
