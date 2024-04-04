from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Create a new ContactMessage object and save it to the database
        contact_message = ContactMessage.objects.create(name=name, phone_number=phone_number, email=email, message=message)
        contact_message.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('contact_page')  # Redirect to a thank you page or any other page
    else:
        # Handle GET request (if any)
        pass
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
    

