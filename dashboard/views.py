from django.shortcuts import render, redirect
import pyrebase
from django.http import HttpResponse

# Create your views here
firebaseConfig = {
  "apiKey": "AIzaSyCAoQvzuc9s5hxtnqg8JDqzYBvJ-6wh0lk",
  "authDomain": "car-booking-app-e465d.firebaseapp.com",
  "databaseURL": "https://car-booking-app-e465d-default-rtdb.firebaseio.com",
  "projectId": "car-booking-app-e465d",
  "storageBucket": "car-booking-app-e465d.appspot.com",
  "messagingSenderId": "620340729907",
  "appId": "1:620340729907:web:d1e123fad8d42b6899eb46"
}
myapp=pyrebase.initialize_app(firebaseConfig)
db = myapp.database()
myauth=myapp.auth()



def index(request):
    return render(request, "index.html")

def users(request):
    sharedRide = db.child("RideData").get()
    allData = []
    activeNumber = []
    for i in sharedRide.each():
        allData.append(i.val())

    for i in sharedRide.each():
        if i.val()['accept']=="false":
            activeNumber.append(i.val())

    # return render(request, "User.html", {"result": results})
    return render(request, "User.html",
                  {
                      "dataList": allData,
                      "activeNumber": len(activeNumber),
                      "totaluser": len(allData)
                  }
                  )


def manAndVan(request):
    sharedRide = db.child("ManAndVan").get()
    allData = []
    activeNumber = []
    for i in sharedRide.each():
        allData.append(i.val())

    for i in sharedRide.each():
        if i.val()['accept']=="false":
            activeNumber.append(i.val())

    # return render(request, "User.html", {"result": results})
    return render(request, "ManAndVan.html",
                  {
                      "dataList": allData,
                      "activeNumber": len(activeNumber),
                      "totaluser": len(allData)
                  }
                  )

def Coach(request):
    sharedRide = db.child("Coach").get()
    allData = []
    activeNumber = []
    for i in sharedRide.each():
        allData.append(i.val())

    for i in sharedRide.each():
        if i.val()['accept']=="false":
            activeNumber.append(i.val())

    return render(request, "Coach.html",
                  {
                      "dataList": allData,
                      "activeNumber": len(activeNumber),
                      "totaluser": len(allData)
                  }
                  )


def WasteManagement(request):
    sharedRide = db.child("WasteManagement").get()
    allData = []
    activeNumber = []
    for i in sharedRide.each():
        allData.append(i.val())

    for i in sharedRide.each():
        if i.val()['accept']=="false":
            activeNumber.append(i.val())

    # return render(request, "User.html", {"result": results})
    return render(request, "WasteManagement.html",
                  {
                      "dataList": allData,
                      "activeNumber": len(activeNumber),
                      "totaluser": len(allData)
                  }
                  )


def Courier(request):
    sharedRide = db.child("Courier").get()
    allData = []
    activeNumber = []
    for i in sharedRide.each():
        allData.append(i.val())

    for i in sharedRide.each():
        if i.val()['accept']=="false":
            activeNumber.append(i.val())

    # return render(request, "User.html", {"result": results})
    return render(request, "Courier.html",
                  {
                      "dataList": allData,
                      "activeNumber": len(activeNumber),
                      "totaluser": len(allData)
                  }
                  )


def document(request):
    return render(request, "Document.html")

def addDoc(request):
    return render(request, "AddDoc.html")

def viewDoc(request):
    return render(request, "viewDoc.html")

def acceptCus(request, name, pagename):

    data = db.child(pagename).get()
    for i in data.each():
        if i.val()['name']==str(name):
            mykey = i.key()
            db.child(pagename).child(mykey).update({"accept": "true"})

    if pagename=="RideData":
        return redirect("users")
    elif pagename=="ManAndVan" :
        return redirect("manAndVan")
    else:
        return redirect(pagename)