from django.urls import path

from django.contrib.auth import views as auth_views

from django.conf import settings

from . import views

urlpatterns=[

	path('', views.home, name='home'),

	path('hiddenIndex/', views.hiddenIndex, name='hiddenIndex'),

	path('services/', views.services, name='services'),

	path('plan/', views.plan, name='plan'),

	path('otherpayment/', views.otherpayment, name='otherpayment'),

	path('about/', views.about, name='about'),

	path('wiretransfer/', views.wiretransfer, name='wiretransfer'),

	path('cashmailing/', views.cashmailing, name='cashmailing'),

	path('renewableEnergy/', views.renewableEnergy, name='renewableEnergy'),

	path('financialService/', views.financialService, name='financialService'),

	path('energy/', views.energy, name='energy'),

	path('portfolioManagement/', views.portfolioManagement, name='portfolioManagement'),

	path('financialAdvising/', views.financialAdvising, name='financialAdvising'),

	path('faq/', views.faq, name='faq'),

	path('signin/', views.signin, name='signin'),

	path('privacy/', views.privacy, name='privacy'),

	path('main-view/', views.main_view, name='main-view'),

	path('main-view/<str:ref_code>/', views.main_view, name='main-view'),

	path('signup/', views.signup, name='signup'),

	path('terms/', views.terms, name='terms'),

	path('realestate/', views.realestate, name='realestate'),

	path('crypto/', views.crypto, name='crypto'),

	path('forex/', views.forex, name='forex'),

	path('nft/', views.nft, name='nft'),

	path('contact/', views.contact, name='contact'),

	path('stocks/', views.stocks, name='stocks'),

	path('card/', views.card, name='card'),

	path('agriculture/', views.agriculture, name='agriculture'),

	path('gold/', views.gold, name='gold'),

	path('retirement/', views.retirement, name='retirement'),

	path('dashboard/', views.dashboard, name='dashboard'),

	path('portfolioDeposit/', views.dashboard, name='portfolioDeposit'),

	path('admindashboard/', views.admindashboard, name="admindashboard"),

	path('deposit/', views.deposit, name='deposit'),

	path('withdrawal/', views.withdrawal, name='withdrawal'),

	path('history/', views.history, name='history'),

	path('pending_deposit/', views.pending_deposit, name='pending_deposit'),

	path('pending_withdrawal/', views.pending_withdrawal, name='pending_withdrawal'),

	path('pending_bonus/', views.pending_bonus, name='pending_bonus'),

	path('completed_transaction/', views.completed_transaction, name='completed_transaction'),

	path('myreferals/', views.myreferals, name='myreferals'),

	path('confirm_withdrawal/', views.confirm_withdrawal, name='confirm_withdrawal' ),

	path('update_withdrawal/<str:pk>/', views.update_withdrawal, name='update_withdrawal' ),

	path('decline_wihdrawal/<str:pk>/', views.decline_wihdrawal, name='decline_wihdrawal'),

	path('confirm_deposit/', views.confirm_deposit, name='confirm_deposit' ),

	path('update_payment/<str:pk>/', views.update_payment, name='update_payment' ),

	path('account_settings/', views.account_settings, name='account_settings'),

	path('create_bonus/', views.create_bonus, name='create_bonus'),

	path('use_bonus/', views.use_bonus, name='use_bonus'),

	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="excelprojremakemainapp/password_reset.html"), name='reset_password'),

	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="excelprojremakemainapp/password_reset_done.html"), name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="excelprojremakemainapp/password_reset_form.html"), name='password_reset_confirm'),

	path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name="excelprojremakemainapp/password_reset_complete.html"), name='password_reset_complete'),
	path('notifications/', views.notifications, name='notifications'),
	path('transfer_funds/', views.transfer_funds, name='transfer_funds'),
	path('video_page/', views.video_page, name='video_page'),
	path('reinvest/', views.reinvest, name='reinvest'),
	path('loan/', views.loan, name='loan'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('verify_otp/', views.verify_otp, name="verify_otp"),

	path('prospectorDepositMethod/', views.prospectorDepositMethod, name='prospectorDepositMethod'),
	path('UpstreamDepositMethod/', views.UpstreamDepositMethod, name='UpstreamDepositMethod'),
	path('PetrolMaxDepositMethod/', views.PetrolMaxDepositMethod, name='PetrolMaxDepositMethod'),
	path('premiumHedgeDepositMethod/', views.premiumHedgeDepositMethod, name='premiumHedgeDepositMethod'),
	path('eliteDepositMethod/', views.eliteDepositMethod, name='eliteDepositMethod'),

	path('prospectorDeposit/', views.prospectorDeposit, name='prospectorDeposit'),
	path('UpstreamDeposit/', views.UpstreamDeposit, name='UpstreamDeposit'),
	path('PetrolMaxDeposit/', views.PetrolMaxDeposit, name='PetrolMaxDeposit'),
	path('premiumHedgeDeposit/', views.premiumHedgeDeposit, name='premiumHedgeDeposit'),
	path('eliteDeposit/', views.eliteDeposit, name='eliteDeposit'),
	path('investmentPlans/', views.investmentPlans, name='investmentPlans'),
	path('logout/', views.logoutuser, name='logout'),
]
'''
	path('retirementDeposit/', views.retirementDeposit, name='retirementDeposit'),
	path('realestateDeposit/', views.realestateDeposit, name='realestateDeposit'),
	path('cryptoDeposit/', views.cryptoDeposit, name='cryptoDeposit'),
	path('stocksDeposit/', views.stocksDeposit, name='stocksDeposit'),
'''