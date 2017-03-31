from django.http import HttpResponse
from Offer.functions import get_all_user_offers
from django.core import serializers

def offers_home(request):
    if request.method == 'GET':
      user = request.GET.get('pk')
      offers = get_all_user_offers(user)
      return HttpResponse(serializers.serialize("json",offers))
  