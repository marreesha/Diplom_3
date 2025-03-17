class URLS:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    REGISTER_PAGE = BASE_URL + 'register'
    LOGIN_PAGE = BASE_URL + 'login'
    FORGOT_PASSWORD_PAGE = BASE_URL + 'forgot-password'
    RESET_PASSWORD_PAGE = BASE_URL + 'reset-password'
    PROFILE_PAGE = BASE_URL + 'account/profile'
    ACCOUNT_PAGE = BASE_URL + 'account'
    ORDER_HISTORY_PAGE = BASE_URL + 'account/order-history'
    ORDERS_FEED_PAGE = BASE_URL + 'feed'

    REGISTRATION_ENDPOINT = "api/auth/register"
    LOGIN_ENDPOINT = "api/auth/login"
    USER_ENDPOINT = "api/auth/user"
    ORDER_ENDPOINT = "api/orders"
    DELETE_ENDPOINT = "api/auth/user"
