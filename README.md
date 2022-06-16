# Content
* [Get Started]()
* [Install]()
* [Setup the bot]()
  - [Change prefix]()
  - [Setting parameters]()
* [Running the bot]()
* [Customizing the bot]()


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

# Setup the bot

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

## 
