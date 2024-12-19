import discord
from discord.ext import commands

async def MessagePlayer(UID, guild, message):
    """Sends a player a discord DM from The Spark
    
    Input: bot, ID of the recepient, the server, the message as a string
    Output: None"""
    
    member = guild.get_member(UID)

    if member:
        print(f"Found member: {member.name}\nSending Message: {message}")
        await member.send(message)
    else:
        print("Member not found.")
    
    return


async def MessageGroup(UIDs, guild, anon, message):
    """Sends an identical message to all members of a list of UIDs.

    Input: list of UIDs, server ID, anon (whether the recipients know who the other recipients are or not), the message as a string
    Output: None    """

    members = [member for member in guild.members if member.id in UIDs]

    for member in members:
        try:
            if anon == True:
                print(f"Sending anonymous message to {member.name}")
                await member.send(message)
            else:
                print(f"Sending non-anonymous message to {member.name}")
                # create list of others who received this message
                others = [m.name for m in members if m != member]
                others_list = ", ".join(others)

                # send message
                await member.send(f"You and {len(members) - 1} others received a message:\n\n{message}\n\nOthers who received this message: {others_list}")
        except Exception as e:
            print(f"Failed to send message to {member.name}: {e}")
    return