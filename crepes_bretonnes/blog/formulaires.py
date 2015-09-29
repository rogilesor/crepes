from django import forms
from blog.models import Article


class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="Votre adresse mail")
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé", required=False)

	# def clean_message(self):
	# 	message = self.cleaned_data['message']
	# 	if "pizza" in message:
	# 		raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
	# 	return message

	def clean(self):
		cleaned_data = super(ContactForm,self).clean()
		sujet = cleaned_data.get('sujet')
		message = cleaned_data.get('message')

		if sujet and message :
			if "pizza" in sujet and "pizza" in message:
				msg = "Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message"
				self.add_error("message",msg)
				raise forms.ValidationError("Vous parlez trop des pizzas")
		return cleaned_data

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields=(
					'titre',
					'slug', 
					'auteur',
					'contenu',
					'categorie',
				)

class NouveauContactForm(forms.Form):
	nom = forms.CharField()
	adresse = forms.CharField(widget=forms.Textarea)
	photo = forms.ImageField()

