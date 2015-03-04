from django.shortcuts import render
def algo(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request,'loucura.html',context_dict)
# Create your views here.
