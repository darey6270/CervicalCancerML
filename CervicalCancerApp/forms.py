from django import forms


class PredictForm(forms.Form):
    Age = forms.IntegerField()
    Number_of_sexual_partners = forms.IntegerField()
    First_sexual_intercourse = forms.IntegerField()
    num_of_pregnancies = forms.IntegerField()
    Smokes = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')])
    Smokes_years = forms.IntegerField()
    Smokes_packs = forms.IntegerField()
    Hormonal_contraceptives = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')])
    Hormonal_contraceptives_year = forms.IntegerField()

