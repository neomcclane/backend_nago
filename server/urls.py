from django.conf.urls import url
from server import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^editProfile/', views.editProfile, name='editProfile'),
    url(r'^existUsername/', views.existUsername, name='existUsername'),
    url(r'^existEmail/', views.existEmail, name='existEmail'),
    url(r'^sendEmailCode/', views.sendEmailCode, name='sendEmailCode'),
    url(r'^viewNagoUsers/', views.viewNagoUsers, name='viewNagoUsers'),
    url(r'^viewProfileUser/', views.viewProfileUser, name='viewProfileUser'),
    url(r'^sendInvitationFriend/', views.sendInvitationFriend, name='sendInvitationFriend'),
    url(r'^invitationViewFriends/', views.invitationViewFriends, name='invitationViewFriends'),
    url(r'^viewMyFriends/', views.viewMyFriends, name='viewMyFriends'),
    url(r'^responseInvitationFriendAccept/', views.responseInvitationFriendAccept, name='responseInvitationFriendAccept'),
    url(r'^validateCode/', views.validateCode, name='validateCode'),
    url(r'^viewProfileFriend/', views.viewProfileFriend, name='viewProfileFriend'),
    url(r'^responseInvitationFriendCancel/', views.responseInvitationFriendCancel, name='responseInvitationFriendCancel'),
    url(r'^loanSolicitude/', views.loanSolicitude, name='loanSolicitude'),
    url(r'^viewFriendsLoans/', views.viewFriendsLoans, name='viewFriendsLoans'),
    url(r'^viewLoanFriend/', views.viewLoanFriend, name='viewLoanFriend'),
    url(r'^payLoanFriend/', views.payLoanFriend, name='payLoanFriend'),
    url(r'^viewFriendsLoansPay/', views.viewFriendsLoansPay, name='viewFriendsLoansPay'),
    url(r'^viewProfileSelf/', views.viewProfileSelf, name='viewProfileSelf'),
    url(r'^userNagoFilter/', views.userNagoFilter, name='userNagoFilter'),
    url(r'^validatePin/', views.validatePin, name='validatePin'),
    url(r'^viewHistoryProfile/', views.viewHistoryProfile, name='viewHistoryProfile'),
    url(r'^viewHistoryDetail/', views.viewHistoryDetail, name='viewHistoryDetail'),
    url(r'^lendingSolicitude/', views.lendingSolicitude, name='lendingSolicitude'),
    url(r'^viewExpectedProfile/', views.viewExpectedProfile, name='viewExpectedProfile'),
    url(r'^viewAmountMarket/', views.viewAmountMarket, name='viewAmountMarket'),
    url(r'^viewInterestMarket/', views.viewInterestMarket, name='viewInterestMarket'),
    url(r'^viewDeadlineMarket/', views.viewDeadlineMarket, name='viewDeadlineMarket'),
    url(r'^viewRequestedAccount/', views.viewRequestedAccount, name='viewRequestedAccount'),
    url(r'^viewInvestedAccount/', views.viewInvestedAccount, name='viewInvestedAccount'),
    url(r'^viewRequestdUser/', views.viewRequestdUser, name='viewRequestdUser'),
    url(r'^viewInvestedUser/', views.viewInvestedUser, name='viewInvestedUser'),
    url(r'^checkInUser/', views.checkInUser, name='checkInUser'),
    url(r'^checkOutUser/', views.checkOutUser, name='checkOutUser'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
