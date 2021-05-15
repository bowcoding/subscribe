# This is the import using GUIZero
from guizero import App, Text, Picture

# Main app body and title
app = App(title="Subscribe!")
app.bg = "cyan"

# Make the app fullscreen
app.height = 5000
app.width = 5000

# Subscribe main text
subscribe = Text(app, text="Subscribe to Moonwolf Gaming 7197 and XGamerBoiii on YouTube!")
subscribe.text_size = 35

# Specifically subscribe to Moonwolf Gaming 7197
MoonwolfGaming7197Profile = Picture(app, image="moonwolfgaming7197.jpg")
MoonwolfGaming7197ProfileID = Text(app, text="Moonwolf Gaming 7197")
MoonwolfGaming7197ProfileID.text_size = 15
SubMoonwolfGaming7197 = Text(app, text="bit.ly/3hGrg6n")

# The and between the profile pictures
betweenthesubscribe = Text(app, text="And")
betweenthesubscribe.text_size = 25

# Spefically subscribe to XGamerBoiii
XGamerBoiiiProfile = Picture(app, image="XGamerBoiii.jpg")
XGamerBoiiiProfileID = Text(app, text="XGamerBoiii")
XGamerBoiiiProfileID.text_size = 15
SubXGamerBoiii = Text(app, text="bit.ly/33OCvkK")

# The websites
LinkSites = Text(app, text="Websites")
LinkSites.text_size = 30

BowWebsite = Text(app, text="www.blastoffwaters.com")
BowWebsite.text_size = 20

BowFunWebsite = Text(app, text="bowfun.epizy.com")
BowFunWebsite.text_size = 20

GalaxyWebsite = Text(app, text="galaxyeco.epizy.com")
GalaxyWebsite.text_size = 20

# Display the GUI popup
app.display()