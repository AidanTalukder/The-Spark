import pandas as pd
import numpy as np
import random
import discord
from discord.ext import commands
import nest_asyncio
from CreateRumorChunks import run_CreateRumorChunks

# loading the chunks from the file
def load_chunks(rumors):
    """ Opens the rumors txt and seperates them by double newlines
    
    Input: list of rumors
    Output: list of lists of four rumors"""

    with open(rumors, "r", encoding="utf-8") as file:
        content = file.read().strip().split("\n\n") # seperate chunks by double \n
    return content

async def DistributeRumors(bot, my_UID, blacklisted_UIDs, guild):
    """Reads the rumors by calling load_chunks() then sends them out to
    the players. It parses through the player list in order, but because 
    the rumors were already randomized in a previous step, the rumors are
    doled out as randomly as reasonble
    
    Input: the bot details, my personal Discord ID, the IDs of players I don't
    want to send rumors to, the server ID (guild)
    Output: None"""

    # create the txt containing the different rumors we want to distribute to server members
    run_CreateRumorChunks()

    # file containing the chunks of rumors
    rumors = "DistributedRumors.txt"

    # gets all members of interest in server excluding bots, myself, and outlined blacklisted UIDs
    members = [member for member in guild.members if member.id != my_UID and member.id not in blacklisted_UIDs and not member.bot]

    chunks = load_chunks(rumors)
    if len(chunks) < len(members):
        print("Not enough chunks for all members.")
        return
    
    for member, chunk in zip(members, chunks):
        try:
            await member.send(f"Ah, so many secrets in your little colony. So many Stories. Would you like to hear some of them?\n\n{chunk}")
            print(f"Sent chunk to {member.name}")
        except Exception as e:
            print(f"Failed to send message to {member.name}: {e}")

        print("Job's done, boss!")
        await bot.close()

async def DistributeRumorsTest(bot, my_UID, blacklisted_UIDs, guild):
    """Testing function for DistributeRumors()"""

    # create the txt containing the different rumors we want to distribute to server members
    run_CreateRumorChunks()

    # file containing the chunks of rumors
    rumors = "DistributedRumors.txt"

    # gets all members of interest in server excluding bots, myself, and outlined blacklisted UIDs
    members = [member for member in guild.members if member.id == my_UID]

    chunks = load_chunks(rumors)
    
    for member in members:
        for chunk in chunks:
            try:
                await member.send(f"Ah, so many secrets in your little colony. So many Stories. Would you like to hear some of them?\n\n{chunk}")
                print(f"Sent chunk to {member.name}")
            except Exception as e:
                print(f"Failed to send message to {member.name}: {e}")

        print("Job's done, boss!")
        await bot.close()