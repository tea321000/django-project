from django.http import HttpResponse
from django.template import loader,Context
from music.models import Musician,RecordCompany,Album,Music,User,PersonalRecord

def print_all(request):
    t=loader.get_template("print_all.html")
    Musicianlist=Musician.objects.all()
    RecordCompanylist=RecordCompany.objects.all()
    Albumlist=Album.objects.all()
    Musiclist=Music.objects.all()
    Userlist=User.objects.all()
    PersonalRecordlist=PersonalRecord.objects.all()
    c=Context({"Musicianlist":Musicianlist,
                "RecordCompanylist":RecordCompanylist,
                "Albumlist":Albumlist,
                "Musiclist":Musiclist})
    return HttpResponse(t.render(c))
