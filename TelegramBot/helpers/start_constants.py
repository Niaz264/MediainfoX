from TelegramBot.version import (__python_version__, __version__, __pyro_version__,  __license__)


COMMAND_TEXT = """🗒️ Documentation for commands available to user's 
	
• /start: To Get start message and help guide. 


(Generates frames screenshot from video  file.)

• /screenshot or /ss [File DDL/Drive URL] | [No. of frames] ( Default 5 and Max 15)

(Generates Mediainfo  from any type file. )

• /mediainfo or /m  [File DDL/Drive URL]

You can also reply Mediainfo and Screenshot commands to telegram files aswell.
"""


ABOUT_CAPTION = f"""• Python version : {__python_version__}
• Bot version : {__version__}
• pyrogram  version : {__pyro_version__}
• License : {__license__}


START_ANIMATION = "https://graph.org/file/aaab3d4135ca233f2b0a7.mp4"

START_CAPTION = ""Hey there!! I am simple Telegram Bot wich is made for the purpose for generating video files frames and mediainfo from Telegram files and links""
