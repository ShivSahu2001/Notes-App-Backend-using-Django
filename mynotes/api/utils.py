from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was Deleted Successfully")

def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    # To Convert the python Objects into Json data we use Serializer
    # many = True --> means to serialize multiple objects
    serializer = NoteSerializer(notes, many=True) # here serializer is an object
    return Response(serializer.data)

def createNote(request):
     data = request.data
     note = Note.objects.create(
        body = data['body']
        )
     serializer = NoteSerializer(note, many=False)
     return serializer.data