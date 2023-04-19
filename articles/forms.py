from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    # VALIDATION METHODS > Clean data
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in use.")
        return data
        # raise error must be after all validations
        # raise is global form error
        # self.add_error is a field error (field, "error text")



# class ArticleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()



    # use for valid some specific field
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('This title is taken')
    #     return title
    

    # use for valid all form
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     content = cleaned_data.get('content')
    #     if 'office' in content:
    #         self.add_error('content', 'office is not allowed') 
    #         # raise forms.ValidationError('office is not allowed')
    #     if title.lower().strip() == 'the office':
    #         # self.add_error('title', 'This title is taken')
    #         raise forms.ValidationError('This title is taken') 
        

    #     return cleaned_data