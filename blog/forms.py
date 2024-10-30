from django import forms


class Add_New(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))


class Edit_Article(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    def custom(self, obj):
        if "Heading" in obj:
            self.initial['title'] = obj["Heading"]
            self.initial['content'] = obj["Content"]