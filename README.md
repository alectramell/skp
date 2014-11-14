-- SKP Python Module for Skype! (Ubuntu 12.01 >> 14.04) --

-- Compliments of Apollon Data Metrics Agency ;) 2014 --

Skype URL:
    http://www.skype.com

Skype Ubuntu APT install:
In Terminal, run command..

    sudo apt-get install skype

Getting Started:

(1) Remember, before you can use this module, you must have Skype installed, and be signed in to trigger the "chat" and "call" functions.

(2) After step 1 as above, inside your python script, you must import skp (assuming you've installed it), then, after it is imported, use the following python triggers..

   to start a chat with selective contact:
      "skp.chat()"

   to start a call with selective contact:
      "skp.call()"

   example:
   
      import skp

      ask = raw_input('Make Choice (chat/call): ')
      if ask == ('chat'):
         skp.chat()
      if ask == ('call'):
         skp.call()

(3) Test it out ;)

for installation help contact Agent Tramell at alectramell@gmail.com, use "skp" as email subject ;)
