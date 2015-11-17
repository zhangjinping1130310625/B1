from django.conf.urls import patterns, include, url
from django.contrib import admin
from managebook import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Manage/$',views.Manage),
    url(r'^AddAuthor/$',views.AddAuthor),
    url(r'^AddBook/$',views.AddBook),
    url(r'^SearchBook/$',views.SearchBook),
    url(r'^AddAuthorResult/$',views.AddAuthorResult),
    url(r'^AddBookResult/$',views.AddBookResult),
    url(r'^SearchResult/$',views.SearchResult),
    url(r'^ShowBook/$',views.ShowBook),
    url(r'InformationBook/(.+)/$',views.InformationBook),
    url(r'UpdataBook/(.+)/$',views.UpdataBook),
    url(r'DeleteBook/(.+)/$',views.DeleteBook),
)

