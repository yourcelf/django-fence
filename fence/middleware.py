from django.conf import settings
from django.shortcuts import render, redirect
from django import forms

class FenceTokenForm(forms.Form):
    magic_word = forms.CharField()

class Fence(object):
    def process_request(self, request):
        magic_word = getattr(settings, 'FENCE_TOKEN', None)

        if request.session.get('fence_token', None) == magic_word:
            return self.you_may_pass(request)

        form = FenceTokenForm(request.POST or None)
        if 'fence_next' not in request.session:
            request.session['fence_next'] = request.path

        if form.is_valid():
            if form.cleaned_data["magic_word"] == magic_word:
                request.session['fence_token'] = magic_word
                return self.you_may_pass(request)

        return render(request, "fence/say_the_magic_word.html", {
            'form': form
        })

    def you_may_pass(self, request):
        nextr = request.session.pop('fence_next', None)
        if nextr:
            return redirect(nextr)
        return None
