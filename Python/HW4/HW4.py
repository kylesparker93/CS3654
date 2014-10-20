import pandas as pd

# 3
# There is no reshaping needed
data = pd.read_csv('cfb2013stats.csv')

# 4
data.Date.describe() # Date of the game
data.FumblesDef.describe() # Fumbles by the opponent
data.FumblesOff.describe() # Fumbles by "this" team
data.Line.describe() # Vegas line
data.Opponent.describe() # Opposing team
data.PassAttDef.describe() # Opponents passing attempts
data.PassAttOff.describe() # "This" teams passing attempts
data.PassCompDef.describe() # Opponents passing completions
data.PassCompOff.describe() # "This" teams passing completions
data.PassIntDef.describe() # Opponents interceptions
data.PassIntOff.describe() # "This" teams interceptions
data.PassYdsDef.describe() # Total passing yards for opponent
data.PassYdsOff.describe() # Total passing yards for this team
data.RushAttDef.describe() # Opponents rush attempts
data.RushAttOff.describe() # This teams rush attempts
data.RushYdsDef.describe() # Opponents rush yards
data.RushYdsOff.describe() # This teams rush yards
data.ScoreDef.describe() # Total score of opponent
data.ScoreOff.describe() # Total score of this team
data.Site.describe() # Home, away, neutral
data.TeamName.describe() # This team's name

# 5
# Replace missing lines with 0's
data.Line.replace(' ', '0', inplace=True)

# 6
# No transformations are needed