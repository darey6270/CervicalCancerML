from django.views.generic import TemplateView
from django.shortcuts import render
import joblib
from sklearn.preprocessing import LabelEncoder
from .forms import PredictForm
import numpy as np


class AboutWebsite(TemplateView):
    template_name = "CervicalCancerApp/about.html"


class ContactWebsite(TemplateView):
    template_name = "CervicalCancerApp/contact.html"


class PredictWebsite(TemplateView):
    template_name = "CervicalCancerApp/result.html"


class ServiceWebsite(TemplateView):
    template_name = "CervicalCancerApp/service.html"


class HomeWebsite(TemplateView):
    template_name = "CervicalCancerApp/index.html"


def ServiceWebsiteView(request):
    prediction_text = ''
    predictForm = PredictForm()
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['Age']
            nsp = form.cleaned_data['Number_of_sexual_partners']
            fsi = form.cleaned_data['First_sexual_intercourse']
            nop = form.cleaned_data['num_of_pregnancies']
            smokes = form.cleaned_data['Smokes']
            smokes_years = form.cleaned_data['Smokes_years']
            smokes_packs = form.cleaned_data['Smokes_packs']
            hc = form.cleaned_data['Hormonal_contraceptives']
            hcy = form.cleaned_data['Hormonal_contraceptives_year']
            model = joblib.load(open('CervicalCancerApp/randomForestClassifier.pkl', 'rb'))
            pred_test = np.array(
                [age, nsp, fsi, nop, smokes, smokes_years, smokes_packs, hc, hcy, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                 1])
            result = model.predict(pred_test.reshape(1, -1))
            if result[0] == 1:
                prediction_text = "Cervical cancer detected"
            else:
                prediction_text = "Cervical cancer not detected "

            return render(request, "CervicalCancerApp/result.html",
                          {"prediction_text": prediction_text})
        else:
            print(form.errors)
    else:
        predictForm = PredictForm()
    return render(request, "CervicalCancerApp/service.html",
                  {"predictForm": predictForm})
