from django.shortcuts import render

# Create your views here.
def index(request):
    peliculas = [
        {
            'titulo':'AVATAR 2',
            'imagen':'https://cloudfront-us-east-1.images.arcpublishing.com/gruponacion/DFFLHUVNEJGYFESCBUN74Z3UGQ.jpg'
        },
        {
            'titulo':'MARIO BROSS',
            'imagen':'https://i.blogs.es/b9f542/1500x500-5-/1366_521.jpeg'
        },
        {
            'titulo':'SHAZAM 2',
            'imagen':'https://i.blogs.es/6a33c2/shazam-2-poster-resenaa/1366_2000.jpeg'
        }
    ]
    
    context = {
        'peliculas':peliculas
    }
    
    return render(request,'index.html',context)