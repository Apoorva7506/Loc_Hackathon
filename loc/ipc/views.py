from django.shortcuts import render
from django.http import HttpResponse
from . import templates
# Create your views here.

def ipc(request):
    found=False
    if request.method=="POST":
        search = request.POST['word']
        found=True
        code = {
        300:"Except in the cases hereinafter excepted, culpable homicide is murder, if the act by which the death is caused is done with the intention of causing death, or—2ndly.—If it is done with the intention of causing such bodily injury as the offender knows to be likely to cause the death of the person to whom the harm is caused, or—3rdly.—If it is done with the intention of causing bodily injury to any person and the bodily injury intended to be inflicted is sufficient in the ordinary course of nature to cause death, or—4thly.—If the person committing the act knows that it is so imminently dangerous that it must, in all probability, cause death, or such bodily injury as is likely to cause death, and commits such act without any excuse for incurring the risk of causing death or such injury as aforesaid.",
        302:"Whoever commits murder shall be punished with death or 1 [imprisonment for life], and shall also be liable to fine",
        303:"Whoever, being under sentence of 1 [imprisonment for life], commits murder, shall be punished with death.",
        378:"Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.Explanation 1.—A thing so long as it is attached to the earth, not being movable property, is not the subject of theft; but it becomes capable of being the subject of theft as soon as it is severed from the earth.Explanation 2.—A moving effected by the same act which effects the severance may be a theft.Explanation 3.—A person is said to cause a thing to move by removing an obstacle which prevented it from moving or by separating it from any other thing, as well as by actually moving it.Explanation 4.—A person, who by any means causes an animal to move, is said to move that animal, and to move everything which, in consequence of the motion so caused, is moved by that animal.Explanation 5.—The consent mentioned in the definition may be express or implied, and may be given either by the person in possession, or by any person having for that purpose authority either express or implied.",
        379:"Whoever commits theft shall be punished with imprisonment of either description for a term which may extend to three years, or with fine, or with both.",
        380:"Whoever commits theft in any building, tent or vessel, which building, tent or vessel is used as a human dwelling, or used for the custody of property, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.",
        381:"Whoever, being a clerk or servant, or being employed in the capacity of a clerk or servant, commits theft in respect of any property in the possession of his master or employer, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.",
        382:"Whoever commits theft, having made preparation for causing death, or hurt, or restraint, or fear of death, or of hurt, or of restraint, to any person, in order to the committing of such theft, or in order to the effecting of his escape after the committing of such theft, or in order to the retaining of property taken by such theft, shall be punished with rigorous imprisonment for a term which may extend to ten years, and shall also be liable to fine."
        }
        res = [key for key, val in code.items() if search in val] 
        d={}
        for i in res:
            d[i]=code[i]
        return render(request,'ipc/searching.html',{'d':d,'found':found})
    else:
        return render(request,'ipc/searching.html')
        #return HttpResponse("It works")