# How to contribute
First off, *thank you* for wanting to help improve Fake Golf. This game runs on volunteers, and it's great to know someone else shares that passion.

If you haven't already, please join us in our Discord server. The link is in the repo's description.

# Fake Bot Setup
Currently, Fake Bot runs through a Discord bot on the server, using calls to an API. The bot is built using discord.py, while the API is built on FastAPI. While running it all through the bot is possible, the decision was made to build upon a stand-alone API so the project could expand more easily. For example, a website could be built or a new social media site could be added just by working with the API.