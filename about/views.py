from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    """
    Renders the About page and processes the collaboration form.
    """
    about = About.objects.all().order_by('-updated_on').first()

    # Create an instance of the CollaborateForm
    collaborate_form = CollaborateForm()

    # If the form has been submitted and is valid, process the form
    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            # Save the form data or send an email, etc.
            collaborate_form.save()  # Example: Saving form data if needed
            return redirect('success')  # Redirect to a success page after submission

    # Pass the form into the context to render in the template
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,  # Add the form to the context
        },
    )
