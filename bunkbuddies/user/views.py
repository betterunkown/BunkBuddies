# In your views.py file

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage
from django.http import JsonResponse

def contact_submit(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']

            phone_number = form.cleaned_data['phone_number']

            email = form.cleaned_data['email']

            message = form.cleaned_data['message']

            try:

                contact_message = ContactMessage.objects.create(name=name, phone_number=phone_number, email=email, message=message)

                contact_message.save()

                messages.success(request, 'Your message has been sent. Thank you!')

                return redirect('contact_page')

            except Exception as e:

                messages.error(request, f'Error sending message: {e}')

        else:

            messages.error(request, 'Error in form data. Please check your input and try again.')

    else:

        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def your_view(request):
    swiper_config = {
        "loop": True,
        "speed": 600,
        "autoplay": {
            "delay": 5000
        },
        "slidesPerView": "auto",
        "pagination": {
            "el": ".swiper-pagination",
            "type": "bullets",
            "clickable": True
        }
    }
    return render(request, 'index.html', {'swiper_config': swiper_config})

    

