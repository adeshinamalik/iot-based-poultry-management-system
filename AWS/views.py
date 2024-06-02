from django.shortcuts import render, redirect
import pyrebase
from datetime import datetime
from autopoultryweb.models import EggCollection, Feeding, WasteCollection, Water

# username: admin
# password: funaabadmin

firebaseConfig = {
    "apiKey": "AIzaSyDOCyQf_hfr3g-miCj4e60KY2KMsupfT_k",
    "authDomain": "automatedpoultry-dce6b.firebaseapp.com",
    "databaseURL": "https://automatedpoultry-dce6b-default-rtdb.firebaseio.com",
    "projectId": "automatedpoultry-dce6b",
    "storageBucket": "automatedpoultry-dce6b.appspot.com",
    "messagingSenderId": "74098175761",
    "appId": "1:74098175761:web:297ad0b6b5308e5ec726b0",
    "measurementId": "G-3MFRT11TPJ"
}

firebaseSetup = pyrebase.initialize_app(firebaseConfig)
authentication = firebaseSetup.auth()
poultryDB = firebaseSetup.database()

# dateFormat = '%Y-%m-%d %H:%M:%S.%f%z'   # e.g date_str = 2023-09-17 03:39:54.273594+00:00
# dateFormat = '%Y-%m-%d %H:%M:%S%z'   #e.g date_str = 2023-09-19 12:00:00+00:00
dateFormat = '%Y-%m-%d %H:%M:%S'  # e.g  date_str = 2023-09-19 12:00:00


# Create your views here.


