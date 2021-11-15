from django.urls import path
from admin_app.views import AddUser, AddMember, AddGuest, AddDepartment, ViewAttendance, ViewFinanceInfo, Login, AddRole, \
    Logout, FindMemberById, UpdateMemberById, DeleteMemberById, Test, ApproveGuestById, RejectGuestById


urlpatterns =[

path('welcome/user', AddUser,name='admin'),
path('view/role', AddRole,name='role'),
path('view/member', AddMember,name='member'),
path('view/guest', AddGuest,name='guest'),
path('view/department', AddDepartment,name='department'),
path('view/attendance', ViewAttendance,name='attendance'),

path('finance/info', ViewFinanceInfo,name='finance'),
path('admin/login', Login, name='login'),
path('logout', Logout, name='logout'),
path('find/member/<int:mid>', FindMemberById, name='findmb'),
path('update/member', UpdateMemberById, name='updatememb'),


path('trash/member/<int:mid>', DeleteMemberById, name='trash'),
path('approve/booking/<int:id>', ApproveGuestById, name='approveguest'),
path('reject/booking/<int:id>', RejectGuestById, name='rejectguest'),





path('trash/', Test, name='trashs'),

]