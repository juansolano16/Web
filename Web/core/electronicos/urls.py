from django.urls import  path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from core.electronicos.views import listRide, dowloadElec, downloadElect

app_name = 'electronicos'

urlpatterns = [
    path('rideComprobantes/', listRide.as_view(), name='rideComprobantes'),

    path('dowloadElectronicos/', downloadElect.as_view(), name='dowloadElec'),
]