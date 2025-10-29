from django.shortcuts import render
from .forms import MovieForm

def form(request):
    # Siempre inicializamos la variable form
    movie_form = MovieForm(request.POST or None)

    if request.method == "POST":
        if movie_form.is_valid():
            movie_form.save()
            # Renderizamos el mismo formulario vacío y un mensaje de éxito
            movie_form = MovieForm()  # Reiniciamos el formulario
            return render(request, "cinemaapp/form.html", {"form": movie_form, "success": True})

    # Para GET o si el POST no es válido, mostramos el formulario con errores
    return render(request, "cinemaapp/form.html", {"form": movie_form})
