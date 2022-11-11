from django.test import TestCase

# Create your tests here.
class Tttleaguestandings(models.Model):
    lrid = models.AutoField(db_column='LRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=50)  # Field name made lowercase.
    leagueteamref = models.CharField(db_column='leagueTeamref', unique=True, max_length=50)  # Field name made lowercase.
    teamclub = models.CharField(db_column='Teamclub', max_length=50)  # Field name made lowercase.
    leagueteamid = models.CharField(db_column='leagueTeamID', max_length=50)  # Field name made lowercase.
    leaguerno = models.IntegerField(db_column='leagueRno')  # Field name made lowercase.
    leagueteamtsegfol = models.IntegerField(db_column='leagueTeamTSEGFOL')  # Field name made lowercase.
    leagueteamtsegfts = models.IntegerField(db_column='leagueTeamTSEGFTS')  # Field name made lowercase.
    leagueteamtfin = models.DecimalField(db_column='leagueTeamTFIN', max_digits=15, decimal_places=3)  # Field name made lowercase.
    leagueteamsfpts = models.IntegerField(db_column='leagueTeamSFpts')  # Field name made lowercase.
    leagueteamlpts = models.IntegerField(db_column='leagueTeamLPTS')  # Field name made lowercase.
    tlptsonly = models.IntegerField(db_column='TLPTSonly')  # Field name made lowercase.
    leaguerecalcdate = models.DateField(db_column='leagueRecalcdate')  # Field name made lowercase.
    leaguetotaltpen = models.IntegerField(db_column='leaguetotalTPEN')  # Field name made lowercase.
    leagueteamname = models.CharField(db_column='leagueteamName', max_length=30)  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.
    eventrbonus = models.DecimalField(db_column='eventRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    teamtsprint = models.DecimalField(db_column='teamTSPRINT', max_digits=15, decimal_places=3)  # Field name made lowercase.
    teamtkom = models.DecimalField(db_column='teamTKOM', max_digits=15, decimal_places=3)  # Field name made lowercase.
    komteambonus = models.IntegerField(db_column='KOMTEAMBONUS')  # Field name made lowercase.
    sprintteambonus = models.IntegerField(db_column='SPRINTTEAMBONUS')  # Field name made lowercase.
    totalriderbonus = models.IntegerField(db_column='TOTALRIDERBONUS')  # Field name made lowercase.