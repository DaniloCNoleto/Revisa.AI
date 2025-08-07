from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='home'),  # ← Essa linha trata a rota "/"
    path('login/', views.login_view, name='login'),
    path('registro/', views.register_view, name='register'),
    path('upload/', views.upload_view, name='upload'),
    path('modo-revisao/', views.modo_revisao_view, name='modo_revisao'),
    path('acompanhamento/', views.acompanhamento_view, name='acompanhamento'),
    path('cancelar-revisao/<int:revision_id>/', views.cancelar_revisao_view, name='cancelar_revisao'),
    path('resultados/', views.resultados_view, name='resultados'),
    path('historico/', views.historico_view, name='historico'),
    path('resultados/<int:revision_id>/', views.resultados_view, name='resultados'),
    path('logout/', views.logout_view, name='logout'),
    path('email-sent-confirmation/', views.email_sent_confirmation_view, name='email_sent_confirmation'), # Nova URL
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), # Nova URL para o link de ativação
    # --- NOVAS URLS PARA RESET DE SENHA ---

    # 1. Página para solicitar o reset (pede o e-mail)
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='revisor/password_reset_form.html',
            email_template_name='revisor/password_reset_email.html',
            subject_template_name='revisor/password_reset_subject.txt',
            success_url='/password_reset/done/'
        ), 
        name='password_reset'),

    # 2. Página de sucesso após o pedido de reset
    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='revisor/password_reset_done.html'
        ), 
        name='password_reset_done'),

    # 3. Link de reset enviado por e-mail (contém UID e token)
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='revisor/password_reset_confirm.html',
            success_url='/reset/done/'
        ), 
        name='password_reset_confirm'),

    # 4. Página de sucesso após a senha ser alterada
    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='revisor/password_reset_complete.html'
        ), 
        name='password_reset_complete'),
    path('password_change/', 
        auth_views.PasswordChangeView.as_view(
            template_name='revisor/password_change_form.html',
            success_url='/password_change/done/'
        ),
        name='password_change'),
    
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='revisor/password_change_done.html'
        ),
        name='password_change_done'),

        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)