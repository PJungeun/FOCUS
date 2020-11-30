from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect

app_name = 'free'

def protected_file(request, path, document_root=None):
    messages.error(request, "접근 불가")
    return redirect('/')

urlpatterns = [
    path('', views.AllListView.as_view(), name='all_list'),
    path('free/', views.FreeListView.as_view(), name='free_list'),

    path('broadcasting_list/', views.BroadcastingListView.as_view(), name='broadcasting_list'),
    path('musicvideo_list/', views.MusicvideoListView.as_view(), name='musicvideo_list'),
    path('show_list/', views.ShowListView.as_view(), name='show_list'),
    path('etc_list/', views.EtcListView.as_view(), name='etc_list'),

    path('write/', views.free_write_view, name='free_write'),
    path('<int:pk>/', views.free_detail_view, name='free_detail'),
    path('<int:pk>/edit/', views.free_edit_view, name='free_edit'),
    path('<int:pk>/delete/', views.free_delete_view, name='free_delete'),
    path('download/<int:pk>', views.free_download_view, name="free_download"),

    path('<int:pk>/comment/write/', views.comment_write_view, name='comment_write'),
    path('<int:pk>/comment/delete/', views.comment_delete_view, name='comment_delete'),

]

urlpatterns += static(settings.MEDIA_URL, protected_file, document_root=settings.MEDIA_ROOT)