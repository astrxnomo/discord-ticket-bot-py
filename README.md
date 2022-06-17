# Content
* [Get Started](https://github.com/astrxnomo/discord-ticket-bot-py#get-started)
* [Install](https://github.com/astrxnomo/discord-ticket-bot-py#install-)
* [Setup the bot](https://github.com/astrxnomo/discord-ticket-bot-py#setup-the-bot-)
  - [Change prefix](https://github.com/astrxnomo/discord-ticket-bot-py#change-prefix)
  - [Setting parameters](https://github.com/astrxnomo/discord-ticket-bot-py#setting-parameters-)
* [Running the bot](https://github.com/astrxnomo/discord-ticket-bot-py#running-the-bot)
  - [Ticket channel](https://github.com/astrxnomo/discord-ticket-bot-py#ticket-channel)
  - [Ticket command](https://github.com/astrxnomo/discord-ticket-bot-py#ticket-command)
  - [Testing the bot](https://github.com/astrxnomo/discord-ticket-bot-py#testing-the-bot)
    - [Select function](https://github.com/astrxnomo/discord-ticket-bot-py#select-function)
    - [Inside the ticket](https://github.com/astrxnomo/discord-ticket-bot-py#inside-the-ticket)
      - [Call staff function](https://github.com/astrxnomo/discord-ticket-bot-py#call-staff-function)
      - [Close ticket function](https://github.com/astrxnomo/discord-ticket-bot-py#close-ticket-function)
    - [Ticket logs](https://github.com/astrxnomo/discord-ticket-bot-py#ticket-logs)
* [Customizing the bot](https://github.com/astrxnomo/discord-ticket-bot-py#customizing-the-bot)


# Get Started
We suggest you be familiar with discord.py and python. This is a Ticket Bot guide so it couldn't contain a lot of python explanations.

# Install *
1. We need to install the library [discord-components](https://devkiki7000.gitbook.io/discord-components/)

```py
pip install --upgrade discord-components
```

> ⚠️ If you meet an error `No matching distribution found for discord-components` when installing, try updating the python version! (It must be upper than 3.6)

2. We need to create the bot in Discord Developer Portal. If you have no idea how to do it follow this [documentation](https://discord.com/developers/docs/getting-started#creating-an-app).
3. Invite the bot to your server.

# Setup the bot *

## Change prefix 

`tb!` is the default prefix, if you want to change it just change what is inside the quotation marks `' '`

```py
bot = ComponentsBot('tb!', help_command=None)
```
> [Go to code](https://github.com/astrxnomo/discord-ticket-bot-py/blob/a74c6c23be90d7356b197e441ed3bf3944344635/main.py#L9)

## Setting parameters *
The bot will need a category where it will create the tickets channels, a channel where it will put the ticket logs and the role of those who attend the tickets, commonly the staff role and finally a hexadecimal color that will carry all the embeds sent by the bot, by default it is yellow.

```py
id_category =
id_channel_ticket_logs =
id_staff_role =
embed_color = 0xfcd005 
```
> [Go to code]()


We must enable server members intent and copy the bot token from the Discord developer portal and paste it inside the quotation marks `' '`
```py
bot.run(' ')
```
> [Go to code]() 

# Running the bot

Up to this part of the guide the bot should be working, with the default values of course, but if up to this part your bot is working it means that you have completed the previous steps well.

## Ticket channel

Now we will create the channel where our message will go to create tickets

![image](https://user-images.githubusercontent.com/75272665/174153373-7f1113f5-c21b-4592-98f6-99478fdd7307.png)

## Ticket command

In the ticket channel we are going to execute the command `tb!ticket` (remember that `tb!` is the default prefix, if you changed it you put its respective prefix) and the bot will reply this:

![image](https://user-images.githubusercontent.com/75272665/174154120-df75f170-b378-4324-857a-53050a2c1884.png)

## Testing the bot

<details><summary>Select function</summary>
<p>
  
![image](https://user-images.githubusercontent.com/75272665/174156497-2f13d506-7ae2-4074-8e06-ac887ca46932.png)

![image](https://user-images.githubusercontent.com/75272665/174156675-39bb34fa-5bac-4543-8399-06cf07f56fdb.png)

When one of the options is selected, the bot will send a confirmation message when the respective ticket is created, also mentioning its executor in the ticket.

![image](https://user-images.githubusercontent.com/75272665/174156906-6c56e21c-878a-4f4a-affe-c9462fa01e52.png)

![image](https://user-images.githubusercontent.com/75272665/174156983-8f871413-d75f-417b-b4ba-6077db365d8c.png)
  </p>
</details>

<details><summary>Inside the ticket</summary>
<p>
  
![image](https://user-images.githubusercontent.com/75272665/174157033-8ebf9975-04ea-4246-8f6e-7951b7b8d6b9.png)

#### Call staff function
  
![image](https://user-images.githubusercontent.com/75272665/174157118-7d67a67e-6283-49fd-9b4e-72106716090b.png)

#### Close ticket function
  
![image](https://user-images.githubusercontent.com/75272665/174157206-4b69ef02-e0ac-4ab7-b69d-ae26139fd37c.png)
  </p>
</details>

<details><summary>Ticket logs</summary>
<p>

When the ticket has been closed, a message will be automatically sent to the ticket log channel with basic ticket information.
  
![image](https://user-images.githubusercontent.com/75272665/174157271-92372073-5bd3-4e75-b466-f5947194e43d.png)
  
  </p>
</details>

# Customizing the bot
