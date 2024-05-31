from rest_framework.throttling import UserRateThrottle

class SendFriendRequestThrottle(UserRateThrottle):
    scope = 'send_friend_request'