def index(request):
    # Fetch data from Firebase
    # Data = poultryDB.child('Poultry').child('Egg').child('EggWeight').get().val()  # returns value of a key
    EggDataFirebase = poultryDB.child('Poultry').child('Egg').get().val()  # This returns the whole Egg dictionary
    WasteDataFirebase = poultryDB.child('Poultry').child('Waste').get().val()
    FeedingDataFirebase = poultryDB.child('Poultry').child('Feeding').get().val()
    WaterDataFirebase = poultryDB.child('Poultry').child('Water').get().val()


    #
    # Note when you fetch Date Data from firebase, you need to convert the time from string to Datetime

    EggDataFirebase["StartEggDateTime"] = datetime.strptime(str(EggDataFirebase["StartEggDateTime"]), dateFormat)
    EggDataFirebase["StopEggDateTime"] = datetime.strptime(str(EggDataFirebase["StopEggDateTime"]), dateFormat)
    EggDataFirebase["NextEggDateTime"] = datetime.strptime(str(EggDataFirebase["NextEggDateTime"]), dateFormat)

    FeedingDataFirebase["StartFeedingDateTime"] = datetime.strptime(str(FeedingDataFirebase["StartFeedingDateTime"]),
                                                                    dateFormat)
    FeedingDataFirebase["StopFeedingDateTime"] = datetime.strptime(str(FeedingDataFirebase["StopFeedingDateTime"]),
                                                                   dateFormat)
    FeedingDataFirebase["NextFeedingDateTime"] = datetime.strptime(str(FeedingDataFirebase["NextFeedingDateTime"]),
                                                                   dateFormat)

    WasteDataFirebase["StartWasteDateTime"] = datetime.strptime(str(WasteDataFirebase["StartWasteDateTime"]),
                                                                dateFormat)
    WasteDataFirebase["StopWasteDateTime"] = datetime.strptime(str(WasteDataFirebase["StopWasteDateTime"]), dateFormat)
    WasteDataFirebase["NextWasteDateTime"] = datetime.strptime(str(WasteDataFirebase["NextWasteDateTime"]), dateFormat)

    WaterDataFirebase["StartRefillDateTime"] = datetime.strptime(str(WaterDataFirebase["StartRefillDateTime"]),
                                                                 dateFormat)
    WaterDataFirebase["StopRefillDateTime"] = datetime.strptime(str(WaterDataFirebase["StopRefillDateTime"]),
                                                                dateFormat)

    # Fetch Data from DB sqlite
    EggDataDBSqlite = EggCollection.objects.last()
    FeedingDataDBSqlite = Feeding.objects.last()
    WasteDataDBSqlite = WasteCollection.objects.last()
    WaterDataDBSqlite = Water.objects.last()
    # date_obj = datetime.strptime(str(FeedingData.NextFeedingDateTime), dateFormat)

    if (EggDataFirebase["StopEggDateTime"] is None or EggDataDBSqlite is None) or EggDataDBSqlite.StopEggDateTime != EggDataFirebase[
        "StopEggDateTime"]:
        newEggDataDBSqlite = EggCollection(StartEggDateTime=EggDataFirebase["StartEggDateTime"],
                                           StopEggDateTime=EggDataFirebase["StopEggDateTime"],
                                           NextEggDateTime=EggDataFirebase["NextEggDateTime"],
                                           EggDuration=EggDataFirebase["EggDuration"],
                                           EggQuantity=EggDataFirebase["EggQuantity"],
                                           EggWeight=EggDataFirebase["EggWeight"],
                                           EggStatus=EggDataFirebase["EggStatus"],
                                           EggSystemFault=EggDataFirebase["EggSystemFault"])

        newEggDataDBSqlite.save()

    if (FeedingDataFirebase["StopFeedingDateTime"] is None or FeedingDataDBSqlite is None) or FeedingDataDBSqlite.StopFeedingDateTime != \
            FeedingDataFirebase["StopFeedingDateTime"]:
        newFeedingDataDBSqlite = Feeding(StartFeedingDateTime=FeedingDataFirebase["StartFeedingDateTime"],
                                         StopFeedingDateTime=FeedingDataFirebase["StopFeedingDateTime"],
                                         NextFeedingDateTime=FeedingDataFirebase["NextFeedingDateTime"],
                                         FeedWeight=FeedingDataFirebase["FeedWeight"],
                                         FeedingDuration=FeedingDataFirebase["FeedingDuration"],
                                         FeedingStatus=FeedingDataFirebase["FeedingStatus"],
                                         FeedingSystemFault=FeedingDataFirebase["FeedingSystemFault"])

        newFeedingDataDBSqlite.save()

    if (WaterDataFirebase["StopRefillDateTime"] is None or WaterDataDBSqlite is None) or WaterDataDBSqlite.StopRefillDateTime != WaterDataFirebase[
        "StopRefillDateTime"]:
        newWaterDataDBSqlite = Water(StartRefillDateTime=WaterDataFirebase["StartRefillDateTime"],
                                     StopRefillDateTime=WaterDataFirebase["StopRefillDateTime"],
                                     RefillDuration=WaterDataFirebase["RefillDuration"],
                                     RefillStatus=WaterDataFirebase["RefillStatus"],
                                     WaterSystemFault=WaterDataFirebase["WaterSystemFault"])
        newWaterDataDBSqlite.save()

    if (WasteDataFirebase["StopWasteDateTime"] is None or WasteDataDBSqlite is None) or WasteDataDBSqlite.StopWasteDateTime != WasteDataFirebase["StopWasteDateTime"]:
        newWasteDataDBSqlite = WasteCollection(StartWasteDateTime=WasteDataFirebase["StartWasteDateTime"],
                                               StopWasteDateTime=WasteDataFirebase["StopWasteDateTime"],
                                               NextWasteDateTime=WasteDataFirebase["NextWasteDateTime"],
                                               WasteDuration=WasteDataFirebase["WasteDuration"],
                                               WasteStatus=WasteDataFirebase["WasteStatus"],
                                               WasteSystemFault=WasteDataFirebase["WasteSystemFault"])
        newWasteDataDBSqlite.save()
    '''
    if request.method == 'POST':
        startFeeding = request.POST.get('startFeeding', '0')
        stopFeeding = request.POST.get('stopFeeding', '0')
	startEgg = request.POST.get('startEgg', '0')
	stopEgg = request.POST.get('stopEgg', '0')
	startWaste = request.POST.get('startWaste', '0')
        stopWaste = request.POST.get('stopWaste', '0')
        if startFeeding == '1':
            FeedingStartButton = 1
        else:
            FeedingStartButton = 0
	if startEgg == '1':
	    EggStartButton = 1
	else:
	    EggStartButton = 0
        if startWaste == '1':
            WasteStartButton = 1
        else:
            WasteStartButton = 0
	update_feeding_data = {"FeedingStartButton": FeedingStartButton}
	update_egg_data = {"EggStartButton": EggStartButton}
	update_waste_data = {"WasteStartButton": WasteStartButton}
	poultryDB.child('Poultry/Feeding').update(update_feeding_data)
        poultryDB.child('Poultry/Egg').update(update_egg_data)
        poultryDB.child('Poultry/Waste').update(update_waste_data)
	#print(startFeeding)
        #print(stopFeeding)
        return redirect('/home')
      '''
    return render(request, "index.html", context={'currentTime':datetime.now(), 'EggData': EggDataFirebase,
                                                  'FeedingData': FeedingDataFirebase,'WasteData': WasteDataFirebase,
                                                  'WaterData': WaterDataFirebase})
