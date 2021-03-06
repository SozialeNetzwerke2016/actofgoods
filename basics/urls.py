"""actofgoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'basics'

urlpatterns = [
    url(r'^$', views.actofgoods_startpage, name='actofgoods_startpage'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^chat/(?P<roomname>[A-Za-z0-9]+)/$', views.chat_room, name='chat_room'),
    url(r'^chat/(?P<roomname>[A-Za-z0-9]+)/kick_user$', views.kick_user, name='kick_user'),

    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/$', views.claim, name='claim'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/refresh/$', views.claim_refresh, name='claim_refresh'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/post/$', views.claim_post, name='claim_post'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/delete/$', views.claim_delete, name='claim_delete'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/needs/$', views.claim_needs, name='claim_needs'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/infos/$', views.claim_information, name='claim_information'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/reportNeed/$', views.claim_reportNeed, name='claim_reportNeed'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/reportInfo/$', views.claim_reportInfo, name='claim_reportInfo'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/follow/$', views.claim_follow, name='claim_follow'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/unfollow/$', views.claim_unfollow, name='claim_unfollow'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/like/$', views.claim_like, name='claim_like'),
    url(r'^claim/(?P<name>[A-Za-z0-9 ]+)/unlike/$', views.claim_unlike, name='claim_unlike'),

    url(r'^faq_signin/$', views.faq_signin, name='faq_signin'),
    url(r'^faq_startpage/$', views.faq_startpage, name='faq_startpage'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/filter/$', views.home_filter, name='home_filter'),
    url(r'^home/unfollow/$', views.home_unfollow, name='home_unfollow'),
    url(r'^immediate_aid/$', views.immediate_aid, name='immediate_aid'),

    url(r'^information_all/$', views.information_all, name='information_all'),
    url(r'^information_all/filter/$', views.information_filter, name='information_filter'),
    url(r'^information_all/report/$', views.report_information, name='report_information'),
    url(r'^information_all/follow/$', views.follow, name='follow'),
    url(r'^information_all/unfollow/$', views.unfollow, name='unfollow'),
    url(r'^information_all/like/$', views.like_information, name='like_information'),
    url(r'^information_all/unlike/$', views.unlike_information, name='unlike_information'),
    url(r'^information_new/$', views.information_new, name='information_new'),
    url(r'^information_view/(?P<pk>\d+)/$', views.information_view, name='information_view'),
    url(r'^information_view/(?P<pk>\d+)/comment$', views.information_view_comment, name='information_view_comment'),
    url(r'^information_view/comment/delete/(?P<pk_inf>\w+)/(?P<pk_comm>\w+)/$', views.information_delete_comment, name='information_delete_comment'),
    url(r'^information_update/(?P<pk>\d+)$', views.information_update, name='information_update'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^needs_all/$', views.needs_all, name='needs_all'),
    url(r'^needs_all/filter/$', views.needs_filter, name='needs_filter'),
    url(r'^needs_all/report/$', views.report_need, name='report_need'),
    url(r'^needs_help/(?P<id>\d+)/$', views.needs_help, name='needs_help'),
    url(r'^needs_help/(?P<id>\d+)/(?P<group_id>\d+)$', views.needs_help_group, name='needs_help_group'),
    url(r'^needs_new/$', views.needs_new, name='needs_new'),
    url(r'^needs_finish/(?P<roomname>[A-Za-z0-9]+)/$', views.needs_finish, name='needs_finish'),
    url(r'^needs_view/(?P<pk>\d+)/$', views.needs_view, name='needs_view'),

    url(r'^privacy/$', views.privacy, name='privacy'),

    url(r'^profil/$', views.profil, name='profil'),
    url(r'^profil_edit/$', views.profil_edit, name='profil_edit'),
    url(r'^profil_delete/$', views.profil_delete, name='profil_delete'),

    url(r'^register/$', views.register, name='register'),

    url(r'^reset_password/$', views.reset_password_page, name='reset_password_page'),
    url(r'^reset_password_confirmation/$', views.reset_password_confirmation, name='reset_password_confirmation'),

	url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^comment/report/(?P<pk>\d+)/$', views.report_comment, name='report_comment'),
    url(r'^verification/(?P<id>\w+)$', views.verification, name='verification'),
	url(r'^need_edit/(?P<pk>\w+)$', views.need_edit, name='need_edit'),
    url(r'^need_delete/(?P<pk>\w+)$', views.need_delete, name='need_delete'),
    url(r'^info_edit/(?P<pk>\w+)$', views.info_edit, name='info_edit'),
    url(r'^info_delete/(?P<pk>\w+)$', views.info_delete, name='info_delete'),
    url(r'^comm_delete/(?P<pk>\w+)$', views.comm_delete, name='comm_delete'),
    url(r'^home/delete_comment_timeline/(?P<pk>\w+)$', views.delete_comment_timeline, name='delete_comment_timeline'),

    url(r'^groups/all/$', views.groups_all, name='groups_all'),
    url(r'^groups/detail/(?P<name>[A-Za-z0-9 ]+)/$', views.group_detail, name='group_detail'),
    url(r'^groups/edit/(?P<pk>\d+)/$', views.group_edit, name='group_edit'),
    url(r'^groups/leave/(?P<pk>\d+)/$', views.group_leave, name='group_leave'),
    url(r'^group/(?P<name>[A-Za-z0-9 ]+)/$', views.group_detail_for_user, name='group_detail_for_user'),
]
