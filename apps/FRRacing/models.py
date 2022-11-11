# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aresultaudit(models.Model):
    rpid = models.AutoField(db_column='RPID', primary_key=True)  # Field name made lowercase.
    rpseries = models.CharField(max_length=10)
    rpraceno = models.IntegerField()
    rpuserid = models.IntegerField()
    rpstage = models.CharField(max_length=30)
    rpdate = models.DateTimeField()
    rpmessage = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'ARESULTAUDIT'


class Aresultcontrol(models.Model):
    evtpid = models.AutoField(db_column='EVTPID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField()
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    racetype = models.CharField(max_length=10)
    racetime = models.CharField(db_column='raceTime', max_length=5)  # Field name made lowercase.
    eventfinal = models.CharField(max_length=1)
    hidepass = models.CharField(db_column='hidePass', max_length=1)  # Field name made lowercase.
    eventid = models.IntegerField()

    class Meta:
        
        db_table = 'ARESULTCONTROL'


class Aresultprocess(models.Model):
    proid = models.AutoField(primary_key=True)
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField()
    eventid = models.IntegerField()
    eventtype = models.CharField(max_length=20)
    evbasetime = models.IntegerField()
    prostart = models.DateTimeField()
    proend = models.DateTimeField()
    promessage = models.CharField(max_length=30)

    class Meta:
        
        db_table = 'ARESULTPROCESS'


class Event(models.Model):
    evid = models.AutoField(db_column='EVID', primary_key=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='EventID', unique=True, max_length=12)  # Field name made lowercase.
    zeventid = models.IntegerField(db_column='ZEVENTID')  # Field name made lowercase.
    zpteamct = models.IntegerField(db_column='ZPTEAMCT')  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    eseries = models.CharField(db_column='eSeries', max_length=3)  # Field name made lowercase.
    eseason = models.CharField(db_column='eSeason', max_length=3)  # Field name made lowercase.
    eraceno = models.IntegerField(db_column='eRaceno')  # Field name made lowercase.
    eshowracepass = models.CharField(db_column='eShowracepass', max_length=1)  # Field name made lowercase.
    eventclosed = models.CharField(db_column='eventClosed', max_length=1)  # Field name made lowercase.
    eracedate = models.DateField(db_column='eRacedate')  # Field name made lowercase.
    eformat = models.CharField(db_column='eFormat', max_length=10)  # Field name made lowercase.
    ecourse = models.CharField(db_column='eCourse', max_length=40)  # Field name made lowercase.
    ecoursealtname = models.CharField(db_column='eCoursealtname', max_length=50)  # Field name made lowercase.
    ecompleted = models.CharField(db_column='eCompleted', max_length=1)  # Field name made lowercase.
    eshowschedule = models.CharField(db_column='eShowschedule', max_length=1)  # Field name made lowercase.
    enote = models.TextField(db_column='eNote')  # Field name made lowercase.
    enote2 = models.TextField(db_column='eNote2')  # Field name made lowercase.
    enote3 = models.TextField(db_column='eNote3')  # Field name made lowercase.
    enote4 = models.TextField(db_column='eNote4')  # Field name made lowercase.
    eracenxtevent = models.CharField(db_column='eRacenxtevent', max_length=1)  # Field name made lowercase.
    epowerup = models.CharField(db_column='ePowerup', max_length=1)  # Field name made lowercase.
    ezlink = models.CharField(db_column='eZlink', max_length=255)  # Field name made lowercase.
    eposter = models.CharField(db_column='ePoster', max_length=50)  # Field name made lowercase.
    estageinfo = models.CharField(db_column='eStageinfo', max_length=50)  # Field name made lowercase.
    elastupdate = models.DateField(db_column='eLastupdate')  # Field name made lowercase.
    elastupid = models.IntegerField(db_column='eLastupID')  # Field name made lowercase.
    edistance = models.CharField(db_column='eDistance', max_length=6)  # Field name made lowercase.
    easc = models.IntegerField(db_column='eASC')  # Field name made lowercase.
    elaps = models.IntegerField(db_column='eLaps')  # Field name made lowercase.
    ecustomf = models.CharField(db_column='eCustomF', max_length=1)  # Field name made lowercase.
    equeen = models.CharField(db_column='eQueen', max_length=1)  # Field name made lowercase.
    ebasetime = models.IntegerField(db_column='eBasetime')  # Field name made lowercase.
    ebuffertime = models.IntegerField(db_column='eBuffertime')  # Field name made lowercase.
    efpointsmulti = models.IntegerField(db_column='eFpointsmulti')  # Field name made lowercase.
    efrhcdifficulty = models.CharField(db_column='eFRHCdifficulty', max_length=1)  # Field name made lowercase.
    elaptime = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'Event'


class Leaguestandings(models.Model):
    lrid = models.AutoField(db_column='LRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=20)  # Field name made lowercase.
    leagueteamref = models.CharField(db_column='leagueTeamref', unique=True, max_length=25)  # Field name made lowercase.
    leagueteamid = models.CharField(db_column='leagueTeamID', max_length=10)  # Field name made lowercase.
    leaguerno = models.IntegerField(db_column='leagueRno')  # Field name made lowercase.
    leagueteamtsegfol = models.IntegerField(db_column='leagueTeamTSEGFOL')  # Field name made lowercase.
    leagueteamtsegfts = models.IntegerField(db_column='leagueTeamTSEGFTS')  # Field name made lowercase.
    leagueteamtfin = models.IntegerField(db_column='leagueTeamTFIN')  # Field name made lowercase.
    leagueteamsfpts = models.IntegerField(db_column='leagueTeamSFpts')  # Field name made lowercase.
    leagueteamlpts = models.IntegerField(db_column='leagueTeamLPTS')  # Field name made lowercase.
    leaguerecalcdate = models.DateField(db_column='leagueRecalcdate')  # Field name made lowercase.
    leaguetotaltpen = models.IntegerField(db_column='leaguetotalTPEN')  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.

    class Meta:
        
        db_table = 'LeagueStandings'


class Leagues(models.Model):
    lid = models.AutoField(db_column='LID', primary_key=True)  # Field name made lowercase.
    leagueref = models.CharField(db_column='leagueRef', unique=True, max_length=20)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueseries = models.CharField(db_column='leagueSeries', max_length=10)  # Field name made lowercase.
    leagueseason = models.IntegerField(db_column='leagueSeason')  # Field name made lowercase.
    leaguediv = models.CharField(db_column='leagueDiv', max_length=10)  # Field name made lowercase.
    leaguedivno = models.IntegerField(db_column='leagueDivno')  # Field name made lowercase.
    leaguename = models.CharField(db_column='leagueName', max_length=40)  # Field name made lowercase.
    leagueriders = models.IntegerField(db_column='leagueRiders')  # Field name made lowercase.
    leaguegender = models.CharField(db_column='leagueGender', max_length=1)  # Field name made lowercase.
    leaguedivdisplay = models.CharField(db_column='leagueDivdisplay', max_length=2)  # Field name made lowercase.
    leagueactive = models.CharField(db_column='leagueActive', max_length=1)  # Field name made lowercase.
    leaguestart = models.DateField(db_column='leagueStart')  # Field name made lowercase.
    leaguezone = models.CharField(db_column='leagueZone', max_length=5)  # Field name made lowercase.
    leaguezonetime = models.CharField(db_column='leagueZonetime', max_length=10)  # Field name made lowercase.
    leaguezinvite = models.CharField(db_column='leagueZinvite', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Leagues'


class Raceteams(models.Model):
    rtid = models.AutoField(db_column='RTID', primary_key=True)  # Field name made lowercase.
    rteamid = models.CharField(db_column='rTeamID', unique=True, max_length=15)  # Field name made lowercase.
    rteamname = models.CharField(db_column='rTeamname', max_length=40)  # Field name made lowercase.
    raceteamactive = models.CharField(db_column='raceteamActive', max_length=2)  # Field name made lowercase.
    rteamnxtno = models.IntegerField(db_column='rTeamnxtno')  # Field name made lowercase.
    zpid = models.IntegerField(db_column='ZPID')  # Field name made lowercase.
    raceteamadmin = models.CharField(db_column='raceTeamadmin', max_length=1)  # Field name made lowercase.
    seriesregistered = models.CharField(db_column='seriesRegistered', max_length=1)  # Field name made lowercase.
    teamdefpw = models.CharField(max_length=20)
    zrloption = models.CharField(db_column='ZRLoption', max_length=1)  # Field name made lowercase.
    tttoption = models.CharField(db_column='TTToption', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Raceteams'


class Results(models.Model):
    resid = models.AutoField(db_column='ResID', primary_key=True)  # Field name made lowercase.
    resevid = models.CharField(db_column='ResEVID', unique=True, max_length=35)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueref = models.CharField(db_column='leagueRef', max_length=20)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=20)  # Field name made lowercase.
    resraceno = models.IntegerField(db_column='ResRaceno')  # Field name made lowercase.
    resteamid = models.CharField(db_column='ResTeamID', max_length=10)  # Field name made lowercase.
    resracedate = models.DateField(db_column='ResRacedate')  # Field name made lowercase.
    resteamleaguepts = models.IntegerField(db_column='ResTeamleaguepts')  # Field name made lowercase.
    resriderid1 = models.IntegerField(db_column='ResRiderID1')  # Field name made lowercase.
    resrider1fol = models.IntegerField(db_column='ResRider1FOL')  # Field name made lowercase.
    resrider1fts = models.IntegerField(db_column='ResRider1FTS')  # Field name made lowercase.
    resrider1fin = models.IntegerField(db_column='ResRider1fin')  # Field name made lowercase.
    resrider1wkg = models.DecimalField(db_column='ResRider1wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid2 = models.IntegerField(db_column='ResRiderID2')  # Field name made lowercase.
    resrider2fol = models.IntegerField(db_column='ResRider2FOL')  # Field name made lowercase.
    resrider2fts = models.IntegerField(db_column='ResRider2FTS')  # Field name made lowercase.
    resrider2fin = models.IntegerField(db_column='ResRider2fin')  # Field name made lowercase.
    resrider2wkg = models.DecimalField(db_column='ResRider2wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid3 = models.IntegerField(db_column='ResRiderID3')  # Field name made lowercase.
    resrider3fol = models.IntegerField(db_column='ResRider3FOL')  # Field name made lowercase.
    resrider3fts = models.IntegerField(db_column='ResRider3FTS')  # Field name made lowercase.
    resrider3fin = models.IntegerField(db_column='ResRider3fin')  # Field name made lowercase.
    resrider3wkg = models.DecimalField(db_column='ResRider3wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid4 = models.IntegerField(db_column='ResRiderID4')  # Field name made lowercase.
    resrider4fol = models.IntegerField(db_column='ResRider4FOL')  # Field name made lowercase.
    resrider4fts = models.IntegerField(db_column='ResRider4FTS')  # Field name made lowercase.
    resrider4fin = models.IntegerField(db_column='ResRider4fin')  # Field name made lowercase.
    resrider4wkg = models.DecimalField(db_column='ResRider4wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid5 = models.IntegerField(db_column='ResRiderID5')  # Field name made lowercase.
    resrider5fol = models.IntegerField(db_column='ResRider5FOL')  # Field name made lowercase.
    resrider5fts = models.IntegerField(db_column='ResRider5FTS')  # Field name made lowercase.
    resrider5fin = models.IntegerField(db_column='ResRider5fin')  # Field name made lowercase.
    resrider5wkg = models.DecimalField(db_column='ResRider5wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid6 = models.IntegerField(db_column='ResRiderID6')  # Field name made lowercase.
    resrider6fol = models.IntegerField(db_column='ResRider6FOL')  # Field name made lowercase.
    resrider6fts = models.IntegerField(db_column='ResRider6FTS')  # Field name made lowercase.
    resrider6fin = models.IntegerField(db_column='ResRider6fin')  # Field name made lowercase.
    resrider6wkg = models.DecimalField(db_column='ResRider6wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid7 = models.IntegerField(db_column='ResRiderID7')  # Field name made lowercase.
    resrider7fol = models.IntegerField(db_column='ResRider7FOL')  # Field name made lowercase.
    resrider7fts = models.IntegerField(db_column='ResRider7FTS')  # Field name made lowercase.
    resrider7fin = models.IntegerField(db_column='ResRider7fin')  # Field name made lowercase.
    resrider7wkg = models.DecimalField(db_column='ResRider7wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid8 = models.IntegerField(db_column='ResRiderID8')  # Field name made lowercase.
    resrider8fol = models.IntegerField(db_column='ResRider8FOL')  # Field name made lowercase.
    resrider8fts = models.IntegerField(db_column='ResRider8FTS')  # Field name made lowercase.
    resrider8wkg = models.DecimalField(db_column='ResRider8wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider8fin = models.IntegerField(db_column='ResRider8fin')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Results'


class Riderstandings(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamriderref = models.CharField(db_column='teamriderRef', unique=True, max_length=40)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=20)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=10)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totalrpt = models.IntegerField(db_column='totalRPT')  # Field name made lowercase.
    recalcdate = models.DateField(db_column='recalcDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'RiderStandings'


class Riderstatsindividual(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', unique=True, max_length=35)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=30)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=10)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totaltpt = models.IntegerField(db_column='totalTPT')  # Field name made lowercase.
    totalrpt = models.IntegerField(db_column='totalRPT')  # Field name made lowercase.
    calcdate = models.DateField()
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    timevalue = models.CharField(db_column='timeValue', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'RiderStatsindividual'


class Rideravailability(models.Model):
    raid = models.AutoField(db_column='RAid', primary_key=True)  # Field name made lowercase.
    razid = models.IntegerField(db_column='RAZid', unique=True)  # Field name made lowercase.
    raname = models.CharField(db_column='RAname', max_length=50)  # Field name made lowercase.
    atttcomment = models.CharField(db_column='aTTTcomment', max_length=50)  # Field name made lowercase.
    azrlcomment = models.CharField(db_column='aZRLcomment', max_length=50)  # Field name made lowercase.
    azrlcommentdate = models.DateTimeField(db_column='aZRLcommentdate')  # Field name made lowercase.
    atttcommentdate = models.DateTimeField(db_column='aTTTcommentdate')  # Field name made lowercase.
    atttcanride = models.CharField(db_column='aTTTcanride', max_length=1)  # Field name made lowercase.
    attttime1 = models.CharField(db_column='aTTTtime1', max_length=1)  # Field name made lowercase.
    attttime2 = models.CharField(db_column='aTTTtime2', max_length=1)  # Field name made lowercase.
    attttime3 = models.CharField(db_column='aTTTtime3', max_length=1)  # Field name made lowercase.
    attttime4 = models.CharField(db_column='aTTTtime4', max_length=1)  # Field name made lowercase.
    attttime5 = models.CharField(db_column='aTTTtime5', max_length=1)  # Field name made lowercase.
    azrlcanride = models.CharField(db_column='aZRLcanride', max_length=1)  # Field name made lowercase.
    azrltime1 = models.CharField(db_column='aZRLtime1', max_length=1)  # Field name made lowercase.
    azrltime2 = models.CharField(db_column='aZRLtime2', max_length=1)  # Field name made lowercase.
    azrltime3 = models.CharField(db_column='aZRLtime3', max_length=1)  # Field name made lowercase.
    azrltime4 = models.CharField(db_column='aZRLtime4', max_length=1)  # Field name made lowercase.
    azrltime5 = models.CharField(db_column='aZRLtime5', max_length=1)  # Field name made lowercase.
    azrltime6 = models.CharField(db_column='aZRLtime6', max_length=1)  # Field name made lowercase.
    azrltime7 = models.CharField(db_column='aZRLtime7', max_length=1)  # Field name made lowercase.
    atttconfirm = models.CharField(db_column='aTTTconfirm', max_length=1)  # Field name made lowercase.
    azrlconfirm = models.CharField(db_column='aZRLconfirm', max_length=1)  # Field name made lowercase.
    azrlstage1 = models.CharField(db_column='aZRLstage1', max_length=1)  # Field name made lowercase.
    azrlstage2 = models.CharField(db_column='aZRLstage2', max_length=1)  # Field name made lowercase.
    azrlstage3 = models.CharField(db_column='aZRLstage3', max_length=1)  # Field name made lowercase.
    azrlstage4 = models.CharField(db_column='aZRLstage4', max_length=1)  # Field name made lowercase.
    azrlstage5 = models.CharField(db_column='aZRLstage5', max_length=1)  # Field name made lowercase.
    azrlstage6 = models.CharField(db_column='aZRLstage6', max_length=1)  # Field name made lowercase.
    azrlstage7 = models.CharField(db_column='aZRLstage7', max_length=1)  # Field name made lowercase.
    azrlstage8 = models.CharField(db_column='aZRLstage8', max_length=1)  # Field name made lowercase.
    azrlstage9 = models.CharField(db_column='aZRLstage9', max_length=1)  # Field name made lowercase.
    azrlstage10 = models.CharField(db_column='aZRLstage10', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Rideravailability'


class Ridercategory(models.Model):
    cid = models.AutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    catref = models.CharField(db_column='catRef', max_length=2)  # Field name made lowercase.
    catref2 = models.CharField(db_column='catRef2', max_length=2)  # Field name made lowercase.
    catname = models.CharField(db_column='catName', max_length=20)  # Field name made lowercase.
    catlowerwkg = models.DecimalField(db_column='catLowerwkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    cathigherwkg = models.DecimalField(db_column='catHigherwkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    standardcat = models.CharField(db_column='standardCat', max_length=1)  # Field name made lowercase.
    divname = models.CharField(db_column='divName', max_length=20)  # Field name made lowercase.
    frhcname = models.CharField(db_column='FRHCname', max_length=20)  # Field name made lowercase.
    frhccode = models.CharField(db_column='FRHCcode', unique=True, max_length=3)  # Field name made lowercase.
    frhcwwkglimit = models.DecimalField(db_column='FRHCwWKGlimit', max_digits=5, decimal_places=2)  # Field name made lowercase.
    frhcvalue = models.IntegerField(db_column='FRHCvalue')  # Field name made lowercase.
    sortorder = models.CharField(db_column='Sortorder', max_length=10)  # Field name made lowercase.
    frhcup = models.CharField(db_column='FRHCup', max_length=10)  # Field name made lowercase.
    frhcdown = models.CharField(db_column='FRHCdown', max_length=10)  # Field name made lowercase.
    frhcroutehandicap = models.IntegerField(db_column='FRHCroutehandicap')  # Field name made lowercase.
    frhcstagedifficulty = models.IntegerField(db_column='FRHCstagedifficulty')  # Field name made lowercase.
    frhcsortorder = models.IntegerField(db_column='FRHCsortorder')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Ridercategory'


class Riders(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid', unique=True)  # Field name made lowercase.
    rname = models.CharField(db_column='rName', max_length=50)  # Field name made lowercase.
    rgender = models.CharField(db_column='rGender', max_length=1)  # Field name made lowercase.
    rlang = models.CharField(db_column='rLang', max_length=5)  # Field name made lowercase.
    rcty = models.CharField(db_column='rCTY', max_length=10)  # Field name made lowercase.
    rcat = models.CharField(db_column='rCat', max_length=2)  # Field name made lowercase.
    rcatw = models.CharField(db_column='rCatw', max_length=2)  # Field name made lowercase.
    frhccode = models.CharField(db_column='FRHCcode', max_length=3)  # Field name made lowercase.
    rexp = models.CharField(db_column='rEXP', max_length=15)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    rteamalt = models.CharField(db_column='rTeamALT', max_length=20)  # Field name made lowercase.
    rwkg = models.DecimalField(db_column='rWkg', max_digits=10, decimal_places=2)  # Field name made lowercase.
    rwattsavg = models.DecimalField(db_column='rWattsavg', max_digits=10, decimal_places=2)  # Field name made lowercase.
    rzname = models.CharField(db_column='rZname', max_length=50)  # Field name made lowercase.
    rwatt20m = models.IntegerField(db_column='rWatt20m')  # Field name made lowercase.
    rwkg20m = models.DecimalField(db_column='rWkg20m', max_digits=10, decimal_places=2)  # Field name made lowercase.
    rzftp = models.IntegerField(db_column='rZFTP')  # Field name made lowercase.
    rzrlroster1 = models.CharField(db_column='rZRLroster1', max_length=10)  # Field name made lowercase.
    rzrlroster2 = models.CharField(db_column='rZRLroster2', max_length=10)  # Field name made lowercase.
    rlrwkg = models.DecimalField(db_column='rLRwkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    frrrtname = models.CharField(db_column='frrRtname', max_length=30)  # Field name made lowercase.
    frrrseries = models.CharField(db_column='frrRseries', max_length=10)  # Field name made lowercase.
    frrrteamg = models.CharField(db_column='frrRteamg', max_length=30)  # Field name made lowercase.
    frrrfrhc = models.CharField(db_column='frrRFRHC', max_length=10)  # Field name made lowercase.
    rideractive = models.CharField(db_column='riderActive', max_length=1)  # Field name made lowercase.
    frrrraces = models.IntegerField(db_column='frrRraces')  # Field name made lowercase.
    frrtzone = models.CharField(db_column='frrTzone', max_length=10)  # Field name made lowercase.
    frrgctime = models.DecimalField(db_column='frrGCtime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    frrgcracect = models.IntegerField(db_column='frrGCracect')  # Field name made lowercase.
    frrtupdate = models.CharField(db_column='frrTupdate', max_length=30)  # Field name made lowercase.
    rtrainer = models.CharField(db_column='rTrainer', max_length=20)  # Field name made lowercase.
    rcontactemail = models.CharField(db_column='rContactemail', max_length=50)  # Field name made lowercase.
    rtrainerother = models.CharField(db_column='rTrainerother', max_length=30)  # Field name made lowercase.
    frrrpzone = models.CharField(db_column='frrRPZone', max_length=10)  # Field name made lowercase.
    frrrtc = models.CharField(db_column='frrRTC', max_length=1)  # Field name made lowercase.
    frrweight = models.DecimalField(db_column='frrWeight', max_digits=10, decimal_places=2)  # Field name made lowercase.
    frrcfrhc = models.CharField(db_column='frrCFRHC', max_length=3)  # Field name made lowercase.
    frrcwkg = models.DecimalField(db_column='frrCWKG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    frrrnp = models.IntegerField(db_column='frrRNP')  # Field name made lowercase.
    frrrnpdate = models.DateField(db_column='frrRNPdate')  # Field name made lowercase.
    frrfseries = models.CharField(db_column='frrFseries', max_length=10)  # Field name made lowercase.
    frrffrhc = models.CharField(db_column='frrFFRHC', max_length=10)  # Field name made lowercase.
    lastupdated = models.DateField(db_column='Lastupdated')  # Field name made lowercase.
    baselinefrhc = models.CharField(db_column='baselineFRHC', max_length=10)  # Field name made lowercase.
    riderfrhcchk = models.CharField(db_column='riderFRHCchk', max_length=1)  # Field name made lowercase.
    rccat = models.CharField(db_column='RCCAT', max_length=2)  # Field name made lowercase.
    rcfrhc = models.CharField(db_column='RCFRHC', max_length=10)  # Field name made lowercase.
    rcweight = models.DecimalField(db_column='RCWEIGHT', max_digits=6, decimal_places=2)  # Field name made lowercase.
    rcnp = models.IntegerField(db_column='RCNP')  # Field name made lowercase.
    rcwkg = models.DecimalField(db_column='RCWKG', max_digits=6, decimal_places=2)  # Field name made lowercase.
    tourteam = models.CharField(db_column='TourTeam', max_length=5)  # Field name made lowercase.
    tourteamjoin = models.CharField(db_column='TourTeamJoin', max_length=1)  # Field name made lowercase.
    eventmarketing = models.CharField(max_length=1)
    frrtseries = models.CharField(db_column='frrTseries', max_length=10)  # Field name made lowercase.
    frrtteamg = models.CharField(db_column='frrTteamg', max_length=30)  # Field name made lowercase.
    frrtfrhc = models.CharField(db_column='frrTFRHC', max_length=10)  # Field name made lowercase.
    frrtraces = models.IntegerField(db_column='frrTraces')  # Field name made lowercase.
    frrtstages = models.IntegerField(db_column='frrTstages')  # Field name made lowercase.
    touremail = models.CharField(max_length=1)
    tourfrance = models.CharField(max_length=1)
    tourbritannia = models.CharField(max_length=1)
    tourwatopia = models.CharField(max_length=1)
    tourworld = models.CharField(max_length=1)
    worldchamps = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'Riders'


class Sasettings(models.Model):
    settid = models.AutoField(db_column='SETTID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    memberlevel = models.IntegerField(db_column='memberLevel')  # Field name made lowercase.
    captainlevel = models.IntegerField(db_column='captainLevel')  # Field name made lowercase.
    adminlevel = models.IntegerField(db_column='adminLevel')  # Field name made lowercase.
    mteamlevel = models.IntegerField(db_column='mteamLevel')  # Field name made lowercase.
    memberband = models.IntegerField(db_column='memberBand')  # Field name made lowercase.
    memberrole = models.CharField(db_column='memberRole', max_length=20)  # Field name made lowercase.
    mteamrole = models.CharField(db_column='mteamRole', max_length=20)  # Field name made lowercase.
    captainband = models.IntegerField(db_column='captainBand')  # Field name made lowercase.
    mteamband = models.IntegerField(db_column='mteamBand')  # Field name made lowercase.
    adminband = models.IntegerField(db_column='adminBand')  # Field name made lowercase.
    adminaccount = models.CharField(db_column='adminAccount', max_length=10)  # Field name made lowercase.
    hometeam = models.CharField(db_column='homeTeam', max_length=10)  # Field name made lowercase.
    zrlleague = models.CharField(db_column='ZRLleague', max_length=15)  # Field name made lowercase.
    seriesopen = models.CharField(db_column='seriesOpen', max_length=10)  # Field name made lowercase.
    seriesracecompleted = models.IntegerField(db_column='seriesRacecompleted')  # Field name made lowercase.
    flashopen = models.CharField(db_column='flashOpen', max_length=10)  # Field name made lowercase.
    seriestsheet = models.IntegerField(db_column='seriesTsheet')  # Field name made lowercase.
    frrdefpw = models.CharField(db_column='frrDEFpw', max_length=20)  # Field name made lowercase.
    frrcommsdir = models.TextField(db_column='frrCommsdir')  # Field name made lowercase.
    frrpolicydir = models.TextField(db_column='frrPolicydir')  # Field name made lowercase.
    tttshowdetails = models.CharField(db_column='tttShowdetails', max_length=1)  # Field name made lowercase.
    frremail = models.CharField(db_column='FRRemail', max_length=50)  # Field name made lowercase.
    lboardresultmsg = models.TextField(db_column='lboardResultMSG')  # Field name made lowercase.
    testseries = models.CharField(db_column='testSeries', max_length=10)  # Field name made lowercase.
    resapihead = models.TextField()
    resapitail = models.TextField()
    ftsapihead = models.TextField()
    ftsapitail = models.TextField()
    frrbdoor = models.CharField(db_column='frrBdoor', max_length=20)  # Field name made lowercase.
    frruserbdoor = models.CharField(db_column='frrUserbdoor', max_length=20)  # Field name made lowercase.
    loginstatus = models.CharField(db_column='loginStatus', max_length=1)  # Field name made lowercase.
    loginstatusmessage = models.CharField(db_column='loginStatusmessage', max_length=100)  # Field name made lowercase.
    raceopen = models.CharField(db_column='raceOpen', max_length=10)  # Field name made lowercase.
    dcmatchref = models.CharField(max_length=20)
    prevmatchref = models.CharField(max_length=30)
    dcdefplayer = models.CharField(max_length=20)
    dcdashbrange = models.IntegerField()
    curseason = models.CharField(max_length=10)

    class Meta:
        
        db_table = 'SASettings'


class Sateamsettings(models.Model):
    settid = models.AutoField(db_column='SETTID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    dcmatchref = models.CharField(max_length=20)
    prevmatchref = models.CharField(max_length=30)
    dcdefplayer = models.CharField(max_length=20)
    dcdashbrange = models.IntegerField()
    curseason = models.CharField(max_length=10)

    class Meta:
        
        db_table = 'SATeamSettings'


class Saactionpoints(models.Model):
    apid = models.AutoField(db_column='APID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    matchref = models.CharField(db_column='MATCHREF', max_length=20)  # Field name made lowercase.
    periodref = models.CharField(db_column='PERIODREF', max_length=10)  # Field name made lowercase.
    applayerid = models.CharField(db_column='APPLAYERID', max_length=10)  # Field name made lowercase.
    puid = models.CharField(max_length=20)
    aptyperef = models.CharField(db_column='APTYPEREF', max_length=20)  # Field name made lowercase.
    aptypesubref = models.CharField(db_column='APTYPESUBREF', max_length=10)  # Field name made lowercase.
    aptimeref = models.CharField(db_column='APTIMEREF', max_length=10)  # Field name made lowercase.
    aptime = models.CharField(db_column='APTIME', max_length=10)  # Field name made lowercase.
    apclass = models.CharField(db_column='APCLASS', max_length=5)  # Field name made lowercase.
    aptype = models.CharField(db_column='APTYPE', max_length=5)  # Field name made lowercase.
    apoutcome = models.CharField(db_column='APOUTCOME', max_length=10)  # Field name made lowercase.
    applayerid2 = models.CharField(db_column='APPLAYERID2', max_length=20)  # Field name made lowercase.
    appakno = models.IntegerField(db_column='APPAKNO')  # Field name made lowercase.
    appakdefno = models.IntegerField(db_column='APPAKDEFNO')  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAactionpoints'


class Saactionpointtype(models.Model):
    aptyid = models.AutoField(db_column='APTYID', primary_key=True)  # Field name made lowercase.
    apcode = models.CharField(db_column='APCODE', max_length=10)  # Field name made lowercase.
    apdescription = models.CharField(db_column='APDESCRIPTION', max_length=30)  # Field name made lowercase.
    apshortcode = models.CharField(db_column='APSHORTCODE', max_length=10)  # Field name made lowercase.
    apclassref = models.CharField(db_column='APCLASSREF', max_length=1)  # Field name made lowercase.
    apexecution = models.CharField(db_column='APEXECUTION', max_length=1)  # Field name made lowercase.
    apoutcomeref = models.CharField(db_column='APOUTCOMEREF', max_length=1)  # Field name made lowercase.
    posssortorder = models.IntegerField(db_column='POSSSORTORDER')  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAactionpointtype'


class Samatch(models.Model):
    mtsid = models.AutoField(db_column='MTSID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    matchref = models.CharField(max_length=20)
    matchdate = models.DateField()
    kotime = models.CharField(max_length=10)
    ownteam = models.CharField(max_length=20)
    oppteam = models.CharField(max_length=20)
    htscore = models.CharField(max_length=10)
    ftscore = models.CharField(max_length=10)
    kozone = models.CharField(max_length=10)
    homeaway = models.CharField(max_length=10)
    matchcomment = models.TextField()
    matchseason = models.CharField(max_length=10)
    matchactive = models.CharField(max_length=1)
    matchcapture = models.CharField(max_length=1)
    matchtype = models.CharField(max_length=10)
    lastupdated = models.DateField()
    matchopposition = models.CharField(max_length=30)
    matchtracked = models.CharField(max_length=1)
    matchprev = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'SAmatch'


class Samatchgoal(models.Model):
    mtglid = models.AutoField(db_column='MTGLID', primary_key=True)  # Field name made lowercase.
    matchref = models.CharField(db_column='MATCHREF', max_length=20)  # Field name made lowercase.
    playerref = models.CharField(db_column='PLAYERREF', max_length=20)  # Field name made lowercase.
    goaltime = models.IntegerField(db_column='GOALTIME')  # Field name made lowercase.
    golfhalf = models.CharField(db_column='GOLFHALF', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAmatchgoal'


class Saobservationhistory(models.Model):
    obid = models.AutoField(db_column='OBID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    puid = models.CharField(max_length=20)
    obdate = models.DateTimeField()
    obuserid = models.CharField(max_length=20)
    obmsg1 = models.TextField()
    obmsg2 = models.TextField()
    obmsg3 = models.TextField()
    obmsg4 = models.TextField()
    obmsg5 = models.TextField()

    class Meta:
        
        db_table = 'SAobservationhistory'


class Saperiod(models.Model):
    perid = models.AutoField(db_column='PERID', primary_key=True)  # Field name made lowercase.
    periodref = models.CharField(db_column='PERIODREF', max_length=10)  # Field name made lowercase.
    prefdesc = models.CharField(db_column='PREFDESC', max_length=30)  # Field name made lowercase.
    phalf = models.CharField(db_column='PHALF', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAperiod'


class Sapitcharea(models.Model):
    ptaid = models.AutoField(db_column='PTAID', primary_key=True)  # Field name made lowercase.
    pitcharearef = models.CharField(db_column='PITCHAREAREF', max_length=10)  # Field name made lowercase.
    padesc = models.CharField(db_column='PADESC', max_length=30)  # Field name made lowercase.
    patype = models.CharField(db_column='PATYPE', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SApitcharea'


class Saplayer(models.Model):
    plid = models.AutoField(db_column='PLID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    puid = models.CharField(max_length=20)
    trackerid = models.CharField(max_length=10)
    frhccode = models.CharField(db_column='FRHCcode', max_length=4)  # Field name made lowercase.
    teampno = models.CharField(max_length=3)
    playertypeid = models.CharField(db_column='playertypeID', max_length=10)  # Field name made lowercase.
    playername = models.CharField(max_length=50)
    playerinitials = models.CharField(max_length=10)
    playergender = models.CharField(max_length=1)
    playerpossshortcode = models.CharField(max_length=5)
    pmainposition = models.CharField(max_length=20)
    psecondposition = models.CharField(max_length=20)
    pcurrentteam = models.CharField(max_length=20)
    pprevteam = models.CharField(max_length=20)
    playerbestfoot = models.CharField(max_length=10)
    playertwofooted = models.CharField(max_length=1)
    playershirtno = models.CharField(max_length=5)
    playerkey = models.CharField(max_length=1)
    playeractive = models.CharField(max_length=1)
    playeremail = models.CharField(max_length=100)
    playercomment = models.TextField()
    playermsg1 = models.TextField()
    playermsg2 = models.TextField()
    playermsg3 = models.TextField()
    playermsg4 = models.TextField()
    playermsg5 = models.TextField()
    lastupdated = models.DateField()

    class Meta:
        
        db_table = 'SAplayer'


class Saplayertype(models.Model):
    ptid = models.AutoField(db_column='PTID', primary_key=True)  # Field name made lowercase.
    playertypeid = models.CharField(db_column='playertypeID', max_length=10)  # Field name made lowercase.
    playertypedesc = models.CharField(max_length=30)
    ptaveragedistance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'SAplayertype'


class Sastatsports(models.Model):
    ssid = models.AutoField(db_column='SSID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    apexpname = models.CharField(max_length=30)
    statsegment = models.CharField(max_length=12)
    totaldistance = models.DecimalField(max_digits=10, decimal_places=2)
    distpermin = models.IntegerField()
    highspeedrun = models.IntegerField()
    highmetloaddist = models.IntegerField()
    maxspeed = models.DecimalField(max_digits=6, decimal_places=2)
    nosprints = models.IntegerField()
    sprintdist = models.IntegerField()
    noacc = models.IntegerField()
    nodeacc = models.IntegerField()
    calories = models.IntegerField()
    puid = models.CharField(max_length=20)
    matchref = models.CharField(max_length=20)
    lastupdated = models.DateField()
    gametime = models.IntegerField()
    oldid = models.CharField(max_length=20)
    goalscored = models.IntegerField()
    goalassist = models.IntegerField()
    cleansheet = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'SAstatsports'


class Sateam(models.Model):
    rtid = models.AutoField(db_column='RTID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', unique=True, max_length=20)  # Field name made lowercase.
    teamname = models.CharField(max_length=30)
    teamnameshort = models.CharField(max_length=10)
    teamactive = models.CharField(max_length=1)
    teamdefpw = models.CharField(max_length=20)
    venuepostcode = models.CharField(max_length=20)
    pitchcomment = models.TextField()
    teamstep = models.CharField(max_length=20)
    lastupdated = models.DateField()
    teamshortcode = models.CharField(max_length=5)

    class Meta:
        
        db_table = 'SAteam'


class Sateamsheet(models.Model):
    tsid = models.AutoField(db_column='TSID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    matchref = models.CharField(max_length=20)
    p1 = models.CharField(db_column='P1', max_length=20)  # Field name made lowercase.
    p2 = models.CharField(db_column='P2', max_length=20)  # Field name made lowercase.
    p3 = models.CharField(db_column='P3', max_length=20)  # Field name made lowercase.
    p4 = models.CharField(db_column='P4', max_length=20)  # Field name made lowercase.
    p5 = models.CharField(db_column='P5', max_length=20)  # Field name made lowercase.
    p6 = models.CharField(db_column='P6', max_length=20)  # Field name made lowercase.
    p7 = models.CharField(db_column='P7', max_length=20)  # Field name made lowercase.
    p8 = models.CharField(db_column='P8', max_length=20)  # Field name made lowercase.
    p9 = models.CharField(db_column='P9', max_length=20)  # Field name made lowercase.
    p10 = models.CharField(db_column='P10', max_length=20)  # Field name made lowercase.
    p11 = models.CharField(db_column='P11', max_length=20)  # Field name made lowercase.
    p12 = models.CharField(db_column='P12', max_length=20)  # Field name made lowercase.
    p13 = models.CharField(db_column='P13', max_length=20)  # Field name made lowercase.
    p14 = models.CharField(db_column='P14', max_length=20)  # Field name made lowercase.
    p15 = models.CharField(db_column='P15', max_length=20)  # Field name made lowercase.
    p16 = models.CharField(db_column='P16', max_length=20)  # Field name made lowercase.
    p17 = models.CharField(db_column='P17', max_length=20)  # Field name made lowercase.
    p18 = models.CharField(db_column='P18', max_length=20)  # Field name made lowercase.
    p19 = models.CharField(db_column='P19', max_length=20)  # Field name made lowercase.
    p20 = models.CharField(db_column='P20', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAteamsheet'


class Sauser(models.Model):
    uidno = models.AutoField(db_column='UIDNO', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', unique=True, max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=40)  # Field name made lowercase.
    userpw = models.CharField(db_column='Userpw', max_length=255)  # Field name made lowercase.
    userlvl = models.IntegerField(db_column='Userlvl')  # Field name made lowercase.
    userrole = models.CharField(db_column='Userrole', max_length=15)  # Field name made lowercase.
    appservice = models.CharField(db_column='Appservice', max_length=10)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=15)  # Field name made lowercase.
    user3rmember = models.CharField(db_column='User3Rmember', max_length=1)  # Field name made lowercase.
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=30)
    useremail = models.CharField(db_column='userEmail', max_length=255)  # Field name made lowercase.
    resetemail = models.TextField(db_column='resetEmail')  # Field name made lowercase.
    resetsent = models.CharField(db_column='resetSent', max_length=1)  # Field name made lowercase.
    resetdate = models.DateField(db_column='resetDate')  # Field name made lowercase.
    userstatus = models.CharField(db_column='userStatus', max_length=1)  # Field name made lowercase.
    lastloggedin = models.DateField(db_column='lastLoggedin')  # Field name made lowercase.
    lastpw = models.TextField(db_column='lastPW')  # Field name made lowercase.
    newpw = models.CharField(db_column='newPW', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SAuser'


class Series(models.Model):
    srid = models.AutoField(db_column='SRID', primary_key=True)  # Field name made lowercase.
    seriescode = models.CharField(db_column='seriesCode', max_length=5)  # Field name made lowercase.
    seriestest = models.CharField(db_column='seriesTest', max_length=1)  # Field name made lowercase.
    seriestype = models.CharField(db_column='seriesType', max_length=10)  # Field name made lowercase.
    seriesrrlimit = models.IntegerField(db_column='seriesRRlimit')  # Field name made lowercase.
    seriesbonusrace = models.IntegerField(db_column='seriesBonusrace')  # Field name made lowercase.
    seriesno = models.IntegerField(db_column='seriesNo')  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', unique=True, max_length=10)  # Field name made lowercase.
    seriesname = models.CharField(db_column='seriesName', max_length=40)  # Field name made lowercase.
    seriesshowpass = models.CharField(db_column='seriesShowpass', max_length=1)  # Field name made lowercase.
    seriesshowttpass = models.CharField(db_column='seriesShowTTpass', max_length=1)  # Field name made lowercase.
    seriesactivestatus = models.CharField(db_column='seriesactiveStatus', max_length=2)  # Field name made lowercase.
    nextteamno = models.IntegerField(db_column='nextTeamno')  # Field name made lowercase.
    seriesregistrationactive = models.CharField(db_column='seriesregistrationActive', max_length=1)  # Field name made lowercase.
    seriesarchive = models.CharField(max_length=1)
    seriesriders = models.IntegerField(db_column='seriesRiders')  # Field name made lowercase.
    seriesstart = models.DateField(db_column='seriesStart')  # Field name made lowercase.
    seriesteamevent = models.CharField(db_column='seriesTeamevent', max_length=1)  # Field name made lowercase.
    seriesregclosedate = models.DateField(db_column='seriesregClosedate')  # Field name made lowercase.
    series3ronly = models.CharField(db_column='series3Ronly', max_length=1)  # Field name made lowercase.
    seriesinternalonly = models.CharField(db_column='seriesInternalonly', max_length=1)  # Field name made lowercase.
    seriesrules = models.CharField(db_column='seriesRules', max_length=255)  # Field name made lowercase.
    seriesposter = models.CharField(db_column='seriesPoster', max_length=50)  # Field name made lowercase.
    seriesriderpack = models.CharField(db_column='seriesRiderpack', max_length=50)  # Field name made lowercase.
    seriesmidraceupdate = models.CharField(db_column='seriesMidraceupdate', max_length=50)  # Field name made lowercase.
    seriesfinalreport = models.CharField(db_column='seriesFinalreport', max_length=50)  # Field name made lowercase.
    seriesnxtmno = models.IntegerField(db_column='seriesNxtmno')  # Field name made lowercase.
    seriesshortname = models.CharField(db_column='seriesShortname', max_length=15)  # Field name made lowercase.
    seriesstageno = models.IntegerField(db_column='seriesStageno')  # Field name made lowercase.
    seriesmsg = models.CharField(db_column='seriesMSG', max_length=30)  # Field name made lowercase.
    seriesreftest = models.CharField(db_column='seriesReftest', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Series'


class Seriesldiv(models.Model):
    seriesldid = models.AutoField(db_column='seriesLDid', primary_key=True)  # Field name made lowercase.
    seriesldcat = models.CharField(db_column='seriesLDcat', max_length=3)  # Field name made lowercase.
    seriesldfrhc = models.CharField(db_column='seriesLDfrhc', max_length=5)  # Field name made lowercase.

    class Meta:
        
        db_table = 'SeriesLDIV'


class Seriesfeedback(models.Model):
    sfbid = models.AutoField(db_column='SFBID', primary_key=True)  # Field name made lowercase.
    fbref = models.CharField(db_column='fbRef', max_length=50)  # Field name made lowercase.
    feedbackdate = models.DateField(db_column='feedbackDate')  # Field name made lowercase.
    issuetype = models.CharField(db_column='issueType', max_length=2)  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=15)  # Field name made lowercase.
    feedbackadminid = models.IntegerField(db_column='feedbackadminID')  # Field name made lowercase.
    feedbackadminname = models.CharField(db_column='feedbackadminName', max_length=30)  # Field name made lowercase.
    feedbacktext = models.TextField(db_column='feedbackText')  # Field name made lowercase.
    rccommenttext = models.TextField(db_column='rccommentText')  # Field name made lowercase.
    feedbackstatus = models.CharField(db_column='feedbackStatus', max_length=1)  # Field name made lowercase.
    showfeedback = models.CharField(db_column='showFeedback', max_length=1)  # Field name made lowercase.
    userfbrole = models.CharField(db_column='userfbRole', max_length=15)  # Field name made lowercase.
    lastupdatedate = models.DateField(db_column='lastupdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Seriesfeedback'


class Seriesinformation(models.Model):
    siid = models.AutoField(db_column='SIID', primary_key=True)  # Field name made lowercase.
    seriesmid = models.CharField(db_column='seriesMID', unique=True, max_length=10)  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', max_length=10)  # Field name made lowercase.
    postdate = models.DateField(db_column='postDate')  # Field name made lowercase.
    infomno = models.IntegerField(db_column='infoMno')  # Field name made lowercase.
    infolang = models.CharField(db_column='INFOLANG', max_length=10)  # Field name made lowercase.
    shownote = models.CharField(db_column='showNote', max_length=1)  # Field name made lowercase.
    infonote = models.TextField()
    notetag = models.CharField(db_column='noteTag', max_length=15)  # Field name made lowercase.
    infocreatedby = models.IntegerField(db_column='infoCreatedby')  # Field name made lowercase.
    infocreatedbyname = models.CharField(db_column='infoCreatedbyname', max_length=50)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Seriesinformation'


class Seriesregistration(models.Model):
    serid = models.AutoField(db_column='serID', primary_key=True)  # Field name made lowercase.
    sridref = models.CharField(db_column='srIDref', max_length=25)  # Field name made lowercase.
    srregdate = models.DateField(db_column='srRegdate')  # Field name made lowercase.
    srteam = models.CharField(db_column='srTeam', max_length=30)  # Field name made lowercase.
    srteamname = models.CharField(db_column='srTeamname', max_length=50)  # Field name made lowercase.
    srcontactname = models.CharField(db_column='srContactname', max_length=40)  # Field name made lowercase.
    srcontactemail = models.CharField(db_column='srContactemail', max_length=50)  # Field name made lowercase.
    srcontacttype = models.CharField(db_column='srContacttype', max_length=3)  # Field name made lowercase.
    srstatus = models.CharField(db_column='srStatus', max_length=10)  # Field name made lowercase.
    srseriesref = models.CharField(db_column='srSeriesref', max_length=10)  # Field name made lowercase.
    srverificationzpid = models.IntegerField(db_column='srverificationZPID')  # Field name made lowercase.
    srsinglerider = models.CharField(db_column='srsingleRider', max_length=1)  # Field name made lowercase.
    sridercat = models.CharField(db_column='sRiderCAT', max_length=1)  # Field name made lowercase.
    sriderzone = models.CharField(db_column='sRiderZone', max_length=10)  # Field name made lowercase.
    sridergender = models.CharField(db_column='sriderGender', max_length=1)  # Field name made lowercase.
    sriderwkg = models.CharField(db_column='sRiderwkg', max_length=10)  # Field name made lowercase.
    tcaptain = models.CharField(db_column='tCaptain', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Seriesregistration'


class Tttleaguestandings(models.Model):
    lrid = models.AutoField(db_column='LRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=50)  # Field name made lowercase.
    leagueteamref = models.CharField(db_column='leagueTeamref', unique=True, max_length=50)  # Field name made lowercase.
    teamclub = models.CharField(db_column='Teamclub', max_length=50, verbose_name="Team")  # Field name made lowercase.
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
    leagueteamname = models.CharField(db_column='leagueteamName', max_length=30, verbose_name="Team")  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.
    eventrbonus = models.DecimalField(db_column='eventRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    teamtsprint = models.DecimalField(db_column='teamTSPRINT', max_digits=15, decimal_places=3)  # Field name made lowercase.
    teamtkom = models.DecimalField(db_column='teamTKOM', max_digits=15, decimal_places=3)  # Field name made lowercase.
    komteambonus = models.IntegerField(db_column='KOMTEAMBONUS')  # Field name made lowercase.
    sprintteambonus = models.IntegerField(db_column='SPRINTTEAMBONUS')  # Field name made lowercase.
    totalriderbonus = models.IntegerField(db_column='TOTALRIDERBONUS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTLeagueStandings'


class Tttriderstats(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    leaguefrhc = models.CharField(db_column='leagueFRHC', max_length=20)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    finishtotal = models.DecimalField(db_column='finishTotal', max_digits=10, decimal_places=3)  # Field name made lowercase.
    segmenttotalfts = models.DecimalField(db_column='segmentTotalFTS', max_digits=10, decimal_places=3)  # Field name made lowercase.
    totalsf = models.DecimalField(db_column='totalSF', max_digits=15, decimal_places=3)  # Field name made lowercase.
    rbonus = models.DecimalField(db_column='rBonus', max_digits=5, decimal_places=2)  # Field name made lowercase.
    totaltpt = models.DecimalField(db_column='totalTPT', max_digits=15, decimal_places=3)  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=15, decimal_places=3)  # Field name made lowercase.
    calcdate = models.DateField()
    riderwatts = models.IntegerField(db_column='riderWatts')  # Field name made lowercase.
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    exreason = models.CharField(db_column='exReason', max_length=20)  # Field name made lowercase.
    resultselected = models.CharField(db_column='resultSelected', max_length=1)  # Field name made lowercase.
    exreasoncode = models.CharField(db_column='exReasoncode', max_length=10)  # Field name made lowercase.
    totalpen = models.IntegerField(db_column='totalPen')  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30)  # Field name made lowercase.
    kompoints = models.DecimalField(db_column='KOMpoints', max_digits=15, decimal_places=3)  # Field name made lowercase.
    sprintpoints = models.DecimalField(db_column='SPRINTpoints', max_digits=15, decimal_places=3)  # Field name made lowercase.
    tbonus = models.IntegerField(db_column='tBonus')  # Field name made lowercase.
    rmply = models.DecimalField(db_column='rMply', max_digits=5, decimal_places=2)  # Field name made lowercase.
    gcttime = models.DecimalField(db_column='GCttime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=30)  # Field name made lowercase.
    racefrhc = models.CharField(db_column='raceFRHC', max_length=5)  # Field name made lowercase.
    racefrhcpos = models.IntegerField(db_column='raceFRHCpos')  # Field name made lowercase.
    zeventid = models.CharField(db_column='zEventid', max_length=15)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tttime = models.DecimalField(db_column='TTTIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    tttpos = models.IntegerField(db_column='TTTPOS')  # Field name made lowercase.
    teamttpos = models.IntegerField(db_column='teamTTPOS')  # Field name made lowercase.
    tkombonus = models.IntegerField(db_column='TKOMBONUS')  # Field name made lowercase.
    tsprintbonus = models.IntegerField(db_column='TSPRINTBONUS')  # Field name made lowercase.
    evorder = models.IntegerField()

    class Meta:
        
        db_table = 'TTTRiderSTATS'


class Tttstagerescalc(models.Model):
    resid = models.AutoField(db_column='RESID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='RACENO')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    teamleague = models.CharField(max_length=50)
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.
    frhcfinpos = models.IntegerField(db_column='frhcFINpos')  # Field name made lowercase.
    raceridertime = models.IntegerField()
    frhcaddtime = models.IntegerField(db_column='FRHCaddtime')  # Field name made lowercase.
    ridertime = models.DecimalField(max_digits=12, decimal_places=3)
    riderwatts = models.IntegerField()
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    riderwkg = models.DecimalField(max_digits=10, decimal_places=2)
    riderttttime = models.DecimalField(db_column='riderTTTtime', max_digits=10, decimal_places=3)  # Field name made lowercase.
    rbasetime = models.DecimalField(max_digits=15, decimal_places=3)
    finpoints = models.DecimalField(db_column='FINpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    segpoints = models.DecimalField(db_column='SEGpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    penpoints = models.IntegerField(db_column='PENpoints')  # Field name made lowercase.
    bonuspoints = models.DecimalField(db_column='BONUSpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    totalpoints = models.DecimalField(db_column='TOTALpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    evref = models.CharField(unique=True, max_length=30)
    totalraces = models.IntegerField(db_column='TOTALraces')  # Field name made lowercase.
    sprintpoints = models.DecimalField(db_column='SPRINTpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    kompoints = models.DecimalField(db_column='KOMpoints', max_digits=10, decimal_places=3)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rdate = models.DateField(db_column='RDATE')  # Field name made lowercase.
    rinc = models.CharField(db_column='RINC', max_length=1)  # Field name made lowercase.
    teampoints = models.DecimalField(db_column='TEAMpoints', max_digits=15, decimal_places=2)  # Field name made lowercase.
    teamname = models.CharField(max_length=50)
    tttdelay1 = models.DecimalField(db_column='TTTdelay1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    tttdelay2 = models.DecimalField(db_column='TTTdelay2', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegbonus = models.DecimalField(db_column='TSEGBONUS', max_digits=10, decimal_places=3)  # Field name made lowercase.
    tttpos = models.IntegerField(db_column='TTTPOS')  # Field name made lowercase.
    teamttpos = models.IntegerField(db_column='teamTTPOS')  # Field name made lowercase.
    evfrhcdif = models.IntegerField(db_column='evFRHCdif')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageResCALC'


class Tttstageresridertotal(models.Model):
    rtid = models.AutoField(db_column='RTID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    racenoasat = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    totraceno = models.IntegerField()
    evorder = models.IntegerField()
    totbonus = models.IntegerField()

    class Meta:
        
        db_table = 'TTTStageResRIDERTOTAL'


class Tttstageresrteam(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    teamref = models.CharField(max_length=20)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    rpoints = models.IntegerField(db_column='Rpoints')  # Field name made lowercase.
    bpoints = models.IntegerField(db_column='Bpoints')  # Field name made lowercase.
    tpoints = models.IntegerField(db_column='Tpoints')  # Field name made lowercase.
    rinc = models.CharField(db_column='RINC', max_length=1)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rpos = models.IntegerField(db_column='RPOS')  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rtime = models.DecimalField(db_column='RTIME', max_digits=15, decimal_places=3)  # Field name made lowercase.
    tdelay1 = models.DecimalField(db_column='TDELAY1', max_digits=6, decimal_places=2)  # Field name made lowercase.
    tdelay2 = models.DecimalField(db_column='TDELAY2', max_digits=6, decimal_places=2)  # Field name made lowercase.
    stime = models.DecimalField(db_column='STIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMPOINTS')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTPOINTS')  # Field name made lowercase.
    finpoints = models.IntegerField(db_column='FINPOINTS')  # Field name made lowercase.
    bonuspoints = models.IntegerField(db_column='BONUSPOINTS')  # Field name made lowercase.
    teamname = models.CharField(db_column='Teamname', max_length=50)  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageResRTEAM'


class Tttstageresteam(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    teamref = models.CharField(max_length=20)
    teamleague = models.CharField(max_length=30)
    teampoints = models.IntegerField(db_column='TEAMpoints')  # Field name made lowercase.
    teamrcount = models.IntegerField(db_column='TEAMRcount')  # Field name made lowercase.
    teamrpoints = models.IntegerField(db_column='TEAMRpoints')  # Field name made lowercase.
    trzid = models.IntegerField(db_column='TRZID')  # Field name made lowercase.
    teampos = models.IntegerField(db_column='TEAMPOS')  # Field name made lowercase.
    tttime = models.DecimalField(db_column='TTtime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    teamfinpoints = models.IntegerField(db_column='TEAMFINPOINTS')  # Field name made lowercase.
    teamkompoints = models.IntegerField(db_column='TEAMKOMPOINTS')  # Field name made lowercase.
    teamsprintpoints = models.IntegerField(db_column='TEAMSPRINTPOINTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageResTEAM'


class Tttstagesegcalc(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    segtype = models.CharField(db_column='SEGTYPE', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    evsegref = models.CharField(unique=True, max_length=30)
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.
    segpos = models.IntegerField()
    segpband = models.IntegerField()
    segtime = models.DecimalField(max_digits=12, decimal_places=3)
    segbuffertime = models.IntegerField()
    segtimelimit = models.IntegerField()
    segwatts = models.IntegerField()
    segwkg = models.DecimalField(max_digits=10, decimal_places=2)
    segpoints = models.DecimalField(max_digits=15, decimal_places=3)
    segsprintpoints = models.IntegerField(db_column='segSPRINTpoints')  # Field name made lowercase.
    segkompoints = models.IntegerField(db_column='segKOMpoints')  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    segbasetime = models.IntegerField(db_column='SEGbasetime')  # Field name made lowercase.
    evfrhcdif = models.IntegerField(db_column='evFRHCdif')  # Field name made lowercase.
    teamname = models.CharField(db_column='Teamname', max_length=50)  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegCALC'


class Tttstagesegtkom(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.
    gctime = models.DecimalField(db_column='GCTIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    segwkg = models.DecimalField(db_column='SEGWKG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    segwatts = models.IntegerField(db_column='SEGWATTS')  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.
    teamname = models.CharField(db_column='Teamname', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegTKOM'


class Tttstagesegtkombonus(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    tsegpoints = models.DecimalField(max_digits=10, decimal_places=3)
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegTKOMBONUS'


class Tttstagesegtlapbonus(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    tsegpoints = models.DecimalField(max_digits=10, decimal_places=3)
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegTLAPBONUS'


class Tttstagesegtsprint(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.
    gctime = models.DecimalField(db_column='GCTIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    segwkg = models.DecimalField(db_column='SEGWKG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    segwatts = models.IntegerField(db_column='SEGWATTS')  # Field name made lowercase.
    rclub = models.CharField(db_column='RCLUB', max_length=50)  # Field name made lowercase.
    teamname = models.CharField(db_column='Teamname', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegTSPRINT'


class Tttstagesegtsprintbonus(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    tsegpoints = models.DecimalField(max_digits=10, decimal_places=3)
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'TTTStageSegTSPRINTBONUS'


class Teamlatestzrl(models.Model):
    zrlid = models.AutoField(db_column='ZRLID', primary_key=True)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='RZID')  # Field name made lowercase.
    rtid = models.CharField(db_column='RTID', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TeamLatestZRL'


class Teams(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    tteamid = models.CharField(db_column='tTeamID', unique=True, max_length=10)  # Field name made lowercase.
    tteamleagueid = models.CharField(db_column='tTeamleagueID', max_length=50)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=25)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=20)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueref = models.CharField(db_column='leagueRef', max_length=20)  # Field name made lowercase.
    traceseries = models.CharField(db_column='tRaceseries', max_length=3)  # Field name made lowercase.
    traceleaguename = models.CharField(db_column='tRaceleaguename', max_length=10)  # Field name made lowercase.
    tzrlwo = models.CharField(db_column='tZRLwo', max_length=1)  # Field name made lowercase.
    tracetime = models.CharField(db_column='tRacetime', max_length=4)  # Field name made lowercase.
    traceleaguetrc = models.CharField(db_column='tRaceleagueTRC', max_length=6)  # Field name made lowercase.
    traceleagueref = models.CharField(db_column='tRaceleagueref', max_length=10)  # Field name made lowercase.
    tracepen = models.CharField(db_column='tRacepen', max_length=2)  # Field name made lowercase.
    tracedelay = models.CharField(db_column='tRacedelay', max_length=6)  # Field name made lowercase.
    tracetag = models.CharField(db_column='tRacetag', max_length=25)  # Field name made lowercase.
    tracesegpx = models.DecimalField(db_column='tRacesegpx', max_digits=5, decimal_places=2)  # Field name made lowercase.
    tracefinptx = models.DecimalField(db_column='tRacefinptx', max_digits=5, decimal_places=2)  # Field name made lowercase.
    traceteamptx = models.DecimalField(db_column='tRaceteamptx', max_digits=5, decimal_places=2)  # Field name made lowercase.
    triderid1 = models.IntegerField(db_column='tRiderID1')  # Field name made lowercase.
    triderid2 = models.IntegerField(db_column='tRiderID2')  # Field name made lowercase.
    triderid3 = models.IntegerField(db_column='tRiderID3')  # Field name made lowercase.
    triderid4 = models.IntegerField(db_column='tRiderID4')  # Field name made lowercase.
    triderid5 = models.IntegerField(db_column='tRiderID5')  # Field name made lowercase.
    triderid6 = models.IntegerField(db_column='tRiderID6')  # Field name made lowercase.
    triderid7 = models.IntegerField(db_column='tRiderID7')  # Field name made lowercase.
    triderid8 = models.IntegerField(db_column='tRiderID8')  # Field name made lowercase.
    triderid9 = models.IntegerField(db_column='tRiderID9')  # Field name made lowercase.
    triderid10 = models.IntegerField(db_column='tRiderID10')  # Field name made lowercase.
    triderid11 = models.IntegerField(db_column='tRiderID11')  # Field name made lowercase.
    triderid12 = models.IntegerField(db_column='tRiderID12')  # Field name made lowercase.
    traceds = models.IntegerField(db_column='tRaceDS')  # Field name made lowercase.
    tno = models.IntegerField(db_column='tNO')  # Field name made lowercase.
    ttttcc = models.CharField(db_column='tTTTCC', max_length=20)  # Field name made lowercase.
    tzrlcat = models.CharField(db_column='tZRLCAT', max_length=1)  # Field name made lowercase.
    tzrldiv = models.IntegerField(db_column='tZRLDIV')  # Field name made lowercase.
    tzrlcomment = models.CharField(db_column='tZRLcomment', max_length=50)  # Field name made lowercase.
    ttttcomment = models.CharField(db_column='tTTTcomment', max_length=50)  # Field name made lowercase.
    trostername = models.CharField(db_column='tRostername', max_length=10)  # Field name made lowercase.
    tsortorder = models.IntegerField(db_column='tSortorder')  # Field name made lowercase.
    ttttzlink = models.CharField(db_column='tTTTZlink', max_length=255)  # Field name made lowercase.
    tteamactive = models.CharField(db_column='tTeamactive', max_length=1)  # Field name made lowercase.
    tlastupdate = models.DateField(db_column='tLastupdate')  # Field name made lowercase.
    tlastupdateid = models.IntegerField(db_column='tLastupdateID')  # Field name made lowercase.
    trideridsel1 = models.CharField(db_column='tRiderIDSEL1', max_length=1)  # Field name made lowercase.
    trideridsel2 = models.CharField(db_column='tRiderIDSEL2', max_length=1)  # Field name made lowercase.
    trideridsel3 = models.CharField(db_column='tRiderIDSEL3', max_length=1)  # Field name made lowercase.
    trideridsel4 = models.CharField(db_column='tRiderIDSEL4', max_length=1)  # Field name made lowercase.
    trideridsel5 = models.CharField(db_column='tRiderIDSEL5', max_length=1)  # Field name made lowercase.
    trideridsel6 = models.CharField(db_column='tRiderIDSEL6', max_length=1)  # Field name made lowercase.
    trideridsel7 = models.CharField(db_column='tRiderIDSEL7', max_length=1)  # Field name made lowercase.
    trideridsel8 = models.CharField(db_column='tRiderIDSEL8', max_length=1)  # Field name made lowercase.
    trideridsel9 = models.CharField(db_column='tRiderIDSEL9', max_length=1)  # Field name made lowercase.
    trideridsel10 = models.CharField(db_column='tRiderIDSEL10', max_length=1)  # Field name made lowercase.
    trideridsel11 = models.CharField(db_column='tRiderIDSEL11', max_length=1)  # Field name made lowercase.
    trideridsel12 = models.CharField(db_column='tRiderIDSEL12', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Teams'


class Trainer(models.Model):
    trid = models.AutoField(db_column='TRID', primary_key=True)  # Field name made lowercase.
    trref = models.CharField(db_column='TRref', max_length=20)  # Field name made lowercase.
    trname = models.CharField(db_column='TRname', max_length=40)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Trainer'


class Users(models.Model):
    uidno = models.AutoField(db_column='UIDNO', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', unique=True, max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=40)  # Field name made lowercase.
    userpw = models.CharField(db_column='Userpw', max_length=255)  # Field name made lowercase.
    userlvl = models.IntegerField(db_column='Userlvl')  # Field name made lowercase.
    userrole = models.CharField(db_column='Userrole', max_length=15)  # Field name made lowercase.
    recruitingcontact = models.CharField(max_length=1)
    appservice = models.CharField(db_column='Appservice', max_length=10)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=15)  # Field name made lowercase.
    user3rmember = models.CharField(db_column='User3Rmember', max_length=1)  # Field name made lowercase.
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=30)
    useremail = models.CharField(db_column='userEmail', max_length=255)  # Field name made lowercase.
    resetemail = models.TextField(db_column='resetEmail')  # Field name made lowercase.
    resetsent = models.CharField(db_column='resetSent', max_length=1)  # Field name made lowercase.
    resetdate = models.DateField(db_column='resetDate')  # Field name made lowercase.
    userstatus = models.CharField(db_column='userStatus', max_length=1)  # Field name made lowercase.
    lastloggedin = models.DateField(db_column='lastLoggedin')  # Field name made lowercase.
    lastpw = models.TextField(db_column='lastPW')  # Field name made lowercase.
    newpw = models.CharField(db_column='newPW', max_length=255)  # Field name made lowercase.
    prevteam = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'Users'


class Zcourse(models.Model):
    zcid = models.AutoField(db_column='ZCID', primary_key=True)  # Field name made lowercase.
    zcref = models.CharField(db_column='ZCREF', max_length=20)  # Field name made lowercase.
    zwlref = models.CharField(db_column='ZWLREF', max_length=20)  # Field name made lowercase.
    zcname = models.CharField(db_column='ZCname', max_length=50)  # Field name made lowercase.
    zcdistance = models.IntegerField(db_column='ZCdistance')  # Field name made lowercase.
    zcelevation = models.IntegerField(db_column='ZCelevation')  # Field name made lowercase.
    zclink = models.TextField(db_column='ZClink')  # Field name made lowercase.
    zcnote = models.TextField(db_column='ZCnote')  # Field name made lowercase.
    zwref = models.CharField(db_column='ZWref', max_length=10)  # Field name made lowercase.
    routebasetime = models.IntegerField(db_column='ROUTEbasetime')  # Field name made lowercase.
    capbasetime = models.IntegerField(db_column='CAPbasetime')  # Field name made lowercase.
    crpbasetime = models.IntegerField(db_column='CRPbasetime')  # Field name made lowercase.
    ghtbasetime = models.IntegerField(db_column='GHTbasetime')  # Field name made lowercase.
    habbasetime = models.IntegerField(db_column='HABbasetime')  # Field name made lowercase.
    bonbasetime = models.IntegerField(db_column='BONbasetime')  # Field name made lowercase.
    caybasetime = models.IntegerField(db_column='CAYbasetime')  # Field name made lowercase.
    jlpbastime = models.IntegerField(db_column='JLPbastime')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Zcourse'


class Zsegment(models.Model):
    segid = models.AutoField(db_column='SEGID', primary_key=True)  # Field name made lowercase.
    segref = models.CharField(db_column='SEGref', max_length=25)  # Field name made lowercase.
    zwref = models.CharField(db_column='ZWREF', max_length=20)  # Field name made lowercase.
    segname = models.CharField(db_column='SEGname', max_length=40)  # Field name made lowercase.
    segtype = models.CharField(db_column='SEGtype', max_length=10)  # Field name made lowercase.
    segzpref = models.CharField(db_column='SEGZPREF', unique=True, max_length=10)  # Field name made lowercase.
    segdistance = models.CharField(db_column='SEGdistance', max_length=10)  # Field name made lowercase.
    zwsname = models.CharField(db_column='ZWSNAME', max_length=3)  # Field name made lowercase.
    segbasetime = models.IntegerField(db_column='SEGbasetime')  # Field name made lowercase.
    segbuffertime = models.IntegerField(db_column='SEGbuffertime')  # Field name made lowercase.
    segincluded = models.CharField(db_column='SEGincluded', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Zsegment'


class Zworld(models.Model):
    zwlid = models.AutoField(db_column='ZWLID', primary_key=True)  # Field name made lowercase.
    zwsystemid = models.CharField(db_column='ZWsystemID', max_length=10)  # Field name made lowercase.
    zwlref = models.CharField(db_column='ZWLref', max_length=20)  # Field name made lowercase.
    zwlname = models.CharField(db_column='ZWLname', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Zworld'


class Aeventsegprocess(models.Model):
    proid = models.AutoField(primary_key=True)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    eventid = models.IntegerField()
    prostart = models.DateTimeField()
    proend = models.DateTimeField()

    class Meta:
        
        db_table = 'aEventsegprocess'


class Atesttable(models.Model):
    tid = models.AutoField(primary_key=True)
    series = models.CharField(max_length=10)
    team = models.CharField(max_length=20)
    tkom = models.IntegerField(db_column='TKOM')  # Field name made lowercase.
    tsprint = models.IntegerField(db_column='TSPRINT')  # Field name made lowercase.

    class Meta:
        
        db_table = 'aTesttable'





















class Fraccessaudit(models.Model):
    accid = models.AutoField(db_column='ACCID', primary_key=True)  # Field name made lowercase.
    accdate = models.DateTimeField(db_column='accDate')  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    userteam = models.CharField(db_column='userTeam', max_length=20)  # Field name made lowercase.
    useraction = models.TextField(db_column='userAction')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frAccessaudit'


class Frawardtype(models.Model):
    awtid = models.AutoField(db_column='AWTID', primary_key=True)  # Field name made lowercase.
    awardtyperef = models.CharField(db_column='awardtypeRef', unique=True, max_length=20)  # Field name made lowercase.
    awardtypename = models.CharField(db_column='awardtypeName', max_length=50)  # Field name made lowercase.
    awardtypeactive = models.CharField(db_column='awardtypeActive', max_length=1)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frAwardtype'


class Frdivlchange(models.Model):
    dlid = models.AutoField(db_column='DLID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=50)  # Field name made lowercase.
    newlev = models.CharField(db_column='newLEV', max_length=1)  # Field name made lowercase.
    newdiv = models.IntegerField(db_column='newDIV')  # Field name made lowercase.
    tttnote = models.CharField(db_column='TTTnote', max_length=15)  # Field name made lowercase.
    tttpen = models.CharField(db_column='TTTpen', max_length=3)  # Field name made lowercase.
    tttdelay = models.CharField(db_column='TTTdelay', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frDIVLchange'


class Freteamriders(models.Model):
    evtid = models.AutoField(db_column='EVTID', primary_key=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=50)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='RZID')  # Field name made lowercase.
    rname = models.CharField(db_column='rName', max_length=50)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=50)  # Field name made lowercase.
    tdiv = models.CharField(db_column='tDiv', max_length=2)  # Field name made lowercase.
    tdivl = models.IntegerField(db_column='tDivL')  # Field name made lowercase.
    rcat = models.CharField(db_column='rCAT', max_length=10)  # Field name made lowercase.
    tzone = models.CharField(db_column='tZone', max_length=10)  # Field name made lowercase.
    teamswitchid = models.CharField(db_column='teamSwitchID', max_length=50)  # Field name made lowercase.
    rzone = models.CharField(db_column='rZone', max_length=10)  # Field name made lowercase.
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frETeamRiders'


class Freventteam(models.Model):
    etid = models.AutoField(db_column='ETID', primary_key=True)  # Field name made lowercase.
    etzteam = models.CharField(db_column='etZTeam', max_length=15)  # Field name made lowercase.
    etteamid = models.CharField(db_column='etTeamID', unique=True, max_length=50)  # Field name made lowercase.
    etteamname = models.CharField(db_column='etTeamname', max_length=30)  # Field name made lowercase.
    teamlevel = models.IntegerField(db_column='teamLevel')  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.
    penaltypts = models.IntegerField(db_column='penaltyPTS')  # Field name made lowercase.
    evteamactive = models.CharField(db_column='evTeamactive', max_length=1)  # Field name made lowercase.
    etteamgender = models.CharField(db_column='etTeamgender', max_length=5)  # Field name made lowercase.
    etteamdiv = models.CharField(db_column='etTeamDIV', max_length=5)  # Field name made lowercase.
    etdivrating = models.CharField(db_column='etDIVrating', max_length=2)  # Field name made lowercase.
    etteamdivl = models.IntegerField(db_column='etTeamDIVL')  # Field name made lowercase.
    etteamno = models.IntegerField(db_column='etTeamno')  # Field name made lowercase.
    etseriesref = models.CharField(db_column='etseriesRef', max_length=10)  # Field name made lowercase.
    etleagueref = models.CharField(db_column='etleagueRef', max_length=30)  # Field name made lowercase.
    etteammanager = models.CharField(db_column='etTeammanager', max_length=30)  # Field name made lowercase.
    teammanagerzid = models.IntegerField(db_column='teammanagerZID')  # Field name made lowercase.
    etteamcontact = models.CharField(db_column='etTeamcontact', max_length=50)  # Field name made lowercase.
    etteamregdate = models.DateField(db_column='etTeamregdate')  # Field name made lowercase.
    ettca = models.CharField(db_column='etTCa', max_length=1)  # Field name made lowercase.
    etntt = models.CharField(db_column='etNTT', max_length=1)  # Field name made lowercase.
    etrider1 = models.CharField(db_column='etRider1', max_length=30)  # Field name made lowercase.
    etrider1zid = models.IntegerField(db_column='etRider1zid')  # Field name made lowercase.
    etrider2 = models.CharField(db_column='etRider2', max_length=30)  # Field name made lowercase.
    etrider2zid = models.IntegerField(db_column='etRider2zid')  # Field name made lowercase.
    etrider3 = models.CharField(db_column='etRider3', max_length=30)  # Field name made lowercase.
    etrider3zid = models.IntegerField(db_column='etRider3zid')  # Field name made lowercase.
    etrider4 = models.CharField(db_column='etRider4', max_length=30)  # Field name made lowercase.
    etrider4zid = models.IntegerField(db_column='etRider4zid')  # Field name made lowercase.
    etrider5 = models.CharField(db_column='etRider5', max_length=30)  # Field name made lowercase.
    etrider5zid = models.IntegerField(db_column='etRider5zid')  # Field name made lowercase.
    etrider6 = models.CharField(db_column='etRider6', max_length=30)  # Field name made lowercase.
    etrider6zid = models.IntegerField(db_column='etRider6zid')  # Field name made lowercase.
    etrider7 = models.CharField(db_column='etRider7', max_length=30)  # Field name made lowercase.
    etrider7zid = models.IntegerField(db_column='etRider7zid')  # Field name made lowercase.
    etrider8 = models.CharField(db_column='etRider8', max_length=30)  # Field name made lowercase.
    etrider8zid = models.IntegerField(db_column='etRider8zid')  # Field name made lowercase.
    etrider9 = models.CharField(db_column='etRider9', max_length=30)  # Field name made lowercase.
    etrider9zid = models.IntegerField(db_column='etRider9zid')  # Field name made lowercase.
    etrider10 = models.CharField(db_column='etRider10', max_length=30)  # Field name made lowercase.
    etrider10zid = models.IntegerField(db_column='etRider10zid')  # Field name made lowercase.
    etrider1cat = models.CharField(db_column='etRider1CAT', max_length=2)  # Field name made lowercase.
    etrider2cat = models.CharField(db_column='etRider2CAT', max_length=2)  # Field name made lowercase.
    etrider3cat = models.CharField(db_column='etRider3CAT', max_length=2)  # Field name made lowercase.
    etrider4cat = models.CharField(db_column='etRider4CAT', max_length=2)  # Field name made lowercase.
    etrider5cat = models.CharField(db_column='etRider5CAT', max_length=2)  # Field name made lowercase.
    etrider6cat = models.CharField(db_column='etRider6CAT', max_length=2)  # Field name made lowercase.
    etrider7cat = models.CharField(db_column='etRider7CAT', max_length=2)  # Field name made lowercase.
    etrider8cat = models.CharField(db_column='etRider8CAT', max_length=2)  # Field name made lowercase.
    etrider9cat = models.CharField(db_column='etRider9CAT', max_length=2)  # Field name made lowercase.
    etrider10cat = models.CharField(db_column='etRider10CAT', max_length=2)  # Field name made lowercase.
    etteamstatus = models.CharField(db_column='etteamStatus', max_length=10)  # Field name made lowercase.
    etteamcomment = models.CharField(db_column='etteamComment', max_length=255)  # Field name made lowercase.
    teamttt1pen = models.CharField(db_column='TeamTTT1pen', max_length=1)  # Field name made lowercase.
    teamttt1delay = models.DecimalField(db_column='TeamTTT1delay', max_digits=6, decimal_places=2)  # Field name made lowercase.
    teamttt1group = models.CharField(db_column='TeamTTT1group', max_length=20)  # Field name made lowercase.
    teamttt2pen = models.CharField(db_column='TeamTTT2pen', max_length=2)  # Field name made lowercase.
    teamttt2delay = models.DecimalField(db_column='TeamTTT2delay', max_digits=6, decimal_places=2)  # Field name made lowercase.
    teamttt2group = models.CharField(db_column='TeamTTT2group', max_length=20)  # Field name made lowercase.
    etrole = models.CharField(db_column='etRole', max_length=15)  # Field name made lowercase.
    etfbnxtref = models.IntegerField(db_column='etfbnxtRef')  # Field name made lowercase.
    rider1races = models.IntegerField()
    rider2races = models.IntegerField()
    rider3races = models.IntegerField()
    rider4races = models.IntegerField()
    rider5races = models.IntegerField()
    rider6races = models.IntegerField()
    rider7races = models.IntegerField()
    rider8races = models.IntegerField()
    rider9races = models.IntegerField()
    rider10races = models.IntegerField()
    indrider = models.CharField(db_column='indRider', max_length=1)  # Field name made lowercase.
    ettzone = models.CharField(db_column='etTzone', max_length=10)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=15)  # Field name made lowercase.
    etlzone = models.CharField(db_column='etLZone', max_length=10)  # Field name made lowercase.
    ettrno = models.IntegerField(db_column='etTRNO')  # Field name made lowercase.
    ettrval = models.IntegerField(db_column='etTRVAL')  # Field name made lowercase.
    ttevent1 = models.IntegerField(db_column='TTevent1')  # Field name made lowercase.
    ttevent2 = models.IntegerField(db_column='TTevent2')  # Field name made lowercase.
    signuptzone = models.CharField(db_column='signupTzone', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frEventTeam'


class Freventtourpass(models.Model):
    evtpid = models.AutoField(db_column='EVTPID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', max_length=10)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    tpgroup = models.CharField(db_column='TPgroup', max_length=10)  # Field name made lowercase.
    racetype = models.CharField(db_column='raceType', max_length=10)  # Field name made lowercase.
    tpalt = models.CharField(db_column='TPALT', max_length=2)  # Field name made lowercase.
    racetime = models.CharField(db_column='raceTime', max_length=5)  # Field name made lowercase.
    utcorder = models.IntegerField(db_column='UTCorder')  # Field name made lowercase.
    eventfinal = models.CharField(db_column='eventFINAL', max_length=1)  # Field name made lowercase.
    hidepass = models.CharField(db_column='hidePass', max_length=1)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    tpass = models.TextField(db_column='TPass')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frEventTourPass'


class Freventsignup(models.Model):
    evsid = models.AutoField(db_column='EVSID', primary_key=True)  # Field name made lowercase.
    evseries = models.CharField(db_column='evSeries', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rname = models.CharField(db_column='rName', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='rTeam', max_length=20)  # Field name made lowercase.
    rcat = models.CharField(db_column='rCat', max_length=3)  # Field name made lowercase.
    rweight = models.DecimalField(db_column='rWeight', max_digits=10, decimal_places=2)  # Field name made lowercase.
    rcfrhc = models.CharField(db_column='rCFRHC', max_length=10)  # Field name made lowercase.
    rcwkg = models.CharField(db_column='rCWKG', max_length=10)  # Field name made lowercase.
    rnp = models.CharField(db_column='rNP', max_length=10)  # Field name made lowercase.
    signupdate = models.DateField(db_column='signupDate')  # Field name made lowercase.
    revcode = models.CharField(db_column='revCode', max_length=10)  # Field name made lowercase.
    entryupdated = models.DateField(db_column='entryUpdated')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frEventsignup'


class Frfrhccheck(models.Model):
    fchkid = models.AutoField(db_column='fchkID', primary_key=True)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    submitdate = models.DateField(db_column='submitDate')  # Field name made lowercase.
    rgender = models.CharField(db_column='rGender', max_length=1)  # Field name made lowercase.
    rcat = models.CharField(db_column='rCat', max_length=5)  # Field name made lowercase.
    rweight = models.IntegerField(db_column='rWeight')  # Field name made lowercase.
    rnp = models.IntegerField(db_column='rNP')  # Field name made lowercase.
    rnpdate = models.DateField(db_column='rNPdate')  # Field name made lowercase.
    reviewdate = models.DateField(db_column='reviewDate')  # Field name made lowercase.
    frhcset = models.CharField(db_column='FRHCset', max_length=10)  # Field name made lowercase.
    frhcwkg = models.DecimalField(db_column='FRHCwkg', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frFRHCcheck'


class Frfrhcseries2Check(models.Model):
    chkid = models.AutoField(db_column='CHKID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    ridername = models.CharField(db_column='RIDERNAME', max_length=100)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='RZID')  # Field name made lowercase.
    riderteam = models.CharField(db_column='RIDERTEAM', max_length=50)  # Field name made lowercase.
    eventcat = models.CharField(db_column='EVENTCAT', max_length=5)  # Field name made lowercase.
    eventgender = models.CharField(db_column='EVENTGENDER', max_length=1)  # Field name made lowercase.
    eventkg = models.DecimalField(db_column='EVENTKG', max_digits=6, decimal_places=2)  # Field name made lowercase.
    eventage = models.CharField(db_column='EVENTAGE', max_length=10)  # Field name made lowercase.
    eventnp = models.IntegerField(db_column='EVENTNP')  # Field name made lowercase.
    curfrhc = models.CharField(db_column='CURFRHC', max_length=10)  # Field name made lowercase.
    ridergender = models.CharField(db_column='RIDERGENDER', max_length=1)  # Field name made lowercase.
    ridermxcat = models.CharField(db_column='RIDERMXCAT', max_length=5)  # Field name made lowercase.
    calcwkg = models.DecimalField(db_column='CALCWKG', max_digits=6, decimal_places=2)  # Field name made lowercase.
    newfrhc = models.CharField(db_column='NEWFRHC', max_length=10)  # Field name made lowercase.
    assessdate = models.DateField(db_column='ASSESSDATE')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frFRHCseries2check'


class Frinfotrans(models.Model):
    inid = models.AutoField(db_column='INID', primary_key=True)  # Field name made lowercase.
    pgref = models.CharField(db_column='PGREF', max_length=15)  # Field name made lowercase.
    pgmsgno = models.IntegerField(db_column='PGMSGNO')  # Field name made lowercase.
    lang = models.CharField(db_column='LANG', max_length=5)  # Field name made lowercase.
    msgtxt = models.TextField(db_column='MSGTXT')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frInfotrans'


class Frlanguage(models.Model):
    lgid = models.AutoField(db_column='LGID', primary_key=True)  # Field name made lowercase.
    langref = models.CharField(db_column='LANGREF', max_length=5)  # Field name made lowercase.
    langdesc = models.CharField(db_column='LANGDESC', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frLanguage'


class Frleaguestandings(models.Model):
    lrid = models.AutoField(db_column='LRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=50)  # Field name made lowercase.
    leagueteamref = models.CharField(db_column='leagueTeamref', unique=True, max_length=50)  # Field name made lowercase.
    leagueteamid = models.CharField(db_column='leagueTeamID', max_length=50)  # Field name made lowercase.
    leaguerno = models.IntegerField(db_column='leagueRno')  # Field name made lowercase.
    leagueteamtsegfol = models.IntegerField(db_column='leagueTeamTSEGFOL')  # Field name made lowercase.
    leagueteamtsegfts = models.IntegerField(db_column='leagueTeamTSEGFTS')  # Field name made lowercase.
    leagueteamtfin = models.IntegerField(db_column='leagueTeamTFIN')  # Field name made lowercase.
    leagueteamsfpts = models.IntegerField(db_column='leagueTeamSFpts')  # Field name made lowercase.
    leagueteamlpts = models.IntegerField(db_column='leagueTeamLPTS')  # Field name made lowercase.
    tlptsonly = models.IntegerField(db_column='TLPTSonly')  # Field name made lowercase.
    leaguerecalcdate = models.DateField(db_column='leagueRecalcdate')  # Field name made lowercase.
    leaguetotaltpen = models.IntegerField(db_column='leaguetotalTPEN')  # Field name made lowercase.
    leagueteamname = models.CharField(db_column='leagueteamName', max_length=30)  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.
    eventrbonus = models.DecimalField(db_column='eventRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    teamtsprint = models.IntegerField(db_column='teamTSPRINT')  # Field name made lowercase.
    teamtkom = models.IntegerField(db_column='teamTKOM')  # Field name made lowercase.
    komteambonus = models.IntegerField(db_column='KOMTEAMBONUS')  # Field name made lowercase.
    sprintteambonus = models.IntegerField(db_column='SPRINTTEAMBONUS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frLeagueStandings'


class Frleagueteambonus(models.Model):
    tbid = models.AutoField(db_column='TBID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leaguezone = models.CharField(db_column='leagueZone', max_length=10)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=50)  # Field name made lowercase.
    tsprintbonus = models.IntegerField(db_column='tSPRINTbonus')  # Field name made lowercase.
    tkombonus = models.IntegerField(db_column='tKOMbonus')  # Field name made lowercase.
    tgcbonus = models.IntegerField(db_column='tGCbonus')  # Field name made lowercase.
    ttotalbonus = models.IntegerField(db_column='tTOTALbonus')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frLeagueteamBonus'


class Frpoints(models.Model):
    ptid = models.AutoField(db_column='PTID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    pttype = models.CharField(db_column='PTTYPE', max_length=5)  # Field name made lowercase.
    cat = models.CharField(db_column='CAT', max_length=5)  # Field name made lowercase.
    pos = models.IntegerField(db_column='POS')  # Field name made lowercase.
    points = models.IntegerField(db_column='POINTS')  # Field name made lowercase.
    stpoints = models.IntegerField(db_column='STPOINTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frPoints'


class Frresults(models.Model):
    resid = models.AutoField(db_column='ResID', primary_key=True)  # Field name made lowercase.
    resevid = models.CharField(db_column='ResEVID', unique=True, max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueref = models.CharField(db_column='leagueRef', max_length=50)  # Field name made lowercase.
    raceteamid = models.CharField(db_column='raceTeamID', max_length=50)  # Field name made lowercase.
    resraceno = models.IntegerField(db_column='ResRaceno')  # Field name made lowercase.
    resteamid = models.CharField(db_column='ResTeamID', max_length=50)  # Field name made lowercase.
    resracedate = models.DateField(db_column='ResRacedate')  # Field name made lowercase.
    resriderid1 = models.IntegerField(db_column='ResRiderID1')  # Field name made lowercase.
    resrider1fol = models.IntegerField(db_column='ResRider1FOL')  # Field name made lowercase.
    resrider1fin = models.IntegerField(db_column='ResRider1fin')  # Field name made lowercase.
    resriderid2 = models.IntegerField(db_column='ResRiderID2')  # Field name made lowercase.
    resrider2fol = models.IntegerField(db_column='ResRider2FOL')  # Field name made lowercase.
    resrider2fin = models.IntegerField(db_column='ResRider2fin')  # Field name made lowercase.
    resriderid3 = models.IntegerField(db_column='ResRiderID3')  # Field name made lowercase.
    resrider3fol = models.IntegerField(db_column='ResRider3FOL')  # Field name made lowercase.
    resrider3fin = models.IntegerField(db_column='ResRider3fin')  # Field name made lowercase.
    resriderid4 = models.IntegerField(db_column='ResRiderID4')  # Field name made lowercase.
    resrider4fol = models.IntegerField(db_column='ResRider4FOL')  # Field name made lowercase.
    resrider4fin = models.IntegerField(db_column='ResRider4fin')  # Field name made lowercase.
    resriderid5 = models.IntegerField(db_column='ResRiderID5')  # Field name made lowercase.
    resrider5fol = models.IntegerField(db_column='ResRider5FOL')  # Field name made lowercase.
    resrider5fin = models.IntegerField(db_column='ResRider5fin')  # Field name made lowercase.
    resriderid6 = models.IntegerField(db_column='ResRiderID6')  # Field name made lowercase.
    resrider6fol = models.IntegerField(db_column='ResRider6FOL')  # Field name made lowercase.
    resrider6fin = models.IntegerField(db_column='ResRider6fin')  # Field name made lowercase.
    resteamleaguepts = models.IntegerField(db_column='ResTeamleaguepts')  # Field name made lowercase.
    resrider1wkg = models.DecimalField(db_column='ResRider1wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider2wkg = models.DecimalField(db_column='ResRider2wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider3wkg = models.DecimalField(db_column='ResRider3wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider4wkg = models.DecimalField(db_column='ResRider4wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider5wkg = models.DecimalField(db_column='ResRider5wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider6wkg = models.DecimalField(db_column='ResRider6wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider7wkg = models.DecimalField(db_column='ResRider7wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resrider8wkg = models.DecimalField(db_column='ResRider8wkg', max_digits=5, decimal_places=2)  # Field name made lowercase.
    resriderid7 = models.IntegerField(db_column='ResRiderID7')  # Field name made lowercase.
    resrider7fol = models.IntegerField(db_column='ResRider7FOL')  # Field name made lowercase.
    resrider7fin = models.IntegerField(db_column='ResRider7fin')  # Field name made lowercase.
    resriderid8 = models.IntegerField(db_column='ResRiderID8')  # Field name made lowercase.
    resrider8fol = models.IntegerField(db_column='ResRider8FOL')  # Field name made lowercase.
    resrider8fin = models.IntegerField(db_column='ResRider8fin')  # Field name made lowercase.
    resrider1fts = models.IntegerField(db_column='ResRider1FTS')  # Field name made lowercase.
    resrider2fts = models.IntegerField(db_column='ResRider2FTS')  # Field name made lowercase.
    resrider3fts = models.IntegerField(db_column='ResRider3FTS')  # Field name made lowercase.
    resrider4fts = models.IntegerField(db_column='ResRider4FTS')  # Field name made lowercase.
    resrider5fts = models.IntegerField(db_column='ResRider5FTS')  # Field name made lowercase.
    resrider6fts = models.IntegerField(db_column='ResRider6FTS')  # Field name made lowercase.
    resrider7fts = models.IntegerField(db_column='ResRider7FTS')  # Field name made lowercase.
    resrider8fts = models.IntegerField(db_column='ResRider8FTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frResults'


class Frriderpenalty(models.Model):
    penid = models.AutoField(primary_key=True)
    seriesref = models.CharField(max_length=10)
    eventid = models.IntegerField()
    rzid = models.IntegerField()
    raceno = models.IntegerField()
    pentype = models.CharField(max_length=10)
    riderpenalty = models.IntegerField()
    penreason = models.TextField()
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frRiderPENALTY'


class Frriderstats(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totaltpt = models.IntegerField(db_column='totalTPT')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    calcdate = models.DateField()
    riderwatts = models.IntegerField(db_column='riderWatts')  # Field name made lowercase.
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    exreason = models.CharField(db_column='exReason', max_length=20)  # Field name made lowercase.
    resultselected = models.CharField(db_column='resultSelected', max_length=1)  # Field name made lowercase.
    exreasoncode = models.CharField(db_column='exReasoncode', max_length=10)  # Field name made lowercase.
    totalpen = models.IntegerField(db_column='totalPen')  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30)  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMpoints')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTpoints')  # Field name made lowercase.
    tbonus = models.IntegerField(db_column='tBonus')  # Field name made lowercase.
    rbonus = models.DecimalField(db_column='rBonus', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rmply = models.DecimalField(db_column='rMply', max_digits=5, decimal_places=2)  # Field name made lowercase.
    gcttime = models.DecimalField(db_column='GCttime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=30)  # Field name made lowercase.
    racefrhc = models.CharField(db_column='raceFRHC', max_length=5)  # Field name made lowercase.
    racefrhcpos = models.IntegerField(db_column='raceFRHCpos')  # Field name made lowercase.
    zeventid = models.CharField(db_column='zEventid', max_length=15)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tttime = models.DecimalField(db_column='TTTIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    tttpos = models.IntegerField(db_column='TTTPOS')  # Field name made lowercase.
    teamttpos = models.IntegerField(db_column='teamTTPOS')  # Field name made lowercase.
    tkombonus = models.IntegerField(db_column='TKOMBONUS')  # Field name made lowercase.
    tsprintbonus = models.IntegerField(db_column='TSPRINTBONUS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frRiderSTATS'


class Frriderstandings(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=20)  # Field name made lowercase.
    teamriderref = models.CharField(db_column='teamriderRef', unique=True, max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=20)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    recalcdate = models.DateField(db_column='recalcDate')  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    totalrpen = models.IntegerField(db_column='totalRPEN')  # Field name made lowercase.
    riderteamname = models.CharField(db_column='riderteamName', max_length=30)  # Field name made lowercase.
    totalkom = models.IntegerField(db_column='totalKOM')  # Field name made lowercase.
    totalsprint = models.IntegerField(db_column='totalSPRINT')  # Field name made lowercase.
    totalrbonus = models.DecimalField(db_column='totalRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    totalgctime = models.DecimalField(db_column='totalGCtime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=20)  # Field name made lowercase.
    gcracect = models.IntegerField(db_column='GCracect')  # Field name made lowercase.
    riderfrhc = models.CharField(db_column='riderFRHC', max_length=10)  # Field name made lowercase.
    lzone = models.CharField(db_column='lZone', max_length=10)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    gctotaltime = models.CharField(db_column='GCtotaltime', max_length=15)  # Field name made lowercase.
    racersort = models.CharField(db_column='raceRSORT', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frRiderStandings'


class Frriderstatsindividual(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totaltpt = models.IntegerField(db_column='totalTPT')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    calcdate = models.DateField()
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    exreason = models.CharField(db_column='exReason', max_length=20)  # Field name made lowercase.
    resultselected = models.CharField(db_column='resultSelected', max_length=1)  # Field name made lowercase.
    exreasoncode = models.CharField(db_column='exReasoncode', max_length=10)  # Field name made lowercase.
    timefull = models.CharField(db_column='timeFull', max_length=30)  # Field name made lowercase.
    timevalue = models.CharField(db_column='timeValue', max_length=20)  # Field name made lowercase.
    timehr = models.CharField(db_column='timeHR', max_length=2)  # Field name made lowercase.
    timemin = models.CharField(db_column='timeMIN', max_length=2)  # Field name made lowercase.
    timesec = models.CharField(db_column='timeSEC', max_length=6)  # Field name made lowercase.
    totalpen = models.IntegerField(db_column='totalPen')  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30)  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMpoints')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTpoints')  # Field name made lowercase.
    tbonus = models.IntegerField(db_column='tBonus')  # Field name made lowercase.
    rbonus = models.DecimalField(db_column='rBonus', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rmply = models.DecimalField(db_column='rMply', max_digits=5, decimal_places=2)  # Field name made lowercase.
    frrgctime = models.DecimalField(db_column='frrGCtime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    gcracetbonus = models.IntegerField(db_column='GCracetbonus')  # Field name made lowercase.
    gctracetbonus = models.IntegerField(db_column='GCtracetbonus')  # Field name made lowercase.
    gcttime = models.DecimalField(db_column='GCttime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=30)  # Field name made lowercase.
    racefrhc = models.CharField(db_column='raceFRHC', max_length=5)  # Field name made lowercase.
    racefrhcpos = models.CharField(db_column='raceFRHCpos', max_length=10)  # Field name made lowercase.
    racezone = models.CharField(db_column='raceZone', max_length=10)  # Field name made lowercase.
    racersort = models.CharField(db_column='raceRSORT', max_length=20)  # Field name made lowercase.
    zeventid = models.CharField(db_column='zEventid', max_length=15)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frRiderStatsindividual'


class Frsegmentresults(models.Model):
    segrid = models.AutoField(db_column='SEGRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segref = models.CharField(db_column='SEGref', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    ridertime = models.DecimalField(db_column='riderTime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    segwatts = models.IntegerField(db_column='SEGwatts')  # Field name made lowercase.
    segwkg = models.CharField(db_column='SEGwkg', max_length=10)  # Field name made lowercase.
    segtimedisp = models.CharField(db_column='SEGtimedisp', max_length=15)  # Field name made lowercase.
    segeffort = models.CharField(db_column='SEGeffort', max_length=30)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=40)  # Field name made lowercase.
    lzone = models.CharField(db_column='LZONE', max_length=10)  # Field name made lowercase.
    racerank = models.CharField(db_column='raceRANK', max_length=15)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGpos')  # Field name made lowercase.
    segpoints = models.IntegerField(db_column='SEGpoints')  # Field name made lowercase.
    segzpref = models.CharField(db_column='SEGZPREF', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frSegmentResults'


class Frseriesawards(models.Model):
    sawid = models.AutoField(db_column='SAWID', primary_key=True)  # Field name made lowercase.
    awardref = models.CharField(db_column='awardRef', unique=True, max_length=30)  # Field name made lowercase.
    awardleaguezone = models.CharField(db_column='awardLeaguezone', max_length=10)  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', max_length=10)  # Field name made lowercase.
    awardcat = models.CharField(db_column='awardCat', max_length=2)  # Field name made lowercase.
    awarddiv = models.CharField(db_column='awardDIV', max_length=3)  # Field name made lowercase.
    awardtyperef = models.CharField(db_column='awardtypeRef', max_length=20)  # Field name made lowercase.
    awardteamname = models.CharField(db_column='awardTeamname', max_length=50)  # Field name made lowercase.
    awardridername = models.CharField(db_column='awardRidername', max_length=50)  # Field name made lowercase.
    awardriderzid = models.IntegerField(db_column='awardRiderZID')  # Field name made lowercase.
    awarddate = models.DateField(db_column='awardDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frSeriesawards'


class Frsettings(models.Model):
    settid = models.AutoField(db_column='SETTID', primary_key=True)  # Field name made lowercase.
    newclub = models.CharField(max_length=30)
    memberlevel = models.IntegerField(db_column='memberLevel')  # Field name made lowercase.
    captainlevel = models.IntegerField(db_column='captainLevel')  # Field name made lowercase.
    adminlevel = models.IntegerField(db_column='adminLevel')  # Field name made lowercase.
    mteamlevel = models.IntegerField(db_column='mteamLevel')  # Field name made lowercase.
    memberband = models.IntegerField(db_column='memberBand')  # Field name made lowercase.
    memberrole = models.CharField(db_column='memberRole', max_length=20)  # Field name made lowercase.
    mteamrole = models.CharField(db_column='mteamRole', max_length=20)  # Field name made lowercase.
    deflang = models.CharField(db_column='defLang', max_length=5)  # Field name made lowercase.
    captainband = models.IntegerField(db_column='captainBand')  # Field name made lowercase.
    mteamband = models.IntegerField(db_column='mteamBand')  # Field name made lowercase.
    adminband = models.IntegerField(db_column='adminBand')  # Field name made lowercase.
    adminaccount = models.CharField(db_column='adminAccount', max_length=10)  # Field name made lowercase.
    hometeam = models.CharField(db_column='homeTeam', max_length=10)  # Field name made lowercase.
    zrlleague = models.CharField(db_column='ZRLleague', max_length=15)  # Field name made lowercase.
    seriesopen = models.CharField(db_column='seriesOpen', max_length=10)  # Field name made lowercase.
    nexttourseries = models.CharField(db_column='nextTourseries', max_length=10)  # Field name made lowercase.
    nextraceseries = models.CharField(db_column='nextRaceseries', max_length=10)  # Field name made lowercase.
    seriesracecompleted = models.IntegerField(db_column='seriesRacecompleted')  # Field name made lowercase.
    gccheck = models.IntegerField(db_column='GCcheck')  # Field name made lowercase.
    flashopen = models.CharField(db_column='flashOpen', max_length=10)  # Field name made lowercase.
    seriestsheet = models.IntegerField(db_column='seriesTsheet')  # Field name made lowercase.
    frrdefpw = models.CharField(db_column='frrDEFpw', max_length=20)  # Field name made lowercase.
    frrcommsdir = models.TextField(db_column='frrCommsdir')  # Field name made lowercase.
    frrpolicydir = models.TextField(db_column='frrPolicydir')  # Field name made lowercase.
    tttshowdetails = models.CharField(db_column='tttShowdetails', max_length=1)  # Field name made lowercase.
    frremail = models.CharField(db_column='FRRemail', max_length=50)  # Field name made lowercase.
    lboardresultmsg = models.TextField(db_column='lboardResultMSG')  # Field name made lowercase.
    testseries = models.CharField(db_column='testSeries', max_length=10)  # Field name made lowercase.
    resapihead = models.TextField()
    resapitail = models.TextField()
    ftsapihead = models.TextField()
    ftsapitail = models.TextField()
    frrbdoor = models.CharField(db_column='frrBdoor', max_length=20)  # Field name made lowercase.
    frruserbdoor = models.CharField(db_column='frrUserbdoor', max_length=20)  # Field name made lowercase.
    loginstatus = models.CharField(db_column='loginStatus', max_length=1)  # Field name made lowercase.
    loginstatusmessage = models.CharField(db_column='loginStatusmessage', max_length=100)  # Field name made lowercase.
    raceopen = models.CharField(db_column='raceOpen', max_length=10)  # Field name made lowercase.
    defappservice = models.CharField(max_length=10)
    tourresultmsg = models.TextField(db_column='tourResultMSG')  # Field name made lowercase.
    nexttourposter = models.TextField()
    tourreport = models.TextField()
    tourpodium = models.TextField()
    tourfranceposter = models.TextField()
    tourbritanniaposter = models.TextField()
    tourwatopiaposter = models.TextField()
    tourworldposter = models.TextField()
    worldchamposter = models.TextField()
    tourscheduleposter = models.TextField()

    class Meta:
        
        db_table = 'frSettings'


class Frstagerescalc(models.Model):
    resid = models.AutoField(db_column='RESID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='RACENO')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    teamleague = models.CharField(max_length=50)
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.
    frhcfinpos = models.IntegerField(db_column='frhcFINpos')  # Field name made lowercase.
    ridertime = models.DecimalField(max_digits=12, decimal_places=3)
    riderwatts = models.IntegerField()
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    riderwkg = models.DecimalField(max_digits=10, decimal_places=2)
    riderttttime = models.DecimalField(db_column='riderTTTtime', max_digits=10, decimal_places=3)  # Field name made lowercase.
    finpoints = models.IntegerField(db_column='FINpoints')  # Field name made lowercase.
    segpoints = models.IntegerField(db_column='SEGpoints')  # Field name made lowercase.
    bonuspoints = models.IntegerField(db_column='BONUSpoints')  # Field name made lowercase.
    totalpoints = models.IntegerField(db_column='TOTALpoints')  # Field name made lowercase.
    evref = models.CharField(unique=True, max_length=30)
    totalraces = models.IntegerField(db_column='TOTALraces')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTpoints')  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMpoints')  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rdate = models.DateField(db_column='RDATE')  # Field name made lowercase.
    rinc = models.CharField(db_column='RINC', max_length=1)  # Field name made lowercase.
    teampoints = models.DecimalField(db_column='TEAMpoints', max_digits=15, decimal_places=2)  # Field name made lowercase.
    teamname = models.CharField(max_length=50)
    tttdelay = models.DecimalField(db_column='TTTdelay', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegbonus = models.IntegerField(db_column='TSEGBONUS')  # Field name made lowercase.
    tttpos = models.IntegerField(db_column='TTTPOS')  # Field name made lowercase.
    teamttpos = models.IntegerField(db_column='teamTTPOS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageResCALC'


class Frstageresload(models.Model):
    resid = models.AutoField(db_column='RESID', primary_key=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    frhcfinpos = models.IntegerField(db_column='frhcFINpos')  # Field name made lowercase.
    ridertime = models.DecimalField(max_digits=12, decimal_places=3)
    riderwatts = models.IntegerField()
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    riderwkg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'frStageResLOAD'


class Frstageresrteam(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    teamref = models.CharField(max_length=20)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rpoints = models.IntegerField(db_column='Rpoints')  # Field name made lowercase.
    rinc = models.CharField(db_column='RINC', max_length=1)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rpos = models.IntegerField(db_column='RPOS')  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rtime = models.DecimalField(db_column='RTIME', max_digits=15, decimal_places=3)  # Field name made lowercase.
    tdelay = models.IntegerField(db_column='TDELAY')  # Field name made lowercase.
    stime = models.DecimalField(db_column='STIME', max_digits=10, decimal_places=3)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageResRTEAM'


class Frstageresteam(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    teamref = models.CharField(max_length=20)
    teamleague = models.CharField(max_length=30)
    teampoints = models.IntegerField(db_column='TEAMpoints')  # Field name made lowercase.
    teamrcount = models.IntegerField(db_column='TEAMRcount')  # Field name made lowercase.
    teamrpoints = models.IntegerField(db_column='TEAMRpoints')  # Field name made lowercase.
    trzid = models.IntegerField(db_column='TRZID')  # Field name made lowercase.
    teampos = models.IntegerField(db_column='TEAMPOS')  # Field name made lowercase.
    tttime = models.DecimalField(db_column='TTtime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageResTEAM'


class Frstagesegcalc(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    segtype = models.CharField(db_column='SEGTYPE', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    evsegref = models.CharField(unique=True, max_length=30)
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.
    segpos = models.IntegerField()
    segtime = models.DecimalField(max_digits=12, decimal_places=3)
    segwatts = models.IntegerField()
    segwkg = models.DecimalField(max_digits=10, decimal_places=2)
    segpoints = models.IntegerField()
    segsprintpoints = models.IntegerField(db_column='segSPRINTpoints')  # Field name made lowercase.
    segkompoints = models.IntegerField(db_column='segKOMpoints')  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegCALC'


class Frstagesegcalcevent(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    evsegref = models.CharField(unique=True, max_length=30)
    frhccode = models.CharField(db_column='FRHCcode', max_length=10)  # Field name made lowercase.
    segpos = models.IntegerField()
    segtime = models.DecimalField(max_digits=12, decimal_places=3)
    segwatts = models.IntegerField()
    segwkg = models.DecimalField(max_digits=10, decimal_places=2)
    segpoints = models.IntegerField()
    segsprintpoints = models.IntegerField(db_column='segSPRINTpoints')  # Field name made lowercase.
    segkompoints = models.IntegerField(db_column='segKOMpoints')  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegCALCevent'


class Frstagesegload(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    segpos = models.IntegerField()
    segtime = models.DecimalField(max_digits=12, decimal_places=3)
    segwatts = models.IntegerField()
    segwkg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'frStageSegLOAD'


class Frstagesegtkom(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegTKOM'


class Frstagesegtkombonus(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegTKOMBONUS'


class Frstagesegtsprint(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegTSPRINT'


class Frstagesegtsprintbonus(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(max_length=10)
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tleague = models.CharField(db_column='TLEAGUE', max_length=50)  # Field name made lowercase.
    rteam = models.CharField(db_column='RTEAM', max_length=30)  # Field name made lowercase.
    frhc = models.CharField(db_column='FRHC', max_length=10)  # Field name made lowercase.
    tsegpoints = models.IntegerField()
    segpos = models.IntegerField(db_column='SEGPOS')  # Field name made lowercase.
    teamsegpts = models.IntegerField(db_column='TEAMSEGPTS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageSegTSPRINTBONUS'


class Frstageavailability(models.Model):
    raid = models.AutoField(db_column='RAid', primary_key=True)  # Field name made lowercase.
    etzteam = models.CharField(db_column='etZTeam', max_length=15)  # Field name made lowercase.
    evteamid = models.CharField(db_column='evTeamID', max_length=50)  # Field name made lowercase.
    razid = models.IntegerField(db_column='RAZid', unique=True)  # Field name made lowercase.
    eteamname = models.CharField(db_column='eTeamname', max_length=50)  # Field name made lowercase.
    seriesref = models.CharField(db_column='seriesRef', max_length=10)  # Field name made lowercase.
    raname = models.CharField(db_column='RAname', max_length=50)  # Field name made lowercase.
    aeventcomment = models.CharField(db_column='aEventcomment', max_length=50)  # Field name made lowercase.
    acommentdate = models.DateField(db_column='aCommentdate')  # Field name made lowercase.
    astage1 = models.CharField(db_column='aStage1', max_length=1)  # Field name made lowercase.
    astage2 = models.CharField(db_column='aStage2', max_length=1)  # Field name made lowercase.
    astage3 = models.CharField(db_column='aStage3', max_length=1)  # Field name made lowercase.
    astage4 = models.CharField(db_column='aStage4', max_length=1)  # Field name made lowercase.
    astage5 = models.CharField(db_column='aStage5', max_length=1)  # Field name made lowercase.
    astage6 = models.CharField(db_column='aStage6', max_length=1)  # Field name made lowercase.
    astage7 = models.CharField(db_column='aStage7', max_length=1)  # Field name made lowercase.
    astage8 = models.CharField(db_column='aStage8', max_length=1)  # Field name made lowercase.
    astage9 = models.CharField(db_column='aStage9', max_length=1)  # Field name made lowercase.
    astage10 = models.CharField(db_column='aStage10', max_length=1)  # Field name made lowercase.
    astage11 = models.CharField(db_column='aStage11', max_length=1)  # Field name made lowercase.
    astage12 = models.CharField(db_column='aStage12', max_length=1)  # Field name made lowercase.
    astage13 = models.CharField(db_column='aStage13', max_length=1)  # Field name made lowercase.
    astage14 = models.CharField(db_column='aStage14', max_length=1)  # Field name made lowercase.
    astage15 = models.CharField(db_column='aStage15', max_length=1)  # Field name made lowercase.
    astage16 = models.CharField(db_column='aStage16', max_length=50)  # Field name made lowercase.
    astage17 = models.CharField(db_column='aStage17', max_length=1)  # Field name made lowercase.
    astage1picked = models.CharField(db_column='aStage1picked', max_length=1)  # Field name made lowercase.
    astage2picked = models.CharField(db_column='aStage2picked', max_length=1)  # Field name made lowercase.
    astage3picked = models.CharField(db_column='aStage3picked', max_length=1)  # Field name made lowercase.
    astage4picked = models.CharField(db_column='aStage4picked', max_length=1)  # Field name made lowercase.
    astage5picked = models.CharField(db_column='aStage5picked', max_length=1)  # Field name made lowercase.
    astage6picked = models.CharField(db_column='aStage6picked', max_length=1)  # Field name made lowercase.
    atidswitch = models.CharField(db_column='aTIDswitch', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frStageavailability'


class Frteststageresultload(models.Model):
    resid = models.AutoField(db_column='RESID', primary_key=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    frhcfinpos = models.IntegerField(db_column='frhcFINpos')  # Field name made lowercase.
    ridertime = models.DecimalField(max_digits=12, decimal_places=3)
    riderwatts = models.IntegerField()
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    riderwkg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'frTESTStageResultLOAD'


class Frteststagesegmentload(models.Model):
    sgid = models.AutoField(db_column='SGID', primary_key=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=15)  # Field name made lowercase.
    segid = models.CharField(db_column='SEGID', max_length=10)  # Field name made lowercase.
    rzid = models.IntegerField(db_column='rZid')  # Field name made lowercase.
    pen = models.CharField(max_length=2)
    segpos = models.IntegerField()
    segtime = models.DecimalField(max_digits=12, decimal_places=3)
    segwatts = models.IntegerField()
    segwkg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'frTESTStageSegmentLOAD'


class Frttupdate(models.Model):
    ttid = models.AutoField(db_column='TTID', primary_key=True)  # Field name made lowercase.
    etid = models.IntegerField(db_column='ETID')  # Field name made lowercase.
    tteam = models.CharField(db_column='Tteam', max_length=20)  # Field name made lowercase.
    ttteamid = models.CharField(db_column='TTteamID', max_length=50)  # Field name made lowercase.
    ttteamname = models.CharField(db_column='TTteamname', max_length=50)  # Field name made lowercase.
    ttteamzone = models.CharField(db_column='TTteamzone', max_length=10)  # Field name made lowercase.
    ttevent1 = models.IntegerField(db_column='TTevent1')  # Field name made lowercase.
    ttevent2 = models.IntegerField(db_column='TTevent2')  # Field name made lowercase.
    ttpen = models.CharField(db_column='TTpen', max_length=1)  # Field name made lowercase.
    ttdelay = models.CharField(db_column='TTdelay', max_length=10)  # Field name made lowercase.
    ttref = models.CharField(db_column='TTref', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frTTupdate'


class Frtourraceteam(models.Model):
    trtid = models.AutoField(db_column='TRTID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(db_column='SERIESREF', max_length=10)  # Field name made lowercase.
    clubref = models.CharField(db_column='CLUBREF', max_length=15)  # Field name made lowercase.
    teamref = models.CharField(db_column='TEAMREF', max_length=2)  # Field name made lowercase.
    tourteamid = models.CharField(db_column='TOURTEAMID', max_length=30)  # Field name made lowercase.
    teamname = models.CharField(db_column='TEAMNAME', max_length=30)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=20)  # Field name made lowercase.
    lastupdated = models.DateField(db_column='LASTUPDATED')  # Field name made lowercase.

    class Meta:
        
        db_table = 'frTourraceteam'


class Frtourteamcombine(models.Model):
    ttid = models.AutoField(db_column='TTID', primary_key=True)  # Field name made lowercase.
    seriesref = models.CharField(db_column='SERIESREF', max_length=10)  # Field name made lowercase.
    teamfrom = models.CharField(db_column='TEAMFROM', max_length=20)  # Field name made lowercase.
    teamto = models.CharField(db_column='TEAMTO', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'frTourteamcombine'


class Frxdataupdate(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    zid = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    cat = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    np = models.IntegerField()
    frhc = models.CharField(max_length=3)
    wkg = models.DecimalField(max_digits=6, decimal_places=2)
    action = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'frXdataupdate'


class Fraleaguestandings(models.Model):
    lrid = models.AutoField(db_column='LRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=50)  # Field name made lowercase.
    leagueteamref = models.CharField(db_column='leagueTeamref', unique=True, max_length=50)  # Field name made lowercase.
    leagueteamid = models.CharField(db_column='leagueTeamID', max_length=50)  # Field name made lowercase.
    leaguerno = models.IntegerField(db_column='leagueRno')  # Field name made lowercase.
    leagueteamtsegfol = models.IntegerField(db_column='leagueTeamTSEGFOL')  # Field name made lowercase.
    leagueteamtsegfts = models.IntegerField(db_column='leagueTeamTSEGFTS')  # Field name made lowercase.
    leagueteamtfin = models.IntegerField(db_column='leagueTeamTFIN')  # Field name made lowercase.
    leagueteamsfpts = models.IntegerField(db_column='leagueTeamSFpts')  # Field name made lowercase.
    leagueteamlpts = models.IntegerField(db_column='leagueTeamLPTS')  # Field name made lowercase.
    leaguerecalcdate = models.DateField(db_column='leagueRecalcdate')  # Field name made lowercase.
    leaguetotaltpen = models.IntegerField(db_column='leaguetotalTPEN')  # Field name made lowercase.
    leagueteamname = models.CharField(db_column='leagueteamName', max_length=30)  # Field name made lowercase.
    eventbonuspts = models.IntegerField(db_column='eventBonuspts')  # Field name made lowercase.
    eventrbonus = models.DecimalField(db_column='eventRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    tsprintbonus = models.IntegerField(db_column='tSPRINTbonus')  # Field name made lowercase.
    tkombonus = models.IntegerField(db_column='tKOMbonus')  # Field name made lowercase.
    tgcbonus = models.IntegerField(db_column='tGCbonus')  # Field name made lowercase.

    class Meta:
        
        db_table = 'fraLeagueStandings'


class Frariderstandings(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=20)  # Field name made lowercase.
    teamriderref = models.CharField(db_column='teamriderRef', unique=True, max_length=40)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=20)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    recalcdate = models.DateField(db_column='recalcDate')  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    totalrpen = models.IntegerField(db_column='totalRPEN')  # Field name made lowercase.
    riderteamname = models.CharField(db_column='riderteamName', max_length=30)  # Field name made lowercase.
    totalkom = models.IntegerField(db_column='totalKOM')  # Field name made lowercase.
    totalsprint = models.IntegerField(db_column='totalSPRINT')  # Field name made lowercase.
    totalrbonus = models.DecimalField(db_column='totalRbonus', max_digits=7, decimal_places=2)  # Field name made lowercase.
    totalgctime = models.DecimalField(db_column='totalGCtime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=20)  # Field name made lowercase.
    gcracect = models.IntegerField(db_column='GCracect')  # Field name made lowercase.
    riderfrhc = models.CharField(db_column='riderFRHC', max_length=10)  # Field name made lowercase.
    lzone = models.CharField(db_column='lZone', max_length=10)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    gctotaltime = models.CharField(db_column='GCtotaltime', max_length=15)  # Field name made lowercase.
    racersort = models.CharField(db_column='raceRSORT', max_length=20)  # Field name made lowercase.

    class Meta:
        
        db_table = 'fraRiderStandings'


class Frariderstatsindividual(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    segmenttotalfol = models.IntegerField(db_column='segmentTotalFOL')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totaltpt = models.IntegerField(db_column='totalTPT')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    calcdate = models.DateField()
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    exreason = models.CharField(db_column='exReason', max_length=20)  # Field name made lowercase.
    resultselected = models.CharField(db_column='resultSelected', max_length=1)  # Field name made lowercase.
    exreasoncode = models.CharField(db_column='exReasoncode', max_length=10)  # Field name made lowercase.
    timefull = models.CharField(db_column='timeFull', max_length=30)  # Field name made lowercase.
    timevalue = models.CharField(db_column='timeValue', max_length=20)  # Field name made lowercase.
    timehr = models.CharField(db_column='timeHR', max_length=2)  # Field name made lowercase.
    timemin = models.CharField(db_column='timeMIN', max_length=2)  # Field name made lowercase.
    timesec = models.CharField(db_column='timeSEC', max_length=6)  # Field name made lowercase.
    totalpen = models.IntegerField(db_column='totalPen')  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30)  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMpoints')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTpoints')  # Field name made lowercase.
    tbonus = models.IntegerField(db_column='tBonus')  # Field name made lowercase.
    rbonus = models.DecimalField(db_column='rBonus', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rmply = models.DecimalField(db_column='rMply', max_digits=5, decimal_places=2)  # Field name made lowercase.
    frrgctime = models.DecimalField(db_column='frrGCtime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    gcracetbonus = models.IntegerField(db_column='GCracetbonus')  # Field name made lowercase.
    gctracetbonus = models.IntegerField(db_column='GCtracetbonus')  # Field name made lowercase.
    gcttime = models.DecimalField(db_column='GCttime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=30)  # Field name made lowercase.
    racefrhc = models.CharField(db_column='raceFRHC', max_length=5)  # Field name made lowercase.
    racefrhcpos = models.CharField(db_column='raceFRHCpos', max_length=10)  # Field name made lowercase.
    racezone = models.CharField(db_column='raceZone', max_length=10)  # Field name made lowercase.
    racersort = models.CharField(db_column='raceRSORT', max_length=20)  # Field name made lowercase.
    zeventid = models.CharField(db_column='zEventid', max_length=15)  # Field name made lowercase.
    riderwatts = models.IntegerField(db_column='riderWatts')  # Field name made lowercase.
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.

    class Meta:
        
        db_table = 'fraRiderStatsindividual'


class Frasegmentresults(models.Model):
    segrid = models.AutoField(db_column='SEGRID', primary_key=True)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    segref = models.CharField(db_column='SEGref', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    ridertime = models.DecimalField(db_column='riderTime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    segwatts = models.IntegerField(db_column='SEGwatts')  # Field name made lowercase.
    segwkg = models.CharField(db_column='SEGwkg', max_length=10)  # Field name made lowercase.
    segtimedisp = models.CharField(db_column='SEGtimedisp', max_length=15)  # Field name made lowercase.
    segeffort = models.CharField(db_column='SEGeffort', max_length=30)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=20)  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=40)  # Field name made lowercase.
    lzone = models.CharField(db_column='LZONE', max_length=10)  # Field name made lowercase.
    racerank = models.CharField(db_column='raceRANK', max_length=15)  # Field name made lowercase.
    segpos = models.IntegerField(db_column='SEGpos')  # Field name made lowercase.
    segpoints = models.IntegerField(db_column='SEGpoints')  # Field name made lowercase.
    segzpref = models.CharField(db_column='SEGZPREF', max_length=10)  # Field name made lowercase.

    class Meta:
        
        db_table = 'fraSegmentResults'


class Frdatachanges(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    zid = models.IntegerField(db_column='ZID')  # Field name made lowercase.

    class Meta:
        db_table = 'frdatachanges'


class Seriestimezone(models.Model):
    stzid = models.AutoField(db_column='STZID', primary_key=True)  # Field name made lowercase.
    tzcode = models.CharField(db_column='tZcode', unique=True, max_length=10)  # Field name made lowercase.
    tzname = models.CharField(db_column='tZname', max_length=20)  # Field name made lowercase.
    tzactive = models.CharField(db_column='tZactive', max_length=1)  # Field name made lowercase.
    tzref = models.CharField(db_column='tZref', max_length=5)  # Field name made lowercase.

    class Meta:
        db_table = 'seriesTimezone'


class Xfrriderstatsflash(models.Model):
    rsid = models.AutoField(db_column='RSID', primary_key=True)  # Field name made lowercase.
    eventriderref = models.CharField(db_column='eventriderRef', max_length=50)  # Field name made lowercase.
    leagueid = models.CharField(db_column='leagueID', max_length=25)  # Field name made lowercase.
    raceref = models.CharField(db_column='raceRef', max_length=50)  # Field name made lowercase.
    leaguess = models.CharField(db_column='leagueSS', max_length=10)  # Field name made lowercase.
    teamref = models.CharField(db_column='teamRef', max_length=50)  # Field name made lowercase.
    rteamg = models.CharField(db_column='rTeamg', max_length=20)  # Field name made lowercase.
    riderid = models.IntegerField(db_column='riderID')  # Field name made lowercase.
    raceno = models.IntegerField(db_column='raceNo')  # Field name made lowercase.
    tourtype = models.CharField(db_column='tourType', max_length=1)  # Field name made lowercase.
    racedate = models.DateField(db_column='raceDate')  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='finishTotal')  # Field name made lowercase.
    segmenttotalfts = models.IntegerField(db_column='segmentTotalFTS')  # Field name made lowercase.
    totalsf = models.IntegerField(db_column='totalSF')  # Field name made lowercase.
    totaltpt = models.IntegerField(db_column='totalTPT')  # Field name made lowercase.
    totalrpt = models.DecimalField(db_column='totalRPT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    calcdate = models.DateField()
    riderwatts = models.IntegerField(db_column='riderWatts')  # Field name made lowercase.
    rider20minwkg = models.DecimalField(max_digits=5, decimal_places=2)
    ridernpwatts = models.IntegerField(db_column='riderNPwatts')  # Field name made lowercase.
    exreason = models.CharField(db_column='exReason', max_length=20)  # Field name made lowercase.
    resultselected = models.CharField(db_column='resultSelected', max_length=1)  # Field name made lowercase.
    exreasoncode = models.CharField(db_column='exReasoncode', max_length=10)  # Field name made lowercase.
    totalpen = models.IntegerField(db_column='totalPen')  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30)  # Field name made lowercase.
    kompoints = models.IntegerField(db_column='KOMpoints')  # Field name made lowercase.
    sprintpoints = models.IntegerField(db_column='SPRINTpoints')  # Field name made lowercase.
    tbonus = models.IntegerField(db_column='tBonus')  # Field name made lowercase.
    rbonus = models.DecimalField(db_column='rBonus', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rmply = models.DecimalField(db_column='rMply', max_digits=5, decimal_places=2)  # Field name made lowercase.
    gcttime = models.DecimalField(db_column='GCttime', max_digits=15, decimal_places=3)  # Field name made lowercase.
    gctimenote = models.CharField(db_column='GCtimenote', max_length=30)  # Field name made lowercase.
    racefrhc = models.CharField(db_column='raceFRHC', max_length=5)  # Field name made lowercase.
    racefrhcpos = models.IntegerField(db_column='raceFRHCpos')  # Field name made lowercase.
    zeventid = models.CharField(db_column='zEventid', max_length=15)  # Field name made lowercase.
    rformat = models.CharField(db_column='RFORMAT', max_length=10)  # Field name made lowercase.
    rgender = models.CharField(db_column='RGENDER', max_length=1)  # Field name made lowercase.
    tttime = models.DecimalField(db_column='TTTIME', max_digits=10, decimal_places=3)  # Field name made lowercase.
    tttpos = models.IntegerField(db_column='TTTPOS')  # Field name made lowercase.
    teamttpos = models.IntegerField(db_column='teamTTPOS')  # Field name made lowercase.

    class Meta:
        db_table = 'xfrRiderSTATSflash'
