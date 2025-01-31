from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.request import Request


class IsAuthenticatedForGetOrWriteOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method == 'POST':
            return True
        return request.user.is_active


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)


class IsPremiumUser(BasePermission):
    def has_permission(self, request: Request, view):
        print(bool(request.user and request.user.is_premium))
        print(request.user)
        return bool(request.user and request.user.is_premium)


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.role == 'manager' or request.user.role == 'admin')


class IsSellerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'seller')


class IsBuyerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'buyer')
