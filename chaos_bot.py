import discord
from TwitchPlays_KeyCodes import *

#TODO: Get API Token from command line args or user provided file
API_TOKEN = '*******' #Replace '*' with Discord Bot API token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# When the connection to Discord is ready, send a msg to the console
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
# Processing message events from the Discord server
@client.event
async def on_message(message):
    # Disregard messages from this chatbot
    if message.author == client.user:
        return
    
    # $hello command pings the bot to let the user know the bot is running
    # TODO: randomize Flowey quotes using definitions imported from a 
    # separate file
    if message.content.startswith('$hello'):
        await message.channel.send("Howdy! I'm FLOWEY. FLOWEY the FLOWER! "\
            "Hmmm... You're new to the UNDERGROUND, aren'tcha? Golly, "\
            "you must be so confused. Someone ought to teach you how "\
            "things work around here! I guess little old me will have to do. Ready?")
    
    # $close command closes the client if the user sending the command
    # is a member of the Administrator or Mod role
    if message.content.startswith('$close'):
        for role in message.author.roles:
            if role.name == 'Administrator' or role.name == 'Mod':
                await client.close()

    try:
        print(f'Got message from {message.author}: {message.content}')
        # Now that you have a chat message, this is where you add your game logic.
        # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
        # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
        # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
        # Use the pydirectinput library to press or move the mouse

        ###################################
        # Undertale Chaos Mod Code
        # Undertale Chaos allows chat to modify what happens in game 
        # based on options numbered 1 thru 8
        ###################################

        match message.content:
            case "1": # Option 1
                HoldAndReleaseKey(ONE, 0.1)
            case "2": # Option 2
                HoldAndReleaseKey(TWO, 0.1)
            case "3": # Option 3
                HoldAndReleaseKey(THREE, 0.1)
            case "4": # Option 4
                HoldAndReleaseKey(FOUR, 0.1)
            case "5": # Option 5
                HoldAndReleaseKey(FIVE, 0.1)
            case "6": # Option 6
                HoldAndReleaseKey(SIX, 0.1)
            case "7": # Option 7
                HoldAndReleaseKey(SEVEN, 0.1)
            case "8": # Option 8
                HoldAndReleaseKey(EIGHT, 0.1)

    except Exception as e:
        print("Encountered exception: " + str(e))

# INFO: Lets the user know the connection to Discord is disconnected
@client.event
async def on_disconnect():
    print("Client Disconnected")

if __name__ == "__main__":
    # Run client
    client.run(API_TOKEN)